from flask import Flask, request, jsonify

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
    return '<h1>Greetings, Stevenage Branch!</h1>' \
           '<p>We hope you enjoy the show!</p>'


@app.route('/lamp', methods=['GET', 'POST'])
def lamp_stuff():
    if request.method == 'POST':
        data = request.json
        state = data['state']

        if state == 'High'.lower():
            gpio_state = GPIO.HIGH()
        elif state == 'Low'.lower():
            gpio_state = GPIO.LOW()
        else:
            print 'Invalid state!'
            gpio_state = []
            pass

        GPIO.output(pin, gpio_state)

    else:
        # determines the state from the raspberry pi pin
        gpio_state = GPIO.input(pin)
        if gpio_state:
            state = 'High'
        else:
            state = 'Low'

        return jsonify(state=state)


if __name__ == '__main__':
    try:
        app.run(debug=True)
        # app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."
