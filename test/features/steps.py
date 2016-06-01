from lettuce import *
from src.tweet_scraper import Twitter

@step('I have the number (\d+)')
def have_the_number(step, number):
    world.number = int(number)

@step('I search the tweets')
def search_tweets(step):
    tweet_app = Twitter()
    teets = tweet_app._user_timeline(world.number)

@step('I see tweets (\d+)')
def print_tweets(step):
    tweet_app = Twitter()
    tweet_app.print_tweets(world.number)


