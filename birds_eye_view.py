import tweepy
from textblob import TextBlob
import credentials

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret

access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


key_word = input("Enter keyword to search: ")
api = tweepy.API(auth)

public_tweets = api.search(q=key_word, count=1000)

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

