import redis
import time
i = 1
receive = 0
redisClient = redis.Redis()
redisPublisher = redis.Redis()

pubsub1 = redisClient.pubsub()
pubsub1.subscribe("Service","MM","Con")

for item in pubsub1.listen():
    print(type(item['data']))
    # if item['data'] == b'mm':
    #     print("This is Motor Control", item['data'])
    #     break
    # if item['data'] == b'good':
    #     print("This is Service",item['data'])
    #     break
#print('1')

for i in range(2):
    redisPublisher.publish("This is main","main")
    time.sleep(0.5)

# for item in pubsub1.listen():
#     #print('2')
#     print(item)
#     #print('3')
#
# while receive == 0:
#     print('2')
#     for item in pubsub1.listen():
#         print('3')
#         if item['data'] == b'goodconnection':
#             print('receiving')
#             receive = 1
#             break
#         else:
#             redisPublisher.publish("This is main",'main')
#             time.sleep(1)


