from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

sense.clear()

def randNumb(endOfRange):
    return random.randint(0,endOfRange)

## algoritme niet gevonden, hardcoden dan maar

a = (0,0,0)
b = (100,100,100)

rect1 = [
    b, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a
    ]

rect2 = [
    b, b, a, a, a, a, a, a,
    b, b, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a
    ]

rect3 = [
    b, b, b, a, a, a, a, a,
    b, a, b, a, a, a, a, a,
    b, b, b, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a
    ]

rect4 = [
    b, b, b, b, a, a, a, a,
    b, a, a, b, a, a, a, a,
    b, a, a, b, a, a, a, a,
    b, b, b, b, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a
    ]

rect5 = [
    b, b, b, b, b, a, a, a,
    b, a, a, a, b, a, a, a,
    b, a, a, a, b, a, a, a,
    b, a, a, a, b, a, a, a,
    b, b, b, b, b, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a
    ]

rect6 = [
    b, b, b, b, b, b, a, a,
    b, a, a, a, a, b, a, a,
    b, a, a, a, a, b, a, a,
    b, a, a, a, a, b, a, a,
    b, a, a, a, a, b, a, a,
    b, b, b, b, b, b, a, a,
    a, a, a, a, a, a, a, a,
    a, a, a, a, a, a, a, a
    ]

rect7 = [
    b, b, b, b, b, b, b, a,
    b, a, a, a, a, a, b, a,
    b, a, a, a, a, a, b, a,
    b, a, a, a, a, a, b, a,
    b, a, a, a, a, a, b, a,
    b, a, a, a, a, a, b, a,
    b, b, b, b, b, b, b, a,
    a, a, a, a, a, a, a, a
    ]

rect8 = [
    b, b, b, b, b, b, b, b,
    b, a, a, a, a, a, a, b,
    b, a, a, a, a, a, a, b,
    b, a, a, a, a, a, a, b,
    b, a, a, a, a, a, a, b,
    b, a, a, a, a, a, a, b,
    b, a, a, a, a, a, a, b,
    b, b, b, b, b, b, b, b
    ]

while(1):
    sense.set_pixels(rect1)
    sleep(0.1)
    sense.set_pixels(rect2)
    sleep(0.1)
    sense.set_pixels(rect3)
    sleep(0.1)
    sense.set_pixels(rect4)
    sleep(0.1)
    sense.set_pixels(rect5)
    sleep(0.1)
    sense.set_pixels(rect6)
    sleep(0.1)
    sense.set_pixels(rect7)
    sleep(0.1)
    sense.set_pixels(rect8)
    sleep(0.1)
    
    sense.set_pixels(rect7)
    sleep(0.1)
    sense.set_pixels(rect6)
    sleep(0.1)
    sense.set_pixels(rect5)
    sleep(0.1)
    sense.set_pixels(rect4)
    sleep(0.1)
    sense.set_pixels(rect3)
    sleep(0.1)
    sense.set_pixels(rect2)
    sleep(0.1)
    sense.set_pixels(rect1)
    sleep(0.1)