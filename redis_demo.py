__author__ = "xumeng"
__date__ = "2018/9/4 22:06"

import redis


r = redis.Redis(host='127.0.0.1', port=6379)
r.set("name", '66666')
print(r.get('name'))
r.mset(id='1', cd= '2')
print(r.mget('id', 'cd'))

