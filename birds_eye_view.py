import tweepy
from textblob import TextBlob
import credentials
import json

consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret

access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


#key_word = input("Enter keyword to search: ")
api = tweepy.API(auth)



#public_tweets = api.search(q=key_word, count=1000)


# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)

US_WOEID = 23424977

def get_trends():
    us_trending_topics = api.trends_place(US_WOEID,)
    data = us_trending_topics[0]
    trends = data['trends']
    names = [trend['name'] for trend in trends]
    top_ten_trends = names[:10]
    return top_ten_trends

print(get_trends())


def scrub_trends(dict_of_trends):
    scrubbed_trends = get_trends()
    for trend in scrubbed_trends:
        if trend[0] == '#':
            scrubbed_trends.remove(trend)
    return scrubbed_trends

def analyze_trends(list_of_trends):
    for trend in list_of_trends:
        list_of_tweets_about_trend = api.search(q=trend, count=1000)






##TODO get list of top 10 trending topics
##TODO run sentiment analysis on 1000 tweets for each of top 10 items
##TODO average the sentiments to determine overall mood of US