from ..blockchain.mempool import mempool
from flask import Flask, current_app
from ..blockchain.blockchain import blockchain


class TestMempool():

    def test_index(self):
        app = Flask(__name__)
        with app.app_context():
            assert mempool.Mempool().index().status_code == 200
    
    def test_add_new_transaction_to_mempool(self):
        app = Flask(__name__)
        with app.app_context():
            transaction_data = {
                "send_acount_id" : 1,
                "amount" : 5000,
                "recieve_acount_id" : 2
            } 
            assert mempool.Mempool().add_new_transaction_to_mempool(transaction_data).status_code == 200



