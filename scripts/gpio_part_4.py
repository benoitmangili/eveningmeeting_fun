from flask import Flask, request, jsonify, render_template, url_for, redirect
from time import sleep
# Can only use DS18B20 on the raspberry pi
#from sensor.sensor import DS18B20 as sensor
from sensor.DummySensor import DummySensor as sensor
from Controller import Controller
try:
   import RPi.GPIO as GPIO
except:
    from MockGPIO import MockGPIO
    GPIO = MockGPIO()

GPIO.setmode(GPIO.BOARD)

pin = 36

GPIO.setup(pin, GPIO.OUT)

# Instantiate Sensor Class
sensor = sensor()

# Instantiate Controller Class
t_lower = 15
t_upper = 20
controller = Controller(t_lower, t_upper)

app = Flask(__name__)

threshold = []

# Load index page
@app.route('/')
def index():
    return render_template('index_part3.html')


@app.route('/temperature')
def measure_temperature():
    measurement = sensor.getMeasurement()
    return jsonify(value=measurement.value, time=measurement.timeStamp)


@app.route('/set_point', methods=['GET', 'PUT'])
def set_set_point():
    global threshold
    if request.method == 'POST':
        data = request.form
        set_point_upper = data['set_point_upper']
        set_point_lower = data['set_point_lower']
        controller.update_temperature_range(set_point_lower, set_point_upper)
    else:
        return jsonify(threshold=threshold)


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


def get_heater_command():
    # Returns true if the heater is to be turned on or false otherwise
    measurement = sensor.getMeasurement()
    command = controller.get_command(measurement.value)
    return command

if __name__ == '__main__':
    try:
        # app.run(debug=True)
        app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."