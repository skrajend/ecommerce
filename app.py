from flask import Flask
import socket
import redis
import time

app = Flask(__name__)

cache = redis.Redis(
    host='10.2.29.198',
    port='6379',
    password='SVTvj7w2iP')


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    count = get_hit_count()
    message = "Welcome to E-Commerce Application. Pod Name  : " + hostname + "You've visited me {} times.\n".format(
        count)
    return message
