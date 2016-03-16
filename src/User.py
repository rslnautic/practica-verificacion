import oauth
import tweepy


class User:
    def __init__(self, name):
        self.user = oauth.api.get_user(name)

    def print_friends_tweets(self):
        new_tweets = oauth.api.user_timeline(screen_name = "sergiorosello", count=200)
        for tweet in new_tweets:
            print "-> "+tweet.text

