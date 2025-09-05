from typing import Union
from pydantic import NonNegativeInt, Field
from thordantic.common.clause import Clause
from thordantic.config import ThorModel
from thordantic.transactions.responses import TransactionReceiptOutputResponse
from thordantic.types.hex import HexStr, HexInt
from thordantic.types.thor import BlockId, TransactionId, BlockRef, Address

class BlockTransactionResponse(ThorModel):
    """
    Block transaction response from /blocks/{revision} endpoint.
    """
    id: TransactionId
    type: NonNegativeInt
    chain_tag: NonNegativeInt = Field(alias="chainTag")
    block_ref: BlockRef = Field(alias="blockRef")
    expiration: NonNegativeInt
    clauses: list[Clause]
    gas_price_coef: NonNegativeInt | None = Field(alias="gasPriceCoef", default=None)
    max_fee_per_gas: HexInt | None = Field(alias="maxFeePerGas", default=None)
    max_priority_fee_per_gas: HexInt | None = Field(alias="maxPriorityFeePerGas", default=None)
    gas: NonNegativeInt
    origin: Address
    delegator: Address | None = None
    nonce: HexStr
    depends_on: TransactionId | None = Field(alias="dependsOn", default=None)
    size: NonNegativeInt
    gas_used: NonNegativeInt = Field(alias="gasUsed")
    gas_payer: Address = Field(alias="gasPayer")
    paid: HexInt
    reward: HexInt
    reverted: bool
    outputs: list[TransactionReceiptOutputResponse]

class ExpandedBlockResponse(ThorModel):
    """
    Expanded Block response from /blocks/{revision} endpoint.
    """
    number: NonNegativeInt
    id: BlockId
    size: NonNegativeInt
    parent_id: BlockId = Field(alias="parentID")
    timestamp: NonNegativeInt
    gas_limit: NonNegativeInt = Field(alias="gasLimit")
    beneficiary: Address
    gas_used: NonNegativeInt = Field(alias="gasUsed")
    total_score: NonNegativeInt = Field(alias="totalScore")
    txs_root: HexStr = Field(alias="txsRoot")
    txs_features: NonNegativeInt = Field(alias="txsFeatures")
    state_root: HexStr = Field(alias="stateRoot")
    receipts_root: HexStr = Field(alias="receiptsRoot")
    com: bool
    signer: Address
    is_trunk: bool = Field(alias="isTrunk")
    is_finalized: bool = Field(alias="isFinalized")
    base_fee_per_gas: HexInt | None = Field(alias="baseFeePerGas", default=None)
    transactions: list[BlockTransactionResponse]

class CompressedBlockResponse(ThorModel):
    """
    Compressed Block response from /blocks/{revision}endpoint.
    """
    number: NonNegativeInt
    id: BlockId
    size: NonNegativeInt
    parent_id: BlockId = Field(alias="parentID")
    timestamp: NonNegativeInt
    gas_limit: NonNegativeInt = Field(alias="gasLimit")
    beneficiary: Address
    gas_used: NonNegativeInt = Field(alias="gasUsed")
    total_score: NonNegativeInt = Field(alias="totalScore")
    txs_root: HexStr = Field(alias="txsRoot")
    txs_features: NonNegativeInt = Field(alias="txsFeatures")
    state_root: HexStr = Field(alias="stateRoot")
    receipts_root: HexStr = Field(alias="receiptsRoot")
    com: bool
    signer: Address
    is_trunk: bool = Field(alias="isTrunk")
    is_finalized: bool = Field(alias="isFinalized")
    base_fee_per_gas: HexInt | None = Field(alias="baseFeePerGas", default=None)
    transactions: list[TransactionId]

class RawBlockResponse(ThorModel):
    """
    Raw Block response from /blocks/{revision} endpoint.
    """
    raw: HexStr