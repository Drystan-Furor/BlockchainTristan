import hashlib

class ValidateProof():

    @staticmethod
    def valid_proof(last_proof, proof, timestamp):
        guess = f'{last_proof}{proof}{timestamp}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000" 