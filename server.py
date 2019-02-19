import redis

redisClient = redis.Redis()

pubsub1 = redisClient.pubsub()
pubsub1.subscribe("Service","MM")

for item in pubsub1.listen():
    if item['channel'] == b'MM':
        print("This is Motor Control", item['data'])
    if item['channel'] == b'Service':
        print("This is Service",item['data'])
#client_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
#client_r = redis.Redis(connection_pool=client_pool)
# client_r = redis.Redis()
# client_p = client_r.pubsub()
# client_p.subscribe(["Service"])

# motor_pool = redis.ConnectionPool(host='localhost', port=5555, db=0)
# motor_r = redis.Redis(connection_pool=motor_pool)
# motor_p = motor_r.pubsub()
# motor_p.subscribe(["Motor Movement"])

#
# for item in client_p.listen():
#     print('listening')
#     print(item['data'])
# for item in motor_p.listen():
#     print(item['data'])