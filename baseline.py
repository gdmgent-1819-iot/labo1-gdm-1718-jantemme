from sense_hat import SenseHat
import random

sense = SenseHat()

sense.clear()

sense.set_rotation(180)


def scrollingMsg(r, g, b, r2, g2, b2):
    sense.show_message("We are New Media Development!", text_colour=[r,g,b], back_colour=[r2,g2,b2])
    
def randNumb(endOfRange):
    return random.randint(0,endOfRange)
    
while("true"):
    scrollingMsg(randNumb(255), randNumb(255), randNumb(255), randNumb(100), randNumb(100), randNumb(100))