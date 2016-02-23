from flask import Flask, request, jsonify

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


# Return hello world to the index page
@app.route('/')
def hello_world():
    return '<h1>Greetings, Stevenage Branch!</h1>' \
           '<p>We hope you enjoy the show!</p>'

@app.route('/temperature')
def measure_temperature():
    measurement = sensor.getMeasurement()
    return jsonify(value=measurement.value, time=measurement.timeStamp)


if __name__ == '__main__':
    try:
        app.run(debug=True)
        # app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."
