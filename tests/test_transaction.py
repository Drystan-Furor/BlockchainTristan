from blockchain.transaction import Transaction

def test_transaction():

    tx = Transaction('first')

    assert tx.coinbase == 'first'
    assert tx.timestamp
    assert len(tx.hash)
