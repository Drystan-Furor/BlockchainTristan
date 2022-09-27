from blockchain import Blockchain
from blockchain.mempool.mempool import Mempool
from flask import jsonify, make_response
import datetime;


class Transaction():

    def __init__(self, mempool):
        self.mempool = mempool

    def new_transaction(self, sender, recipient, amount):
        # Adds a new transaction to the mempool list of transactions
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.mempool.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return Blockchain.last_block['index'] + 1
