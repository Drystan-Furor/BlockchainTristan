import requests
from ..blockchain.blockchain import blockchain
from ..blockchain.mempool import mempool

from flask import Flask, current_app
import json

class TestBlock:
    def create(self):
        app = Flask(__name__)
        with app.app_context():
            assert blockchain.Blockchain().create().status_code == 200

    def test_add_block(self):
        app = Flask(__name__)
        test_blockchain = [
            {
                "current_block_hash": "14acb6dac20a03cf611f0a12c7746721673fb61022bd7ff58f88692088ac9371",
                "data": "transaction",
                "index": 1,
                "previous_block_hash": "",
                "timestamp": "Thu, 15 Sep 2022 21:10:30 GMT"
            }
        ] 

        with app.app_context():
            test_mempool = mempool.Mempool()
            assert blockchain.Blockchain(test_blockchain).add_block(test_mempool).status_code == 200
            
    def test_add_block_to_empty_chain(self): 
        app = Flask(__name__)
        test_blockchain = [] 

        with app.app_context():
            test_mempool = mempool.Mempool()
            assert blockchain.Blockchain(test_blockchain).add_block(test_mempool).status_code == 200

    def test_index(self):
        assert type(blockchain.Blockchain().list()) == list

    def test_reset(self):
        app = Flask(__name__)
        with app.app_context():
            assert blockchain.Blockchain().reset().status_code == 200

    def test_create(self):
        app = Flask(__name__)
        with app.app_context():
            transaction_data = {
                "transaction_data": {
                    "amount": 50000,
                    "recieve_acount_id": 2,
                    "send_acount_id": 1
                }
            }
            assert type(blockchain.Blockchain().create(transaction_data)) == list

    def test_add_block(self):
        app = Flask(__name__)
        with app.app_context():
            transaction_data = {
                "transaction_data": {
                    "amount": 500000,
                    "recieve_acount_id": 2,
                    "send_acount_id": 1
                    }
                }        
            transaction_data_2 = {
                "transaction_data": {
                    "amount": 50000,
                    "recieve_acount_id": 2,
                    "send_acount_id": 1
                    }
                }                
            test_mempool = mempool.Mempool()
            test_mempool.add_new_transaction_to_mempool(transaction_data)
            test_mempool.add_new_transaction_to_mempool(transaction_data_2)

            test_blockchain = blockchain.Blockchain()
            test_blockchain.create(transaction_data)
            assert type(test_blockchain.add_block(test_mempool)) == list


    def test_add_block_empty_blockchain(self):
        app = Flask(__name__)
        with app.app_context():
            transaction_data = {
                "transaction_data": {
                    "amount": 50000,
                    "recieve_acount_id": 2,
                    "send_acount_id": 1
                    }
                }
                
            test_mempool = mempool.Mempool()
            test_mempool.add_new_transaction_to_mempool(transaction_data)
            assert type(blockchain.Blockchain().add_block(test_mempool)) == list