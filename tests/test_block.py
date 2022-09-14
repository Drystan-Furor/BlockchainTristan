import time
from blockchain.block import Block

def test_block():
    block = Block(1, 1662843237.224394, 0, 1)
    assert block.index == 1
    assert block.timestamp == 1662843237.224394
    assert block.previous_hash == 0
    assert block.nonce == 1
    assert block.hash() == '34d8198e11fe26828c75cd2d3ffee472a68fb2d783eaf664f74f4adac34cb63e'
    