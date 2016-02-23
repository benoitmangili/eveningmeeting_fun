from unittest import TestCase
import Twitter


class TestTwitter(TestCase):

    def test_authenticate(self):

        t = Twitter.Twitter()
        self.assertTrue(t.api.auth.oauth.authorized)

    def test_send_tweet(self):
        t = Twitter.Twitter()
        t.send_tweet("It's too cold!")
