import sys
for path in sys.path:
    print path
"""Twitter app script"""

import tweepy
from src.mongo_db import MongoDB


class Twitter(object):  # pylint: disable=too-few-public-methods
    """Class Twitter"""

    def __init__(self):
        self.consumer_key = "40GvlhlFPNbVGkZnPncPH8DgB"
        self.consumer_secret = "G595ceskX8iVH34rsuLSqpFROL0brp8ezzZR2dGvTKvcpPsKPw"
        self.access_token = "397905190-LXMFC0clhtDxx5cITBWVFqVUKNQBKuqM06Ls4k5n"
        self.access_token_secret = "nPzoHy5UwzOPUZVZO3JhBFRL3WgdM0jJKignxIzQ6nAS1"
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth)

    # Method to print our tweets
    def print_tweets(self, count=1):
        tweets = self._user_timeline(count)
        for tweet in tweets:
            print tweet

    # Method to save our tweets
    def save_tweets(self, count=1):
        database = MongoDB("verificacion")
        coll = database.collection("tweets")
        tweets = self._user_timeline(count)
        for tweet in tweets:
            coll.insert({"tweet": tweet})

    # Returns the *count* numbers of tweets of your timeline and save it into a database
    def _user_timeline(self, count=200):
        tweets = []
        public_tweets = self.api.user_timeline(id=self.auth.get_username(), count=count)
        for tweet in public_tweets:
            text = tweet.text
            tweets.append(text)
        return tweets


if __name__ == '__main__':
    twepp = Twitter()
    twepp.print_tweets(10)
    twepp.save_tweets(10)
