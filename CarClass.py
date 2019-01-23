import random

class Car:
    def __init__(self, color, model, make, topSpeed, isStarted=False, speed=0):
        self.color = color
        self.model = model
        self.make = make
        self.topSpeed = topSpeed
        self.isStarted = isStarted
        self.speed = speed

    def start(self):
        if self.isStarted == False:
            self.isStarted = True
            print('{} {} {} colored is starting...'.format(self.make, self.model, self.color))
        else:
            print('{} {} {} colored is already started...'.format(self.make, self.model, self.color))

    def turn_off(self):
        if self.isStarted == True:
            self.isStarted = False
            print('{} {} {} colored is turning off...'.format(self.make, self.model, self.color))
        else:
            print('{} {} {} colored is already off...'.format(self.make, self.model, self.color))

    def accelerate(self):
        if self.isStarted == True:
            if self.speed == self.topSpeed:
                print('{} {} {} colored is at its maximum speed...'.format(self.make, self.model, self.color))
            else:
                self.speed += 1
                print('{} {} {} colored is moving forward with speed {}...'.format(self.make, self.model, self.color, self.speed))
        else:
            print('{} {} {} colored is need to start first...'.format(self.make, self.model, self.color))

    def apply_breaks(self):
        if self.speed == 0:
            print('{} {} {} colored is stopped / turned off...'.format(self.make, self.model, self.color))
        else:
            self.speed -= 1
            print('{} {} {} colored slowed down with speed {}...'.format(self.make, self.model, self.color, self.speed))


swift = Car('Gray', 'Swift', 'Maruri-Suzuki', 180)
i10 = Car('Red', 'i10', 'Hyundai', 180)

'''
swift.start()
swift.accelerate()

print(swift.speed)


while True:
    swift.accelerate()
    if swift.speed == 180:
        break

swift.accelerate()

print(swift.speed)


while True:
    swift.apply_breaks()
    if swift.speed == 0:
        break

swift.apply_breaks()

print(swift.speed)
'''

swift.start()
while True:
    num = random.randint(0, 10)
    # print(num)
    if num == 0:
        swift.turn_off()
        break
    elif num >= 1 and num <= 7:
        swift.accelerate()
    else:
        swift.apply_breaks()


