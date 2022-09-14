from hashlib import sha256
import hashlib
import json
import time

class Block(object):

    def __init__(self, index, timestamp, previous_hash, nonce=0) -> None:
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.chain = []
        self.timestamp = timestamp
        self.current_transactions = []
        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)
    
    def hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()


    #------------------------------------------------------------------------------

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        
        block = {
            'index': len(self.chain) + 1,
            'timestamp': self.timestamp,
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block
    #------------------------------------------------------------------------------
    
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    #------------------------------------------------------------------------------

    @staticmethod
    def hash(block):
        """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    #------------------------------------------------------------------------------
    @property
    def last_block(self):
        return self.chain[-1]
    
    #------------------------------------------------------------------------------
    #block = {
    #'index': 1,
    #'timestamp': 1506057125.900785,
    #'transactions': [
    #    {
    #        'sender': "8527147fe1f5426f9dd545de4b27ee00",
    #        'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
    #        'amount': 5,
    #    }
    #],
    #'proof': 324984774000,
    #'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    #}