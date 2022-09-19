from queue import Empty
from flask import Flask, request
from blockchain.blockchain import Blockchain
from uuid import uuid4
from flask import Flask



# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

def create_app(config: dict = None) -> Flask:
    # Instantiate the Node
    # app = Flask(__name__)
    # create
    app = Flask(__name__, instance_relative_config=True)
    
    # configure
    # ...

    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)

    # add blueprint
    from . import api
    app.register_blueprint(api.bp)

    @app.route('/healthz')
    def ping():
        return 'healthy'

    return app