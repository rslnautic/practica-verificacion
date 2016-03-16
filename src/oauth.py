from __future__ import absolute_import, print_function

import tweepy

consumer_key = "40GvlhlFPNbVGkZnPncPH8DgB"
consumer_secret = "G595ceskX8iVH34rsuLSqpFROL0brp8ezzZR2dGvTKvcpPsKPw"

access_token = "397905190-LXMFC0clhtDxx5cITBWVFqVUKNQBKuqM06Ls4k5n"
access_token_secret = "nPzoHy5UwzOPUZVZO3JhBFRL3WgdM0jJKignxIzQ6nAS1"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
