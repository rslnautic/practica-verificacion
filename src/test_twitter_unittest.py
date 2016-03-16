import unittest
import tweet_scraper

class TestEjemplo(unittest.TestCase):

    def setUp(self):
        pass

    def test_name_incorrect(self):
        self.assertEqual(tweet_scraper.print_friends_tweets("3rslnautic"), "Usuario incorrecto")

    def test_negative_count_tweets(self):
        self.assertRaises(TypeError, lambda: tweet_scraper.print_friends_tweets("ramonsl93", -1))

    def test_name_count_(self):
        self.assertRaises(Exception, lambda: concat(1,2))

    def test_fails_with_one_strings(self):
        self.assertRaises(Exception, lambda: concat("a"))

    def test_works_with_more_than_2_elements(self):
        try:
            concat("a","b", "c")
            concat("a","b","d","e","f")
        except Exception:
            self.fail("concat raised Exception unexpectedly!")

    def test_fail_when_more_than_10_elements(self):
        self.assertRaises(Exception, concat("a","b","d","e","f","a","b","d","e","f"))

if __name__ == '__main__':
    unittest.main()
