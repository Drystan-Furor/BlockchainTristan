from queue import Empty
from blockchain.blockchain import Blockchain
from flask import Flask, request

# flask will automatically detect this function
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

    # Instantiate the Blockchain
    blockchain = Blockchain()
    blockchain.create_first_block()
    app.blockchain = blockchain
    # Generate a globally unique address for this node

    return app