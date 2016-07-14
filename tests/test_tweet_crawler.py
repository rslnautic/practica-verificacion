import unittest
from src.tweet_crawler import Twitter
from src.database import MongoDB
import mock
import mongomock


class TestTwitter(unittest.TestCase):
    def test_auth_credentials(self):
        twitter = Twitter()
        self.assertEquals(twitter.consumer_key,"40GvlhlFPNbVGkZnPncPH8DgB")
        self.assertEquals(twitter.consumer_secret, "G595ceskX8iVH34rsuLSqpFROL0brp8ezzZR2dGvTKvcpPsKPw")
        self.assertEquals(twitter.access_token, "397905190-LXMFC0clhtDxx5cITBWVFqVUKNQBKuqM06Ls4k5n")
        self.assertEquals(twitter.access_token_secret, "nPzoHy5UwzOPUZVZO3JhBFRL3WgdM0jJKignxIzQ6nAS1")

    def test_user_timeline(self):
        twitter = Twitter()
        twitter._user_timeline = mock.MagicMock(return_value=["hola"])
        tweets = twitter._user_timeline(1)
        self.assertEqual(tweets, ["hola"])

    @mock.patch('src.tweet_crawler.MongoDB')
    def test_save_tweets(self, mockClass):
        mockClass._conn.return_value = mongomock.MongoClient()

        twitter = Twitter()
        twitter._user_timeline = mock.MagicMock(return_value=["hola"])
        self.fail();
        try:
            twitter.save_tweets(1)
        except Exception as e:
            self.fail(e)


if __name__ == '__main__':
    unittest.main()