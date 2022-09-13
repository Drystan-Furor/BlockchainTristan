from flask import Flask, request, jsonify

app = Flask(__name__) # 1


@app.route('/') # 2

def hello():

    number = request.args.get("number")

    if number == '+3155512345':

        return jsonify({'exists': True})

    else:

        return jsonify({'exists': False}) # 3



app.run(port=8080)
