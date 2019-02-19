import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

redisClient = redis.Redis()
redisSub = redis.Redis()


#for n in range(5):
    #print('Something',n)
redisClient.publish("Service", "good")
time.sleep(1)

pubsub = redisSub.pubsub()
pubsub.subscribe("This is main")
for item in pubsub.listen():
    print('This is main',item['data'])