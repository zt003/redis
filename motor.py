import redis
import time
r = redis.Redis()

for n in range(5):
    #print('Something',n)
    r.publish("MM","mm")
    time.sleep(1)