from __future__ import annotations

from typing import Tuple, TypedDict

class UtxoOutput(TypedDict):
    id: str
    hash: str
    amount: float
    isRemainder: bool

class TransactionData(TypedDict):
    timestamp:  float
    senderID:   int
    receiverID: int
    amount:     float
    balance:    float
    transactionOutput: Tuple[UtxoOutput, UtxoOutput] | None

class BlockData(TypedDict):
    index:        int
    timestamp:    float
    proof:        int
    priorHash:    str
    currentHash:  str
    transaction:  TransactionData
