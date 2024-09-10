import os
import unittest
import requests


# run tests with command python3.10 -m unittest health_check_test.py

class TestApp(unittest.TestCase):
    def setUp(self):
        port = os.getenv("PORT", 8081)
        base_path = os.getenv("PATH_BASE", "/integracao/kit-1")
        self.url = 'http://localhost:' + str(port) + str(base_path)

    def test_health_endpoint(self):
        path_health = os.getenv("HEALTH_CHECK", "health")
        response = requests.get(f'{self.url}/{path_health}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'OK')


if __name__ == '__main__':
    unittest.main()
