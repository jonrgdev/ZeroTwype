import tweepy



if __name__ == '__main__' :
    consumer_key = "1UiJJJMJ1FrdrsXt6E49mPiSk"
    consumer_secret = "bOXLt76589fcdBRBdTjTQEtarLID92Byva3n5L83CJ5sQub3Ry"
    access_token = "1217805358871273472-xrQDA3hsoHlcEAFnleP2ySSALFZBJ7"
    access_token_secret = "UiiYkTna0EJKPfglPqqWK6ofMlpYAc1VNuzl6ZbIlL65x"
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(type(tweet.text))
        