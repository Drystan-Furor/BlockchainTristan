from __future__ import annotations

import hashlib
import time
from ..blockchain.types import TransactionContent, UtxoOutput
from typing import Tuple, Any

from ecdsa import SigningKey, NIST521p

import requests
import json


# mypy: ignore-errors
def make_request(url: str, method: str = "get", body: str | None = None) -> Tuple[Any, int]:
    """
    request builder
    :param url: str
    :param method: get
    :param body: str
    :return: json response
    """
    try:
        response = requests.request(method, url, data=body)
        return json.loads(response.text), response.status_code
    except:
        return "make request could not", 0


class Client:
    def __init__(self) -> None:
        """
        Transaction data for the first transaction. IF we had a storage this would be there.
        Right now we work around it and generate it here until we get a storage or registration
        """
        self.transaction: TransactionContent | None = None
        self.balance: int | None = None
        self.previous_transaction: UtxoOutput | None = None

        # this part would normally be generated or retrieved from storage
        self.userID = 672
        self.privateKey = SigningKey.generate(curve=NIST521p)
        self.publicKey = self.privateKey.get_verifying_key().to_string()

        self.urls = {
            "base": "localhost:8080/api/",
            "balance": "balance",
            "remainder": "openRemainder",
            "transaction": "transaction/new"
        }

    def __str__(self) -> str:
        return f"timestamp:{self.transaction['timestamp']}," \
               f"senderID:{self.transaction['senderID']}," \
               f"receiverID:{self.transaction['receiverID']}," \
               f"amount:{self.transaction['amount']}"

    def make_url(self, endpoint: str) -> str:
        """
        build the base url
        :param endpoint: final route
        :return: route
        """
        return self.urls["base"] + endpoint

    def new_transaction(self) -> None:
        """
        a new transaction
        :return:
        """
        self.get_previous_transaction()

        # Ideally we'd actually receive input but there is no FE to receive input from
        transaction: TransactionContent = {
            "timestamp": time.time(),
            "senderID": self.userID,
            "receiverID": 12,
            "amount": 77.4,
            "publicKey": self.publicKey,
            "signature": "",
            "inputHash": "AlphaTransaction",
            "transaction_output": self.previous_transaction
        }

        if transaction["amount"] > self.balance:
            print("You cannot spend more than you have... sadly")
            return

        hashstr = hashlib.sha256(bytes(self.__str__(), 'utf-8')).hexdigest()

        self.transaction["signature"] = self.privateKey.sign(hashstr)

    def request_transaction(self) -> None:
        """
        Instantiate a transaction
        :return: new balance or
        """
        self.new_transaction()
        result = make_request(self.make_url(self.urls["transaction"]), body=json.dumps(self.transaction))

        if not result[1] == 200:
            return print(f"new transaction creation unsuccessful :{result[0]}")
        print("transaction successful")
        self.get_balance()

    def get_balance(self) -> None:
        """
        get current balance0
        :return: json result
        """
        body = {
            "user_id": self.userID
        }
        result = make_request(self.make_url(self.urls["balance"]), body=json.dumps(body))

        if not result[1] == 200:
            print(f"kaput :{result[0]}")

        self.balance = json.loads(result[0])["balance"]

    def get_previous_transaction(self) -> None:
        """
        get the data of the last transaction
        :return: type 'tuple[UtxoOutput, UtxoOutput] | None'
        """
        body = {
            "user_id": self.userID
        }
        result = make_request(self.make_url(self.urls["remainder"]), body=json.dumps(body))

        if not result[1] == 200:
            print(f"kaput :{result[0]}")

        self.previous_transaction = json.loads(result[0])
