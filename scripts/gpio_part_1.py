# Turn the light on and off using a script
# This only works on the pi as the GPIO package
# does not compile on a Mac/Windows machine (i think...)

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin = 36

# Set up
GPIO.setup(pin, GPIO.OUT)

# Set pin voltage to high
GPIO.output(pin, GPIO.HIGH)

# Do nothing for 3 sec
sleep(3)

# Set pin voltage to low
GPIO.output(pin, GPIO.LOW)

# Clear up
GPIO.cleanup()



