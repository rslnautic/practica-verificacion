import tweepy
from mongo_db import MongoDB


class Twitter:
    CONSUMER_KEY = "40GvlhlFPNbVGkZnPncPH8DgB"
    CONSUMER_SECRET = "G595ceskX8iVH34rsuLSqpFROL0brp8ezzZR2dGvTKvcpPsKPw"
    ACCESS_TOKEN = "397905190-LXMFC0clhtDxx5cITBWVFqVUKNQBKuqM06Ls4k5n"
    ACCESS_TOKEN_SECRET = "nPzoHy5UwzOPUZVZO3JhBFRL3WgdM0jJKignxIzQ6nAS1"

    def __init__(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET)
        self.twitter_api = tweepy.API(auth)

    def print_tweets(self,count=1):
        tweets = self._timeline(count)
        for tweet in tweets:
            print tweet

    def save_tweets(self,count=1):
        db = MongoDB("verificacion")
        coll = db.collection("twitter_friends")
        tweets = self._timeline(count)
        for tweet in tweets:
            coll.insert(tweet)

    # Returns the *count* numbers of tweets of your timeline and save it into a database
    def _timeline(self,count=200):
        tweets = []
        for tweet in tweepy.Cursor(self.twitter_api.user_timeline, count=count):
            text = tweet.text
            tweets.append(text)
        return tweets
