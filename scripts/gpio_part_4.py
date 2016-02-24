from flask import Flask, request, jsonify, render_template, url_for, redirect
from time import sleep
# Can only use DS18B20 on the raspberry pi
#from sensor.sensor import DS18B20 as sensor
from sensor.DummySensor import DummySensor as sensor

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

app = Flask(__name__)

threshold = []

# Load index page
@app.route('/')
def index():
    return render_template('index_part4.html')


@app.route('/temperature')
def measure_temperature():
    measurement = sensor.getMeasurement()
    return jsonify(value=measurement.value, time=measurement.timeStamp)


@app.route('/set_point', methods=['GET', 'PUT'])
def set_set_point():
    global threshold
    if request.method == 'POST':
        data = request.form
        threshold = data['set_point']
    else:
        return jsonify(threshold=threshold)

# add method that decides whether to turn the heater on or off
# (don't call /lamp, wrap code to change pin state in function and reuse here.)

@app.route('/lamp', methods=['GET', 'POST'])
def lamp_stuff():
    if request.method == 'POST':
        # Change state
        data = request.form
        state = data['state']

        if state == 'High':
            gpio_state = GPIO.HIGH()
        elif state == 'Low':
            gpio_state = GPIO.LOW()
        else:
            print 'Invalid state!'
            gpio_state = []
            pass  # TODO: escape the function at this point

        GPIO.output(pin, gpio_state)
        # Give the pin a moment to change state
        sleep(0.001)

    # determines the state from the raspberry pi pin
    gpio_state = GPIO.input(pin)
    if gpio_state:
        state = 'High'
    else:
        state = 'Low'
    # Return current state
    return jsonify(state=state)

if __name__ == '__main__':
    try:
        app.run(debug=True)
        # app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."
