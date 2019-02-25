from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

sense.clear()

def randNumb(endOfRange):
    return random.randint(0,endOfRange)

while(1):
    a = 1
    for x in range(0,8):
        for y in range(0,a):
            a += 2
            sense.set_pixel(y, x, (100,100,100))
            sense.set_pixel(x, y, (100,100,100))
        sleep(0.2)
    sleep(2)