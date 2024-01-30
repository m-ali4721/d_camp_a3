import unittest
from flask import Flask
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        # Send a GET request to the '/' endpoint
        response = self.app.get('/')

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Assert that the response data contains the expected message
        self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()
