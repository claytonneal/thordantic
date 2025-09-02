from thordantic.types.thor import Address
from thordantic.types.hex import HexInt, HexStr
from thordantic.config import ThorModel

class Clause(ThorModel):
    to: Address | None = None
    value: HexInt
    data: HexStr