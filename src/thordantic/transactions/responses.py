from pydantic import NonNegativeInt, Field
from thordantic.common.clause import Clause
from thordantic.types.hex import HexInt, HexStr
from thordantic.types.thor import Address, TransactionId, BlockId, BlockRef
from thordantic.config import ThorModel

class TransactionMetaResponse(ThorModel):
    """
    Transaction meta response from /transactions/{id} endpoint.
    """
    block_id: BlockId = Field(alias="blockID")
    block_number: NonNegativeInt = Field(alias="blockNumber")
    block_timestamp: NonNegativeInt = Field(alias="blockTimestamp")

class TransactionResponse(ThorModel):
    """
    Transaction response from /transactions/{id} endpoint.
    """
    id: TransactionId
    type: NonNegativeInt
    origin: Address
    delegator: Address | None = None
    size: NonNegativeInt
    chain_tag: NonNegativeInt = Field(alias="chainTag")
    block_ref: BlockRef = Field(alias="blockRef")
    expiration: NonNegativeInt
    clauses: list[Clause]
    gas_price_coef: NonNegativeInt | None = Field(alias="gasPriceCoef", default=None)
    max_fee_per_gas: HexInt | None = Field(alias="maxFeePerGas", default=None)
    max_priority_fee_per_gas: HexInt | None = Field(alias="maxPriorityFeePerGas", default=None)
    gas: NonNegativeInt
    depends_on: TransactionId | None = Field(alias="dependsOn", default=None)
    nonce: HexStr
    meta: TransactionMetaResponse

class TransactionReceiptEvent(ThorModel):
    """
    Transaction receipt event from /transactions/{id}/receipt endpoint.
    """
    address: Address
    topics: list[HexStr]
    data: HexStr

class TransactionReceiptTransfer(ThorModel):
    """
    Transaction receipt transfer from /transactions/{id}/receipt endpoint.
    """
    sender: Address
    recipient: Address
    amount: HexInt


class TransactionReceiptOutputResponse(ThorModel):
    """
    The transaction receipt outputs response from /transactions/{id}/receipt endpoint.
    """
    contract_address: Address | None = Field(alias="contractAddress", default=None)
    events: list[TransactionReceiptEvent]
    transfers: list[TransactionReceiptTransfer]

class TransactionReceiptMetaResponse(ThorModel):
    """
    The transaction receipt meta response from /transactions/{id}/receipt endpoint.
    """
    block_id: BlockId = Field(alias="blockID")
    block_number: NonNegativeInt = Field(alias="blockNumber")
    block_timestamp: NonNegativeInt = Field(alias="blockTimestamp")
    tx_id: TransactionId = Field(alias="txID")
    tx_origin: Address = Field(alias="txOrigin")

class TransactionReceiptResponse(ThorModel):
    """
    Transaction receipt response from /transactions/{id}/receipt endpoint.
    """
    type: NonNegativeInt | None = None
    gas_used: NonNegativeInt = Field(alias="gasUsed")
    gas_payer: Address = Field(alias = "gasPayer")
    paid: HexInt
    reward: HexInt
    reverted: bool
    outputs: list[TransactionReceiptOutputResponse]
    meta: TransactionReceiptMetaResponse
