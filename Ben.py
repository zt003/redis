import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

redisClient = redis.Redis()
redisSub = redis.Redis()
pubsub = redisSub.pubsub()
pubsub.subscribe("This is main")

reg_info = '2019 2 24 18 00' #Medication Regiments
reg_info2 = '2019 2 28 18 00'
print(reg_info)

redisClient.publish("wireless",reg_info)
for item in pubsub.listen():
    if type(item['data']) is not int:
        item = str(item['data'],'utf-8')
        if item == 'invalid':
            print(item)
            redisClient.publish("wireless",reg_info2)
        elif item == 'valid':
            print(item)
            break
