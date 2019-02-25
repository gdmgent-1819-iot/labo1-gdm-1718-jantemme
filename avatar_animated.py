from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

sense.clear()

def randNumb(endOfRange):
    return random.randint(0,endOfRange)

while(1):
    for y in range(0,8):
        for x in range(0,4):
            state = randNumb(1)
            
            if state == 0:
                sense.set_pixel(x, y, (0,0,0))
                sense.set_pixel((7-x), y, (0,0,0))
            
            if state == 1:
                sense.set_pixel(x, y, (100,100,100))
                sense.set_pixel((7-x), y, (100,100,100))
    sleep(2)
