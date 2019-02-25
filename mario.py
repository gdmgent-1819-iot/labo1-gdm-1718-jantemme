from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

sense.clear()

a = (0, 0, 0)
b = (255, 0, 0)
c = (0, 0, 255)
d = (255, 222, 64)
e = (156, 65, 0)

def marioJumps():
    led1 = [
        a, a, a, d, d, d, a, a,
        a, a, a, d, d, d, d, a,
        a, a, a, b, b, a, b, a,
        a, b, b, c, c, b, a, a,
        d, a, a, c, c, a, e, a,
        a, e, c, a, a, c, e, a,
        a, e, a, a, a, a, a, a,
        a, a, a, a, a, a, a, a
        ]
    sense.set_pixels(led1)

def marioStands():
    led1 = [
        a, a, a, b, b, b, b, a,
        a, a, a, d, d, d, a, a,
        a, a, a, d, d, d, a, a,
        a, a, a, b, b, a, a, a,
        a, b, b, c, c, b, b, a,
        d, a, a, c, c, a, a, d,
        a, a, c, a, a, c, a, a,
        a, a, e, e, a, e, e, a
        ]
    sense.set_pixels(led1)

while(1):
    marioStands()
    event = sense.stick.wait_for_event()
    marioJumps()
    sleep(0.2)

