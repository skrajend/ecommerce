from flask import Flask
import socket
import redis

app = Flask(__name__)

redis = redis.Redis(
    host='my-release-redis',
    port='6379',
    password='SVTvj7w2iP')

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    message = "Welcome to E-Commerce Application. Pod Name  : " + hostname
    redis.set('pod', hostname)
    return message
