from typing import Annotated
from pydantic import BeforeValidator
from pydantic.functional_serializers import PlainSerializer
from pydantic_core import PydanticCustomError
import re

ADDRESS_PATTERN = re.compile("^0x[a-fA-F0-9]{40}$")

def _parse_address(v: str | bytes) -> str:
    if isinstance(v, str):
        if not ADDRESS_PATTERN.match(v):
            raise PydanticCustomError("address_invalid", "expected 0x followed by 40 hex chars")
        # Normalize: lower-case hex string (optional)
        return v.lower()

    if isinstance(v, (bytes, bytearray)):
        if len(v) != 20:
            raise PydanticCustomError("address_length", "expected 20-byte value")
        return "0x" + bytes(v).hex().lower()

    raise PydanticCustomError("address_type", "expected 0x string or 20-byte value")

Address = Annotated[
    str,
    BeforeValidator(_parse_address),
    PlainSerializer(lambda v: v, when_used="json"),  # JSON: keep checksum string
]