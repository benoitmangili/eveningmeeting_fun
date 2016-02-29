from flask import Flask, request, jsonify, render_template, url_for, redirect
# Can only use DS18B20 on the raspberry pi
# TODO: comment the real sensor in!!!
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


# Load index page
@app.route('/')
def index():
    return render_template('index_part3.html')


@app.route('/temperature')
def measure_temperature():
    measurement = sensor.getMeasurement()
    # TODO: remove the random multiplier before the talk!!
    import random
    measurement.value = random.random()*10
    return jsonify(value=measurement.value, time=measurement.timeStamp)


if __name__ == '__main__':
    try:
        # app.run(debug=True)
        app.run(host='0.0.0.0', port=80, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."