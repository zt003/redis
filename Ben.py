import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

redisClient = redis.Redis()
redisSub = redis.Redis()

reg_info = {'2019 2 21 0':'00', '2019 2 20 19':'00'} #Medication Regiments
print(reg_info)

redisClient.publish("wireless",reg_info)
time.sleep(1)

