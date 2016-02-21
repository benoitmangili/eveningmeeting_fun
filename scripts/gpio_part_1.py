# First show ciruit with transistor, LED and resistor.
# Turn the LED light on and off by running this script
# Then replace the LED and 330Ohm resistor on the collector side with the relay.
# Run the script again to turn the big light on and off.

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin = 36

# Set up
GPIO.setup(pin, GPIO.OUT)

# Set pin voltage to high
GPIO.output(pin, GPIO.HIGH)

sleep(3)

# Set pin voltage to low
GPIO.output(pin, GPIO.LOW)

# Clear up
GPIO.cleanup()



