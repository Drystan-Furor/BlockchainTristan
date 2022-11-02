from __future__ import annotations

from typing import Tuple, TypedDict

class UtxoOutput(TypedDict):
    timestamp:      float
    previousHash:   str
    id:             str
    hash:           str
    amount:         float
    receiverID:     int
    isRemainder:    bool

class TransactionData(TypedDict):
    timestamp:  float
    senderID:   int
    receiverID: int
    amount:     float
    publicKey:  str
    signature:  str
    inputHash:  str
    transactionOutput: Tuple[UtxoOutput, UtxoOutput] | None

class BlockData(TypedDict):
    index:        int
    timestamp:    float
    proof:        int
    priorHash:    str
    currentHash:  str
    transaction:  TransactionData
