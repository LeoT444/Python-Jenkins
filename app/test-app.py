import unittest
from app import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
   
    def test_status(self):
        response = self.app.get('/api/status')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'ok')
   
    def test_hello(self):
        response = self.app.get('/api/hello/Mundo')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()