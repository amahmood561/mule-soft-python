# tests/test_api.py
import unittest
from api.routes import app

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_transform(self):
        response = self.app.post('/transform', json={"key": "value"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"key": "VALUE"})

if __name__ == '__main__':
    unittest.main()
