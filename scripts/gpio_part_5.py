from flask import Flask
from twitter.Twitter import Twitter
import json
try:
   import RPi.GPIO as GPIO
except:
    from MockGPIO import MockGPIO
    GPIO = MockGPIO()

# Instantiate Twitter class
twitter = Twitter()

GPIO.setmode(GPIO.BOARD)

pin = 36
GPIO.setup(pin, GPIO.OUT)

app = Flask(__name__)


# Return hello world to the index page
@app.route('/')
def hello_world():
    return '<h1>Greetings, Stevenage Branch!</h1>' \
           '<p>We hope you enjoy the show!</p>'

# Can be used for the life update stream of tweets
@app.route('/get_tweets/<int:num_tweets>')
def get_last_tweet(num_tweets):
    # Limit the number of tweets that people can get.
    tweets = twitter.get_tweets('tweet_pi_tweet', num_tweets)
    tweet_text = [tweet.text for tweet in tweets]
    tweet_author = [tweet.author.screen_name for tweet in tweets]

    return json.dumps([{"author": name, "tweet": text} for name,text in zip(tweet_author, tweet_text)])

#TODO: This should not be an endpoint and and run all the time. Should be put in a loop. Put this in a separate thread.
# Use the periodic timer
@app.route('/twitter_vote')
def twitter_vote():

    # Use only the 10 last tweets
    tweets = twitter.get_tweets('tweet_pi_tweet', 10)
    # check if need to handle case where there are less than 10
    tweet_text = [tweet.text for tweet in tweets]

    # Turn on heater via voting system
    # change to hotter/colder. 'make it hot, make it hotter'
    num_people_too_hot = sum([tweet.find('hot')>0 for tweet in tweet_text])
    num_people_too_cold = sum([tweet.find('cold')>0 for tweet in tweet_text])

    turn_on_heater = num_people_too_cold > num_people_too_hot

    if turn_on_heater:
        gpio_state = GPIO.HIGH()
    else:
        gpio_state = GPIO.LOW()

    GPIO.output(pin, gpio_state)


if __name__ == '__main__':
    try:
        # app.run(debug=True)
        app.run(host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."
