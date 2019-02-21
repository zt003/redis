import redis

class Motor():
    def __init__(self,name,speed,distance):
        self.speed = speed
        self.distance = distance
        self.sensor = 0
        self.name = name
    def Forward(self):
        print(self.name,"Going forward with speed",str(self.speed),"for distance",str(self.distance))

    def Backward(self):
        print(self.name,"Going backward with speed",str(self.speed),"for distance",str(self.distance))

    def Sensor(self):
        return self.sensor