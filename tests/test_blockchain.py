import time
from blockchain.block import Block
from blockchain.blockchain import Blockchain

def test_mine_async():
    block = Block(1, [], 0, 1662843237.000001, 0)
    blockchain = Blockchain()
    nonce, hash = blockchain.mine(block)
    
    assert nonce > 0
    assert hash.startswith('0' * Blockchain.difficulty)

def test_add_block():
    blockchain = Blockchain()
    first_block = blockchain.create_first_block()
    
    assert len(first_block.hash) > 0
    assert first_block.index == 0
    assert len(blockchain.chain) == 1
    
    block = Block(len(blockchain.chain) + 1, [], blockchain.last_block.hash, 1662843238.000002, 0)
    block.nonce, proof = blockchain.mine(block)
    
    blockchain.add_block(block, proof)
    
    assert len(blockchain.chain) == 2

def test_validate_chain():
    blockchain = Blockchain()
    blockchain.create_first_block()

    block = Block(len(blockchain.chain) + 1, [], blockchain.last_block.hash, 1662843238.000002, 0)
    block.nonce, proof = blockchain.mine(block)
    blockchain.add_block(block, proof)

    block = Block(len(blockchain.chain) + 1, [], blockchain.last_block.hash, 1662843238.000003, 0)
    block.nonce, proof = blockchain.mine(block)
    blockchain.add_block(block, proof)

    assert blockchain.validate_chain()

    # manipulate block by changing the previous hash:
    block = Block(len(blockchain.chain) + 1, [], blockchain.chain[1].hash, 1662843239.000004, 0)
    block.nonce, proof = blockchain.mine(block)
    blockchain.add_block(block, proof)

    # should still be valid
    assert blockchain.validate_chain()