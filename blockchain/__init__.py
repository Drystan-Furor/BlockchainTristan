from queue import Empty
from flask import Flask, request

def create_app(config: dict = None) -> Flask:

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

#_blockchain/Scripts/Activate 