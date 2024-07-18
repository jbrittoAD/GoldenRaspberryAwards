import unittest
from app import create_app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_interval(self):
        response = self.client.get('/producers')
        self.assertEqual(response.status_code, 200)
        # Adicione mais asserções conforme necessário

if __name__ == '__main__':
    unittest.main()
