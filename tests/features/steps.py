# -*- coding: utf-8 -*-
from lettuce import *
from lettuce import step
from src.tweet_crawler import Twitter

@step(u'Given: Number of tweet is (\d+)')
def given_number_of_tweet_is_10(step, number):
    world.number = number
    twitt = Twitter()
    twitt._user_timeline(world.number)

@step(u'When: Print my tweet')
def when_print_my_tweet(step):
    print "ramonsl93"
    twitt = Twitter()
    twitt.print_tweets(world.number)

@step('Save my tweets')
def save_my_tweets(step):
    twitt = Twitter()
    twitt.save_tweets(world.number)