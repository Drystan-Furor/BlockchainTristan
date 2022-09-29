
from blockchain.blockchain.blockchain import Blockchain


class Transaction:

    def __init__(self):
        self.blockchain = Blockchain()

    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.blockchain.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.blockchain.last_block['index'] + 1
