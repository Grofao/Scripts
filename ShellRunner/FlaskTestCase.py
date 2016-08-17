import os
import unittest
import tempfile
import Service
from flask import json


class Host:
    def __init__(self, ip, user, password):
        self.ip = ip
        self.user = user
        self.password = password

class RequestCommand:
    def __init__(self, command, hosts):
        self.command = command
        self.hosts = hosts



class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        Service.app.config['TESTING'] = True
        self.app = Service.app.test_client()

    def tearDown(self):
        pass

    def create_request(self, command, ip, user, password):
        return {
            "command" : [command],
            "hosts" : [{"ip" : ip, "user" : user, "password" : password}]
        }

    def test_sending_single_command(self):
        test_request =  self.create_request("echo 'hello'","10.44.19.45", "richard", "password")
        rv = self.app.get('/command', data=json.dumps(test_request), content_type = 'application/json')
        assert 200 == rv._status_code
        json_response = json.loads(rv.data)
        assert "hello\n" == json_response[0]['standard_out'][0]
        assert 0 == json_response[0]['status_code']



if __name__ == '__main__':
    unittest.main()

