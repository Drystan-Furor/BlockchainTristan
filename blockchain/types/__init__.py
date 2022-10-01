from datetime import datetime
from typing import TypedDict


class TransactionData(TypedDict):
    timestamp: datetime
    senderID: int
    receiverID: int
    amount: float


class BlockData(TypedDict):
    index: int
    timestamp: datetime
    proof: int
    priorHash: str
    currentHash: str
    transaction: TransactionData
