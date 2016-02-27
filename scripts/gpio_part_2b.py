from flask import Flask, request, jsonify, render_template
from time import sleep
try:
   import RPi.GPIO as GPIO
except:
    from MockGPIO import MockGPIO
    GPIO = MockGPIO()

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
        data = request.form
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
        # app.run()
        app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."
