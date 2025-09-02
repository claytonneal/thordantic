from typing import List
from thordantic.types.address import Address
from thordantic.types.hex import HexInt, HexStr
from thordantic.config import ThorModel
from pydantic import Field, RootModel, NonNegativeInt


class AccountDetailResponse(ThorModel):
    """
    Account detail response for /accounts/{address} endpoint.
    """
    balance: HexInt
    energy: HexInt
    has_code: bool = Field(alias="hasCode", default=False)

class InspectClauseEvent(ThorModel):
    """
    Inspect clause event for /accounts/*
    """
    address: Address
    topics: list[HexStr]
    data: HexStr

class InspecClauseTransfer(ThorModel):
    """
    Inspect clause transfer for /accounts/*
    """
    sender: Address
    recipient: Address
    amount: HexInt

class InspectClauseResponse(ThorModel):
    """
    Inspect clause response for /accounts/* for a single clause
    """
    data: HexStr
    events: list[InspectClauseEvent]
    transfers: list[InspecClauseTransfer]
    gas_used: NonNegativeInt = Field(alias="gasUsed")
    reverted: bool
    vm_error: str = Field(alias = "vmError")


class InspectClausesResponse(RootModel[List[InspectClauseResponse]]):
    """
    Inspect clauses response for /accounts/* for all clauses
    """
    pass

class ContractByteCodeResponse(ThorModel):
    """
    Get contract bytecode response for /accounts/{address}/code endpoint.
    """
    code: HexStr

class StoragePositionValueResponse(ThorModel):
    """
    Get storage position value response for /accounts/{address}/storage/{key} endpoint.
    """
    value: HexStr


