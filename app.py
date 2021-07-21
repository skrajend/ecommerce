from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname=socket.gethostname()
    message="Hello World from " + hostname
    return message