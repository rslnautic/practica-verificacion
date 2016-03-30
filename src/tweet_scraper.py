import tweepy
from MongoDB import MongoDB


# Twitter API credentials
consumer_key = "40GvlhlFPNbVGkZnPncPH8DgB"
consumer_secret = "G595ceskX8iVH34rsuLSqpFROL0brp8ezzZR2dGvTKvcpPsKPw"
access_token = "397905190-LXMFC0clhtDxx5cITBWVFqVUKNQBKuqM06Ls4k5n"
access_token_secret = "nPzoHy5UwzOPUZVZO3JhBFRL3WgdM0jJKignxIzQ6nAS1"


def print_friends_tweets(name, n):
    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=name, count=n)
    db = MongoDB("verificacion")
    coll = db.collection(name)
    # print all tweets of screen_name account
    for tweet in new_tweets:
        print "-> " + tweet.text
        coll.save({"name": name, "tweet": tweet.txt})


if '__main__' == __name__:
    print 'Introduce el nombre del usuario para ver sus tweets'
    name = raw_input()
    print 'Introduce la cantidad de tweets que quieres mostrar maximo 200 por cuenta'
    n = raw_input()
    print_friends_tweets(name, n)