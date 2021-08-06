"""from redis.sentinel import Sentinel

#sentinel = Sentinel([('ecom-backend-redis.default.svc.cluster.local', '26379')], password='EfZCuJvBg5', socket_timeout=0.1, sentinel_kwargs={"password": "EfZCuJvBg5"})
#redis_master = sentinel.discover_master('mymaster')
#redis_master = sentinel.master_for('mymaster', password='EfZCuJvBg5', socket_timeout=0.1)
#redis_master.set('test', '1')
#r = sentinel.discover_master('mymaster(master)')

sentinel = Sentinel([('localhost', '26379')], password='GTO3wsfIU4', socket_timeout=0.1, sentinel_kwargs={"password": "GTO3wsfIU4"})
redis_master = sentinel.master_for('mymaster', password='GTO3wsfIU4', socket_timeout=0.1)
#redis_master.set('test', '1')
print(sentinel)
print(redis_master)
"""

"""cache = redis.Redis(
    host='ecom-backend-redis.default.svc.cluster.local',
    port='6379',
    password='Kk5ue0Fx8B')

redis_sentinel = Sentinel([('ecom-backend-redis.default.svc.cluster.local', '26379')], password='EfZCuJvBg5')
redis_master = redis_sentinel.master_for('mymaster')"""

import redis
from redis.sentinel import Sentinel
sentinel = Sentinel([('localhost', 26379)],
                   sentinel_kwargs={'password': 'XnYewjhdcS'})
#redis_client = sentinel.master_for('mymaster', password='XnYewjhdcS')
host, port = sentinel.discover_master('mymaster')

redis_client = redis.StrictRedis(
            host='localhost',
            port=port,
            password= 'XnYewjhdcS'
        )

print(sentinel)
print(host)
print(port)
redis_client.incr('counter', 1)
c=redis_client.get('counter')
print(c)