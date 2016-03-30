import unittest
import tweet_scraper

class test_twitter_unittest(unittest.TestCase):
    def setUp(self):
        pass

    def test_name_incorrect(self):
        self.assertEqual(tweet_scraper.print_friends_tweets("3rslnautic", 1), "Usuario incorrecto")

    def test_negative_count_tweets(self):
        self.assertRaises(TypeError, lambda: tweet_scraper.print_friends_tweets("ramonsl93", -1))

    def test_name_and_count_incorrect(self):
        self.assertRaises(Exception, lambda: tweet_scraper.print_friends_tweets("3rslnautic", -1))

    def test_fails_with_one_parameter(self):
        self.assertRaises(Exception, lambda: tweet_scraper.print_friends_tweets("ramonsl93"))


if __name__ == '__main__':
    unittest.main()
