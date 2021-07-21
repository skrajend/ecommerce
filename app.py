from flask import Flask
import socket
app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname=socket.gethostname()
    message="Hello World. Pod Name : " + hostname
    return message