from typing import Annotated
from pydantic import AfterValidator, BeforeValidator
from pydantic.functional_serializers import PlainSerializer
from pydantic_core import PydanticCustomError

# ---------- helpers ----------

def _is_hex_prefixed(s: str) -> bool:
    return isinstance(s, str) and s.startswith("0x")

def _validate_hex_chars(s: str) -> None:
    try:
        int(s[2:] if s.startswith("0x") else s, 16)
    except Exception:
        raise PydanticCustomError("hex_chars", "invalid hex characters")

# ---------- HexStr (any-length 0x-hex string) ----------

def _validate_hex_str(v: str) -> str:
    if not isinstance(v, str) or not _is_hex_prefixed(v):
        raise PydanticCustomError("hex_str", "expected 0x-prefixed hex string")
    _validate_hex_chars(v)
    return v.lower()

HexStr = Annotated[str, AfterValidator(_validate_hex_str)]

# ---------- HexBytes (even length 0x-hex string) ----------

def _validate_hex_bytes(v: str) -> str:
    v = _validate_hex_str(v)
    if (len(v) - 2) % 2 != 0:
        raise PydanticCustomError("hex_even", "expected even-length 0x… hex bytes")
    return v

HexBytes = Annotated[str, AfterValidator(_validate_hex_bytes)]

# ---------- HexInt (quantity that accepts int or 0x…, serializes to 0x) ----------
# Note: "0x" is parsed as 0

def _parse_hex_int(v: int | str) -> int:
    # Reject bools (they're instances of int in Python)
    if isinstance(v, bool):
        raise PydanticCustomError("hex_int", "expected int or 0x… hex quantity (bool not allowed)")

    if isinstance(v, int):
        return v

    if isinstance(v, str):
        s = v.strip()
        if s[:2].lower() == "0x":
            hex_part = s[2:]
            if hex_part == "":      # support bare "0x" as zero
                return 0
            try:
                return int(hex_part, 16)
            except ValueError:
                raise PydanticCustomError("hex_int", "invalid hex digits in 0x… quantity")
        # optionally: allow plain decimal strings
        # if s.isdigit(): return int(s)

    raise PydanticCustomError("hex_int", "expected int or 0x… hex quantity")

HexInt = Annotated[
    int,
    BeforeValidator(_parse_hex_int),
    PlainSerializer(lambda x: hex(int(x)), when_used="json"),  # emits '0x0' for 0
]

# ---------- Bounded hex string factory, e.g. BoundHexStr[16]  ----------

def bound_hex_str(n: int):
    """Create a 0x-hex string type with exactly n hex chars after 0x."""
    def _validator(v: str) -> str:
        v = _validate_hex_str(v)
        if len(v) != 2 + n:
            raise PydanticCustomError("hex_len", f"expected {n} hex chars after 0x")
        return v
    return Annotated[str, AfterValidator(_validator)]

HexStr16 = bound_hex_str(16)

# ---------- HexUInt (unsigned int: >= 0, serializes as 0x…) ----------

def _parse_hex_uint(v: int | str) -> int:
    # Accept plain integers
    if isinstance(v, int):
        if v < 0:
            raise PydanticCustomError("uint_negative", "unsigned integer cannot be negative")
        return v

    # Accept 0x-prefixed strings
    if isinstance(v, str) and v.startswith("0x"):
        try:
            n = int(v, 16)
        except Exception:
            raise PydanticCustomError("uint_hex", "invalid hex string for unsigned int")
        if n < 0:
            raise PydanticCustomError("uint_negative", "unsigned integer cannot be negative")
        return n

    raise PydanticCustomError("hex_uint", "expected non-negative int or 0x… string")


HexUInt = Annotated[
    int,
    BeforeValidator(_parse_hex_uint),
    PlainSerializer(lambda x: hex(int(x)), when_used="json"),  # JSON always as 0x…
]