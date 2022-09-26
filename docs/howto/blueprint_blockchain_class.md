```
{
from flask import jsonify, make_response
from ..block.block import Block
import json


class Blockchain:
    def __init__(self, blockchain=[]):
        #constructor van de class om te initieren

    def create(self, transaction_data):
        # creëren van een Genesis Block
        pass

    def add_block(self, mempool):
        # toevoegen van een block
        pass

    def list(self):
        # lijst van alle blokken
        pass

    def reset(self):
        # reset de blockchain
        pass

    def get_highest_transaction(self, transaction_list):
        # zoek transactie met hoogste waarde
        pass

}
```

> Onze Blockchain class is verantwoordelijk voor het managen van de chain.
Het bevat onder andere methodes om een block te generen en aan de lijst toe te voegen.