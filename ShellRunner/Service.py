from flask import Flask
from flask import json
from flask import request
from flask import Response
from Client import Client

app = Flask(__name__)

@app.route('/command')
def send_command():
    incomingRequest = request.json
    result = json.dumps(__runCommand__(incomingRequest['command'], incomingRequest['hosts']))
    return Response(result, status=200, mimetype='application/json')

def __runCommand__(command, hosts):
    what =  [execute_command(command, host) for host in hosts]
    return what


def execute_command(command, host):
    client =  Client(host['ip'], host['user'], host['password'] )
    status, stdOut = client.command(command)
    client.close()
    return {"status_code" : status, "standard_out" : stdOut }

