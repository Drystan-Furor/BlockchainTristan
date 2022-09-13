import hashlib
from blockchain import Block
class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.current_transactions = []
        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        # Simple Proof of Work Algorithm:
        """
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        # Validates the Proof:
        """
        Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # To adjust the difficulty of the algorithm, we could modify the number of leading zeroes. But 4 is sufficient.
        return guess_hash[:4] == "0000"

