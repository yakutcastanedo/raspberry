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

# Blink some leds

while userChoise != red or green or blue:
	userChoise = raw_input("Please enter color (red, green, blue): ")

def blink(a):
	if a = red:
		GPIO.output(red)
	else if a = green:
		GPIO.output(green)
	else if a = blue:
		GPIO.output(blue)

blink(userChoise)

GPIO.setwarnings(False)