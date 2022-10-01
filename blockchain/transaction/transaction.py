from flask import jsonify, request


class Transaction:

    def __init__(self):
        pass

    def new_transaction(self):
        values = request.get_json()

        # Check that the required fields are in the POST'ed data
        required = ['sender', 'recipient', 'amount']
        if not all(k in values for k in required):
            return 'Missing values', 400

        # Create a new Transaction
        index = Transaction().create_new_transaction(values['sender'], values['recipient'], values['amount'])

        # methode append to mempool

        response = {'message': f'Transaction will be added to Block {index}'}
        return jsonify(response), 201

    def create_new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.blockchain.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.blockchain.last_block['index'] + 1
