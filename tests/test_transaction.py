from ..blockchain.transaction import transaction
from ..blockchain.mempool import mempool

from flask import Flask, current_app

class TestTransaction():

    def test_transaction_create_valid_data(self):
        app = Flask(__name__)
        with app.app_context():
            transaction_data = {
                "send_acount_id" : 1,
                "amount" : 5000,
                "recieve_acount_id" : 2
            }
            fake_mempool = mempool.Mempool()
            assert transaction.Transaction(fake_mempool).transaction_create(transaction_data).status_code == 200
         
    def test_transaction_create_invalid_data(self):
        app = Flask(__name__)
        with app.app_context():
            transaction_data = {
                "send_acount_id" : "test",
                "amount" : "test",
                "recieve_acount_id" : "test"
            }
            fake_mempool = mempool.Mempool()
            assert transaction.Transaction(fake_mempool).transaction_create(transaction_data).status_code == 400
    
           