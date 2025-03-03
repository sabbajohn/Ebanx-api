import unittest
from app import create_app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client.post('/reset')
    def tearDown(self):
        self.app_context.pop()

    def test_reset(self):
        response = self.client.post('/reset')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "OK")

    def test_get_balance_nonexistent_account(self):
        response = self.client.get('/balance?account_id=nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, 0)

    def test_deposit(self):
        response = self.client.post('/event', json={
            'type': 'deposit',
            'destination': 'account1',
            'amount': 100
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['destination']['balance'], 100)

    def test_withdraw(self):
        self.client.post('/event', json={
            'type': 'deposit',
            'destination': 'account1',
            'amount': 100
        })
        response = self.client.post('/event', json={
            'type': 'withdraw',
            'origin': 'account1',
            'amount': 50
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['origin']['balance'], 50)

    def test_transfer(self):
        self.client.post('/event', json={
            'type': 'deposit',
            'destination': 'account1',
            'amount': 100
        })
        response = self.client.post('/event', json={
            'type': 'transfer',
            'origin': 'account1',
            'destination': 'account2',
            'amount': 50
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['origin']['balance'], 50)
        self.assertEqual(response.json['destination']['balance'], 50)

    def test_withdraw_insufficient_funds(self):
        response = self.client.post('/event', json={
            'type': 'withdraw',
            'origin': 'account1',
            'amount': 50
        })
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, 0)

    def test_transfer_insufficient_funds(self):
        self.client.post('/event', json={
            'type': 'deposit',
            'destination': 'account2',
            'amount': 100
        })
        response = self.client.post('/event', json={
            'type': 'transfer',
            'origin': 'account1',
            'destination': 'account2',
            'amount': 50
        })
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, 0)

if __name__ == '__main__':
    unittest.main()