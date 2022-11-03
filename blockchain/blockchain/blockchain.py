from __future__ import annotations

from ..pool.pooloftransactions import PoolOfTransactions
from ..transaction.utxo import Utxo
from ..types import TransactionContent
from ..pool.pool import Pool
from ..block.block import Block, BlockData
from flask import jsonify, make_response, Response


class Blockchain:
    def __init__(self, transactionPool: PoolOfTransactions) -> None:
        self.chain: list[BlockData] = []
        self.transactionPool = transactionPool

    def generate(self, transaction: TransactionContent) -> list[BlockData]:
        """
        Build a new block or the Genesis block if needed
        :param transaction: data of
        timestamp: datetime
        senderID: int
        receiverID: int
        amount: float
        :return: chain ELSE Genesis block
        """
        last_block: BlockData | None = None
        if len(self.chain) > 0:
            last_block = self.chain[-1]

        genesis_block = Block(1, transaction).generate_block(last_block)
        self.chain.append(genesis_block)

        return self.chain

    def get_highest_value(self, transactions: list) -> TransactionContent:
        """
        Get the transactions with the highest value
        :param transactions: pool of unvalifated transactions
        :return: transaction with most value / PoW
        """
        current_transaction = transactions[-1]
        highest_value_transaction = current_transaction

        for t in transactions:
            if t["amount"] > current_transaction["amount"]:
                highest_value_transaction = t

        return highest_value_transaction

    def appendBlock(self, pool: Pool) -> Response:
        """
        Add the block to the chain
        :param pool: list of transactions
        :return: extended list of transactions
        """
        if not pool.list:
            return make_response(jsonify({"info": "current transactions amount = 0", "status": "500"}), 500)

        transaction = self.get_highest_value(pool.list)
        pool.list.remove(transaction)

        if not self.chain:
            return make_response(jsonify(self.generate(transaction)), 200)

        previous_block = self.chain[-1]
        current_block = Block(previous_block["index"] + 1,
                              transaction, previous_block["currentHash"]).generate_block(previous_block)
        self.chain.append(current_block)

        return make_response(jsonify(self.chain), 200)

    def modify_memory(self) -> Response:
        """
        reset the blockchain
        """
        self.chain.clear()
        return make_response(
            jsonify({"Modify Memory": "https://roll20.net/compendium/dnd5e/Modify%20Memory#content",
                     "status": "200"}), 200)

    def get_length(self) -> Response:
        """
        get the length of the chain
        :return: json list
        """
        return make_response(jsonify({"info": len(self.chain)}), 200)

    def utxo_balance(self, transaction_output: Utxo) -> float:
        """
        walk the line
        :param transaction_output: Utxo
        :return: balance result
        """
        result: float = transaction_output["amount"]
        for block in self.chain:
            # break if not timestamp equals timestamp
            if transaction_output["timestamp"] < block["transaction"]["timestamp"]:
                break

            if transaction_output["receiverID"] == block["transaction"]["receiverID"]:
                result = result + block["transaction"]["amount"]

        return result

    def balance_by_uid(self, userID: int) -> float | None:
        transactionRemainder = self.transactionPool.open_remainder_by_uid(userID)
        if not transactionRemainder:
            return None
        return self.utxo_balance(transactionRemainder)

    def getBalanceByUid(self, balanceReq: Any):
        try:
            userID: float = float(balanceReq["user_id"])
        except:
            return make_response(jsonify({"info": "malformed request", "status": "400"}), 400)

        balance = self.balance_by_uid(userID)
        if not balance:
            return make_response(jsonify({"info": "no transaction history found for this user", "status": "404"}), 404)

        return make_response(jsonify({"balance": balance}), 200)
