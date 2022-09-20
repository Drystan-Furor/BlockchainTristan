import time
from blockchain.block import Block
from blockchain.transaction import Transaction
from hashlib import sha256
from merkletools import MerkleTools

def test_block_with_no_tx():
    block = Block(1, [], 0, 1662843237.224394, 0)
    assert block.index == 1
    assert len(block.txs) == 0
    assert block.timestamp == 1662843237.224394
    assert block.previous_hash == 0
    assert block.nonce == 0

def test_create_hash_with_no_tx():
    block = Block(1, [], 0, 1662843237.224394, 0)
    
    assert not len(block.txs)
    assert block.create_hash() == '5958b1b47b8ca2aae7276c9d8c3a2243b0ec98a630493088c2d4389269f4aba2'

def test_create_hash_with_tx():
    txs = []
    txs.append(Transaction('first', 1))
    txs.append(Transaction('second', 2))
    block = Block(1, txs, 0, 1662843237.224394, 0)
    
    assert len(block.txs)
    assert block.create_hash()

def test_create_merkle_root():
    txs = []
    txs.append(Transaction('first', 1))
    txs.append(Transaction('second', 2))
    block = Block(1, txs, 0, 1662843237.224394, 0)
    block.create_hash()

    mt = MerkleTools(hash_type="SHA256")

    for tx in txs: 
        mt.add_leaf(tx.hash) 
           
    mt.make_tree()
        
    assert mt.get_merkle_root() == block.merkle_root
