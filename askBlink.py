# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

# GPIO number where the led is connected
red = 10
green = 22
blue = 27
# Tell the GPIO module to use GPIO numbering used by processor
GPIO.setmode(GPIO.BCM)

# Set GPIO no 10 to output mode
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

# Blink some leds"

colorList = {0: 'red',
             1: 'green',
             2: 'blue'}

userChoise = int(raw_input("Please choose a number (red = 0, green = 1, blue = 2): "))
print userChoise


def blink(a):
    if a == 0:
        GPIO.setup(red, GPIO.OUT)
        return "blinking red"
    elif a == 1:
        GPIO.setup(green, GPIO.OUT)
        return "blinking green"
    elif a == 2:
        GPIO.setup(blue, GPIO.OUT)
        return "blinking blue"

blink(userChoise)
