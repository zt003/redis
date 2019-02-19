import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

redisClient = redis.Redis()

for n in range(100):
    #print('Something',n)
    redisClient.publish("Service","good")
    time.sleep(1)
    redisClient.publish("Motor Movement", "motor")
    time.sleep(1)


