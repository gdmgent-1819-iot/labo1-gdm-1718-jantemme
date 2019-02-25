from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

sense.clear()

def randNumb(endOfRange):
    return random.randint(0,endOfRange)

while(1):
    for y in range(0,8):
        for x in range(0,8):
            sense.set_pixel(x, y, (randNumb(255),randNumb(255),randNumb(255)))
            sleep(0.1)
            sense.clear()
    sleep(1)
        
        