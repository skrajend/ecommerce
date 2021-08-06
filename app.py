from flask import Flask
import socket
import redis
import time
from redis.sentinel import Sentinel

app = Flask(__name__)

sentinel = Sentinel([('ecom-backend-redis.default.svc.cluster.local', 26379)],
                    sentinel_kwargs={'password': 'svuFY5fGYV'})
host, port = sentinel.discover_master('mymaster')
redis_client = redis.StrictRedis(
    host=host,
    port=port,
    password='svuFY5fGYV'
)


def get_hit_count():
    retries = 5
    while True:
        try:
            return redis_client.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    count = get_hit_count()
    message = "Welcome to E-Commerce Application. Pod Name  : " + hostname
    message = message + "You've visited me {} times.\n".format(count)
    return message
