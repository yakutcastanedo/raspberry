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
             2: 'blue',
             3: "yellow",
             4: 'purple',
             5: 'cyan'
             }

x = 10

userChoise = int(
     raw_input("Please choose a number\
     (red = 0, green = 1, blue = 2, yellow = 3, purple = 4, cyan = 5 ): "))
print userChoise


def clean():
    GPIO.output(red, True)
    GPIO.output(green, True)
    GPIO.output(blue, True)

def blink(a):
    if a == 0:
        print "blinking red"
        clean()
        while True:
            GPIO.output(red, False)
            sleep(0.4)
            GPIO.output(red, True)
            sleep(0.4)

    elif a == 1:
        print "blinking green"
        clean()
        while True:
            GPIO.output(green, False)
            sleep(0.4)
            GPIO.output(green, True)
            sleep(0.4)

    elif a == 2:
        print "blinking blue"
        clean()
        while True:
            GPIO.output(blue, False)
            sleep(0.4)
            GPIO.output(blue, True)
            sleep(0.4)

    elif a == 3:
        print "blinking yellow"
        clean()
        while True:
            GPIO.output(red, False)
            GPIO.output(green, False)
            sleep(0.4)
            GPIO.output(red, True)
            GPIO.output(green, True)
            sleep(0.4)

    elif a == 4:
        print "blinking purple"
        clean()
        while True:
            GPIO.output(red, False)
            GPIO.output(blue, False)
            sleep(0.4)
            GPIO.output(red, True)
            GPIO.output(blue, True)
            sleep(0.4)

    elif a == 5:
        print "blinking cyan"
        clean()
        while True:
            GPIO.output(blue, False)
            GPIO.output(green, False)
            sleep(0.4)
            GPIO.output(blue, True)
            GPIO.output(green, True)
            sleep(0.4)


blink(userChoise)

