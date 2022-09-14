import time
from blockchain.block import Block
from blockchain.blockchain import Blockchain

def test_block():
    block = Block(1, 1662843237.224394, 0)
    blockchain = Blockchain()
    hash1 = blockchain.mineAsync(block)
    print(hash1)
    assert hash1.startswith('0' * Blockchain.difficulty)


 
    