import time
from hashlib import sha256

class Transaction:

    def __init__(self, coinbase='', timestamp=None) -> None:
        self.coinbase = coinbase or 0;
        self.timestamp = timestamp or int(time.time())
        self.hash = self.create_hash()
        
    def create_hash(self) -> str:
        return sha256(sha256('{}{}'.format(self.coinbase, self.timestamp).encode()).hexdigest().encode('utf8')).hexdigest()
    
    def to_dict(self) -> dict:
        return dict(coinbase=self.coinbase, timestamp=self.timestamp, hash=self.hash)