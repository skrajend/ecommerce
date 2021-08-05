from flask import Flask
import socket
import redis
import time
from redis.sentinel import Sentinel

app = Flask(__name__)

"""cache = redis.Redis(
    host='ecom-backend-redis.default.svc.cluster.local',
    port='6379',
    password='SVTvj7w2iP')"""

redis_sentinel = Sentinel([('ecom-backend-redis.default.svc.cluster.local', '26379')], password='SVTvj7w2iP',
                          sentinel_kwargs={"password": "SVTvj7w2iP"}, socket_timeout=0.1)
redis_master = redis_sentinel.master_for('mymaster', socket_timeout=0.1)


def get_hit_count():
    retries = 5
    while True:
        try:
            return redis_master.incr('hits')
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
