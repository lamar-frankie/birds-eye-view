import tweepy
from textblob import TextBlob
import credentials
import json

##Credentials and Auth##
consumer_key = credentials.consumer_key
consumer_secret = credentials.consumer_secret

access_token = credentials.access_token
access_token_secret = credentials.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

US_WOEID = 23424977
EXCLUDED_SUBJECTIVITY = 0.0
EXCLUDED_POLARITY = 0.0





def calculate_mood(key_word):
    mood = 0
    sentiment_dict = {}
    public_tweets = api.search(q=key_word, count=10)

    for tweet in public_tweets:
         analysis = TextBlob(tweet.text)

         if analysis.polarity != EXCLUDED_POLARITY and analysis.subjectivity != EXCLUDED_SUBJECTIVITY:
             sentiment_dict[tweet.text] = analysis.polarity

    for entry in sentiment_dict:
        mood += float(sentiment_dict[entry])

    print("Total Mood: " + str(mood))
    print("Number of entries: " + str(len(sentiment_dict)))

    print("Average Sentiment = " + str(mood/len(sentiment_dict)))
    return mood

def classify_mood(mood):
    if mood <= -0.75:
        print("Miserable")

    elif mood <= -0.50 and mood > -0.75:
        print("Somber")

    elif mood <= 0.25 and mood > -0.50:
        print("Disappointing")

    elif mood <= 0.25 and mood > -0.25:
        print("Meh")

    elif mood <= 0.50 and mood > 25:
        print("Pleased")

    elif mood <= 0.75 and mood > 0.50:
        print("Good")
    elif mood > 0.75:
        print("Overjoyed")


key_word = input("Enter keyword to search: ")
current_mood = calculate_mood(key_word)
classify_mood(current_mood)

