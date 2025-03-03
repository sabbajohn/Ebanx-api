from flask import Blueprint, request, jsonify
from .services import AccountService

bp = Blueprint('app', __name__)
account_service = AccountService()

@bp.route('/reset', methods=['POST'])
def reset():

    account_service.reset()
    return "OK", 200

@bp.route('/balance', methods=['GET'])
def get_balance():

    account_id = request.args.get('account_id')
    balance = account_service.get_balance(account_id)
    if balance is None:
        return jsonify(0), 404
    return jsonify(balance), 200

@bp.route('/event', methods=['POST'])
def handle_event():
    data = request.json
    event_type = data.get('type')
    destination = data.get('destination')
    origin = data.get('origin')
    amount = data.get('amount')

    if event_type == 'deposit':
        account = account_service.deposit(destination, amount)
        return jsonify(destination=account), 201

    if event_type == 'withdraw':
        account = account_service.withdraw(origin, amount)
        if account is None:
            return jsonify(0), 404
        return jsonify(origin=account), 201

    if event_type == 'transfer':
        accounts = account_service.transfer(origin, destination, amount)
        if accounts is None:
            return jsonify(0), 404
        return jsonify(origin=accounts['origin'], destination=accounts['destination']), 201

    return "", 400