import functools

from flask import (
    Blueprint, jsonify
)



bp = Blueprint('api', __name__, url_prefix='/api/v1')

@bp.route('/blocks', methods=['GET'])
def get_blocks():
    response = {'test': 'test'}
    return jsonify(response), 200

@bp.route('/block/add', methods=['POST'])
def add_block():
    pass

@bp.route('/transaction/create', methods=['POST'])
def create_transaction():
    pass

@bp.route('/transactions', methods=['GET'])
def get_transactions():
    response = {'test': 'test'}
    return jsonify(response), 200

@bp.route('/node/create', methods=['POST'])
def create_node():
    pass

@bp.route('/node/register', methods=['POST'])
def register_node():
    pass

