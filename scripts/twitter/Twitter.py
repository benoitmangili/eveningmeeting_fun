# From http://tweepy.readthedocs.org/en/v3.5.0/auth_tutorial.html#auth-tutorial
import tweepy
import json


class Twitter:
    """Class exposing useful stuff from the Twitter API"""

    def __init__(self):
        # The twitter tokens are stored in a file
        token_file = open('twitter/tokens.json')
        self.tokens = json.load(token_file)
        token_file.close()

        self.api = self.authenticate()

    def authenticate(self):

        auth = tweepy.OAuthHandler(self.tokens['consumer'], self.tokens['consumer_secret'])

        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError:
            print 'Error! Failed to get request token.'

        auth.secure = True
        auth.set_access_token(self.tokens['access'], self.tokens['access_secret'])
        api = tweepy.API(auth)
        print(api.me().name)
        return api

    def send_tweet(self, message):
        # Post a tweet
        self.api.update_status(status=message)

    def get_tweets(self, screen_name, number_of_tweets):
        # Returns a list of last number_of_tweets tweets
        tweets = self.api.user_timeline(screen_name=screen_name, count=number_of_tweets, include_rts=True)
        return tweets

    @staticmethod
    def extract_msg_and_author(tweet):
        return "Latest Tweet: \"" + tweet.text + "\" by @" + tweet.author.screen_name

    def send_picture(self, message, picture_file_name):
        # Post an image in response to the original tweet
        self.api.update_with_media(picture_file_name, message, in_reply_to_status_id=tweets[len(tweets)-1].id)

    def update_profile_image(self, filename):
        self.api.update_profile_image(filename)


# TODO: use google text to speech to read out tweets