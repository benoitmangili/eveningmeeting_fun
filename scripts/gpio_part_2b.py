from flask import Flask, request, jsonify, render_template
from time import sleep
import json
try:
   import RPi.GPIO as GPIO
except:
    # MockGPIO can be used for testing purposes when not working directly on the Pi
    from MockGPIO import MockGPIO
    GPIO = MockGPIO()
    print "Using Mock GPIO"

GPIO.setmode(GPIO.BOARD)

pin = 36

GPIO.setup(pin, GPIO.OUT)

app = Flask(__name__)

# Return hello world to the index page
@app.route('/')
def hello_world():
    return render_template('index_part2b.html')


@app.route('/lamp', methods=['GET', 'PUT'])
def lamp_stuff():
    if request.method == 'PUT':
        # Change state
        data = json.loads(request.data)
        state = data['state']

        set_gpio_state(state)

    # confirm the state has been set
    state = get_gpio_state(pin)

    return jsonify(state=state)


def set_gpio_state(state):
    if state == 'High':
        gpio_state = GPIO.HIGH
    elif state == 'Low':
        gpio_state = GPIO.LOW
    else:
        print 'Invalid state!'
        gpio_state = []
        return

    GPIO.output(pin, gpio_state)
    # Give the pin a moment to change state
    sleep(0.01)


def get_gpio_state(pin):

    # determines the state from the raspberry pi pin
    gpio_state = GPIO.input(pin)
    if gpio_state:
        state = 'High'
    else:
        state = 'Low'

    # Return current state
    return state


if __name__ == '__main__':
    try:
        # app.run() # Use to run locally only on your machine
        app.run(host='0.0.0.0', port=80) # This is visible on all computers on the network.
        # Use the IP address of machine that is running the script to contact the server.
    finally:
        GPIO.cleanup()
        print "Bye."
