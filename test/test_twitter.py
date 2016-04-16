from unittest import TestCase
from src.tweet_scraper import Twitter
from src.mongo_db import MongoDB
import mock
import mongomock


class TestTwitter(TestCase):
    def test_timeline(self):
        twitter = Twitter()
        twitter._timeline = mock.MagicMock(return_value=["hola"])
        tweets = twitter._timeline(1)
        self.assertEqual(tweets, ["hola"])

    @mock.patch('src.tweet_scraper.MongoDB')
    def test_save_tweets(self,mockClass):
        mockClass._conn.return_value = mongomock.MongoClient()

        twitter = Twitter()
        twitter._timeline = mock.MagicMock(return_value=["hola"])
        try:
            twitter.save_tweets(1)
        except Exception as e:
            self.fail(e)
