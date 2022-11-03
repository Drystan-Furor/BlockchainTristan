
import hashlib
import time
from ..blockchain.types import TransactionData, TransActionOutput
from typing import Tuple, Any

# mypy: ignore-errors
from ecdsa import SigningKey, NIST521p

import requests
import json

class Client:
    def __init__(self) -> None:
        self.transaction:TransactionData | None         = None
        self.balance:int | None                         = None
        self.priorTransaction:TransActionOutput | None  = None

        #would normally be generated or retrieved from storage, but we have no storage or registration system
        self.userID         = 672
        self.privateKey     = SigningKey.generate(curve=NIST521p)
        self.publicKey      = self.privateKey.get_verifying_key().to_string()

        self.urls = {
            "base":         "localhost:8080/api/",
            "balance":      "balance",
            "remainder":    "openRemainder",
            "transaction":  "transaction/new"
        }

    def __str__(self) -> str:
        return f"timestamp:{self.pseudoTransaction['timestamp']},senderID:{self.pseudoTransaction['senderID']},receiverID:{self.pseudoTransaction['receiverID']},amount:{self.pseudoTransaction['amount']}"

    def newTransaction(self) -> None:
        self.getPriorTransaction()

        #Ideally we'd actually receive input but there is no FE to receive input from
        transaction:TransactionData = {
            "timestamp":            time.time(),
            "senderID":             self.userID,
            "receiverID":           12,
            "amount":               77.4,
            "publicKey":            self.publicKey,
            "signature":            "",
            "inputHash":            "AlphaTransaction",
            "transaction_output":    self.priorTransaction
        }

        if transaction["amount"] > self.balance:
            print("You cannot spend more than you have... sadly")
            return

        hashstr = hashlib.sha256(bytes(self.__str__(), 'utf-8')).hexdigest()

        self.transaction["signature"] = self.privateKey.sign(hashstr)


    def requestTransaction(self) -> None:
        self.newTransaction()

        result = self.makeRequest(self.makeURL(self.urls["transaction"]), body=json.dumps(self.transaction))

        if not result[1] == 200:
            print(f"Could not make transaction :{result[0]}")
            return

        self.getBalance()
        print("transaction succesful")


    def getBalance(self) -> None:
        body = {
            "user_id": self.userID
        }
        result = self.makeRequest(self.makeURL(self.urls["balance"]), body=json.dumps(body))

        if not result[1] == 200:
            print(f"kaput :{result[0]}")

        self.balance = json.loads(result[0])["balance"]


    def getPriorTransaction(self) -> None:
        body = {
            "user_id": self.userID
        }
        result = self.makeRequest(self.makeURL(self.urls["remainder"]), body=json.dumps(body))

        if not result[1] == 200:
            print(f"kaput :{result[0]}")

        self.priorTransaction = json.loads(result[0])


    def makeRequest(self, url:str, method:str = "get", body:str | None = None) -> Tuple[Any, int]:
        try:
            response = requests.request(method, url, data=body)
            return (json.loads(response.text), response.status_code)
        except:
            return ("Could not make request :c", 0)


    def makeURL(self, endpoint:str) -> str:
        return self.urls["base"]+endpoint