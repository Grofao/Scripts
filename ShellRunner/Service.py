from flask import Flask
from flask import json
from flask import request
from Client import Client
from multiprocessing.pool import ThreadPool

app = Flask(__name__)

class CommandResult:
    def __int__(self, status_code, out_put):
        self.status_code = status_code
        self.out_put = out_put

@app('/command')
def send_command():
    json = request.json

    statusCode, output

def __runCommand__(command, hosts):
    pool = ThreadPool(processes=5)
    [hosts, lambda a, c: c.move(a.source, a.destination)]
    async_result = pool.apply_async(foo, ('world', 'foo'))
    return_val = async_result.get()

def sendCommand(command, host):
    client =  Client(json.host, json.urse, json.password )
    status, stdOut = client.command(command)
    return CommandResult(status, stdOut)




