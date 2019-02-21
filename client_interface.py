import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

redisClient = redis.Redis()
redisSub = redis.Redis()
reg_info = {'2019 2 21 0':'00', '2019 2 20 19':'00'}

#for n in range(5):
    #print('Something',n)
redisClient.publish("Service", reg_info)

pubsub = redisSub.pubsub()
pubsub.subscribe("This is main")
for item in pubsub.listen():
    #redisClient.publish("Con",'good connection')
    if item['data'] == b'main':
        print('This is main',item['data'])
        redisClient.publish("Con","goodconnection")
        break