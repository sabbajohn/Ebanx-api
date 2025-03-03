accounts = {}

class AccountService:
    def reset(self):
        global accounts
        accounts = {}

    def get_balance(self, account_id):
        if account_id not in accounts:
            return None
        return accounts[account_id]['balance']

    def create_account(self, account_id):
        if account_id not in accounts:
            accounts[account_id] = {'id': account_id, 'balance': 0}

    def deposit(self, destination, amount):
        self.create_account(destination)
        accounts[destination]['balance'] += amount
        return accounts[destination]

    def withdraw(self, origin, amount):
        if origin not in accounts or accounts[origin]['balance'] < amount:
            return None
        accounts[origin]['balance'] -= amount
        return accounts[origin]

    def transfer(self, origin, destination, amount):
        if origin not in accounts or accounts[origin]['balance'] < amount:
            return None
        self.create_account(destination)
        accounts[origin]['balance'] -= amount
        accounts[destination]['balance'] += amount
        return {
            'origin': accounts[origin],
            'destination': accounts[destination]
        }