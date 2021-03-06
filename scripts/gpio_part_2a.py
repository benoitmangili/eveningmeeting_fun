from flask import Flask, send_from_directory
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
    return '<h1 align="center">Greetings, Stevenage Branch!</h1>' \
           '<p align="center">We hope you enjoy the show!</p>'


@app.route('/lamp/on')
def turn_me_on():
    GPIO.output(pin, GPIO.HIGH)
    return '<h1 align="center">Turning the lamp on</h1>'


@app.route('/lamp/off')
def turn_me_off():
    GPIO.output(pin, GPIO.LOW)
    return '<h1 align="center">Turning the lamp off</h1>'


# Example of how to serve a static file
@app.route('/static/<path:filename>')
def serve_static_file(filename):
    return send_from_directory('static', filename)


if __name__ == '__main__':
    try:
        # app.run() # Use to run locally only on your machine
        app.run(host='0.0.0.0', port=80) # This is visible on all computers on the network.
        # Use the IP address of machine that is running the script to contact the server.
    finally:
        GPIO.cleanup()
        print "Bye."
