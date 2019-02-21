import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

redisClient = redis.Redis()
redisSub = redis.Redis()

release = input('Press the Release Button?: Y/N')
if release == 'Y':
    redisClient.publish("Button Pressed", "yes")

#for n in range(5):
    #print('Something',n)

pubsub = redisSub.pubsub()
pubsub.subscribe("This is main")

for item in pubsub.listen():
    #redisClient.publish("Con",'good connection')
    if item['data'] == b'main':
        print('Dispensing Pills right now')
        break