from thordantic.types.thor import Address, BlockRef
from pydantic import Field, NonNegativeInt
from thordantic.common.clause import Clause
from thordantic.config import ThorModel


class InspectClausesRequest(ThorModel):
    """
    Inspect clauses request for /accounts/*
    """
    proved_work: NonNegativeInt | None = Field(alias="provedWork", default=None)
    gas_payer: Address | None = Field(alias = "gasPayer", default=None)
    expiration: NonNegativeInt | None = None
    block_ref: BlockRef | None = Field(alias = "blockRef", default=None)
    clauses: list[Clause]
    gas: NonNegativeInt | None = None
    gas_price: NonNegativeInt | None = Field(alias = "gasPrice", default=None)
    caller: Address | None = None