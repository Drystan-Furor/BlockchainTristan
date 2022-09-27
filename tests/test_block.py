from ..blockchain.block import block
from ..blockchain.blockchain import blockchain


class TestBlock:
    def test_generate_block(self):
        test_blockchain = [
            {
                "current_block_hash": "ee7de4f21aca73a82fddd86f8b3163c2d24b7ee6b45388cc8fe2b1b0659ed9bb",
                "data": {
                    "current_time_stamp": "Sun, 18 Sep 2022 20:19:50 GMT",
                    "transaction_data": {
                        "amount": 50000,
                        "recieve_acount_id": 2,
                        "send_acount_id": 1
                        }
                    },
                    "index": 1,
                    "previous_block_hash": "",
                    "proof": 1342,
                    "timestamp": "Sun, 18 Sep 2022 20:19:53 GMT"
                    }
                    ]
        assert type(block.Block(1, "transaction").new_block(test_blockchain)) == dict

    def test_generate_block_empty_chain(self):
        
        assert type(block.Block(1, "transaction").new_block([])) == dict

