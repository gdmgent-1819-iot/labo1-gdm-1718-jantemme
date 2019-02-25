from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()

sense.clear()

sense.set_rotation(180)

def randNumb(endOfRange):
    return random.randint(0,endOfRange)

studyAbbriviation = "NMD"

inputtedString = input("What do you want to see? => ")
inputtedSpeed = float(input("How fast do you want it? (in seconds) => "))

while(1):
    for letter in inputtedString:
        sense.show_letter(letter, (randNumb(255), randNumb(255), randNumb(255)))
        sleep(inputtedSpeed)

    sleep(inputtedSpeed * 2)



