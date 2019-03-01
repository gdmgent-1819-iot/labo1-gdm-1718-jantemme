from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear()

b = (100,100,100)

while(1):
    for x in range (0,8):
        for z in range (x):
            sense.set_pixel(z, 0, b)
            sense.set_pixel(z, x - 1, b)
        for y in range (x):
            sense.set_pixel(0, y, b)
            sense.set_pixel(x-1, y, b)
        sleep(0.1)
        sense.clear()
    
    for x in range (8, 0, -1):
        for z in range (x):
            sense.set_pixel(z, 0, b)
            sense.set_pixel(z, x - 1, b)
        for y in range (x):
            sense.set_pixel(0, y, b)
            sense.set_pixel(x-1, y, b)
        sleep(0.1)
        sense.clear()