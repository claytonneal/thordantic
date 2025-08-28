from thordantic.types.address import Address
from thordantic.types.hex import HexInt, HexStr
from thordantic.config import ThorModel

class Clause(ThorModel):
    to: Address
    value: HexInt
    data: HexStr