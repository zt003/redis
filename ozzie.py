import redis
import time
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.Redis(connection_pool=pool)

redisClient = redis.Redis()
redisSub = redis.Redis()
pubsub = redisSub.pubsub()
pubsub.subscribe("This is main")
press = 0

while True:
    release = input('Press the Release Button?: Y/N')
    if release == 'Y':
        redisClient.publish("Interface", "Release-yes")
        press = 1
    elif release == 'N':
        redisClient.publish("Interface", "Release-no")

    if press == 0:
        ad = input('Do user adhere to the medication?: Y/N')
        if ad == 'Y':
            redisClient.publish("Interface", "Nonad-no")
        elif ad == 'N':
            redisClient.publish("Interface", "Nonad-yes")

    #for n in range(5):
        #print('Something',n)


    for item in pubsub.listen():
        #redisClient.publish("Con",'good connection')
        if item['data'] == b'Medrun':
            print('Dispensing Pills right now')
            press = 0
            break
        elif item['data'] == b'Nonad-run':
            print('Pills stored in Non-adherence space')
            press = 0
            break

