from flask import Flask, jsonify, render_template

# You can only use DS18B20 on the raspberry pi, so for testing
# on your dev machine use the dummy sensor.
from sensor.sensor import DS18B20 as sensor
# from sensor.DummySensor import DummySensor as sensor

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
    return jsonify(value=measurement.value, time=measurement.timeStamp)


if __name__ == '__main__':
    try:
        # app.run() # Use to run locally only on your machine
        app.run(host='0.0.0.0', port=80) # This is visible on all computers on the network.
        # Use the IP address of machine that is running the script to contact the server.
    finally:
        GPIO.cleanup()
        print "Bye."
