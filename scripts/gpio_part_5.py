from flask import Flask, request, jsonify, render_template, url_for, redirect

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
from flask_socketio import SocketIO, send

app.config['SECRET_KEY'] = 'evening_fun'
socketio = SocketIO(app)


# Return hello world to the index page
@app.route('/')
def hello_world():
    return render_template('index_part5.html')

# Can be used for the life update stream of tweets
@app.route('/get_tweets/<int:num_tweets>')
def get_last_tweet(num_tweets):
    # Limit the number of tweets that people can get.
    tweets = twitter.get_tweets('tweet_pi_tweet', num_tweets)
    tweet_list = []
    for tweet in tweets:
        tweet_stamp = tweet.created_at
        tweet_list.append(json.dumps({
            "author": tweet.author.screen_name,
            "tweet": tweet.text,
            "timeStamp": str(tweet_stamp),
            "vote": check_tweet_vote(tweet.text)}))
    return jsonify(tweet_list=tweet_list)

#TODO: function to return is there is a new tweet
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
    num_people_too_hot = sum([tweet.find('hotter')>0 for tweet in tweet_text])
    num_people_too_cold = sum([tweet.find('colder')>0 for tweet in tweet_text])

    turn_on_heater = num_people_too_cold > num_people_too_hot

    if turn_on_heater:
        gpio_state = GPIO.HIGH
    else:
        gpio_state = GPIO.LOW

    GPIO.output(pin, gpio_state)

@app.route('/newtweet')
def dsffsf():
    print 'sdfsf'
    s = 'hello ' + str( random.random() )
    emit_new_tweet(s)
    return '...'


import random


def emit_new_tweet(tweet):
    for i in range(3):
        import time
        time.sleep(0.5)
        print 'tweet ?', tweet
        socketio.emit('new_tweet', str(i) , broadcast=True)


def check_tweet_vote(tweet_text):
    if tweet_text.find('hotter') > 0:
        return True
    elif tweet_text.find('colder') > 0:
        return False
    else:
        return []

if __name__ == '__main__':
    try:
        # app.run(debug=True)
        socketio.run(app, host='0.0.0.0', port=8080, debug=True)
    finally:
        GPIO.cleanup()
        print "Bye."
