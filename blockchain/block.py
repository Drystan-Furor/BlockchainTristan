from hashlib import sha256
from merkletools import MerkleTools
import json
import string
import time

class Block:
    def __init__(self, index:int, txs:list, previous_hash:str, timestamp=None, nonce=0) -> None:
        self.index = index
        self.txs = txs or []
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.timestamp = timestamp or int(time.time())
        self.merkle_root = None
        self.merkle_root = self.create_merkle_root()
    
    def create_hash(self) -> str:
        block_string = '{}{}{}{}{}'.format(
            self.index, self.previous_hash, self.timestamp, self.nonce, self.merkle_root 
        )
        return sha256(block_string.encode()).hexdigest()
    
    def create_merkle_root(self) -> str:
        if self.merkle_root is not None:
            return self.merkle_root

        mt = MerkleTools(hash_type="SHA256")

        for tx in self.txs:
            mt.add_leaf(tx.hash)
        
        mt.make_tree()
        
        self.merkle_root = mt.get_merkle_root()
        
        return self.merkle_root
    
    def to_dict(self) -> dict:
        return dict(index=self.index, txs=[tx.to_dict() for tx in self.txs], previous_hash=self.previous_hash, timestamp=self.timestamp, nonce=self.nonce, merkle_root=self.merkle_root)
        