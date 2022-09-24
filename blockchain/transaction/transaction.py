import datetime;

from flask import jsonify, make_response


class Transaction():

    def __init__(self, mempool):
        self.mempool = mempool

    def transaction_create(self, request):
        send_acount_id = request['send_acount_id']
        amount = request['amount']
        recieve_acount_id = request['recieve_acount_id']

        if (type(send_acount_id) == int and type(amount) == int and type(recieve_acount_id) == int):
            transaction_information = {
                "send_acount_id": send_acount_id,
                "amount": amount,
                "recieve_acount_id": recieve_acount_id,
            }

            transaction_data = {
                "current_time_stamp": datetime.datetime.now(),
                "transaction_data": transaction_information
            }

            self.mempool.mempool_list.append(transaction_data)
            return self.mempool.list()

        else:
            return make_response(jsonify("Invalid input"), 400)
