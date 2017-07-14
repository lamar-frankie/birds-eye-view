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

key_word = input("Enter keyword to search: ")

public_tweets = api.search(q=key_word, count=10)

sentiment_dict = {}

#TODO: Fix logic that averages the moods
for tweet in public_tweets:
     print(tweet.text)
     analysis = TextBlob(tweet.text)

     if analysis.polarity != EXCLUDED_POLARITY and analysis.subjectivity != EXCLUDED_SUBJECTIVITY:
         sentiment_dict[tweet.text] = analysis.polarity
         print(sentiment_dict)
         print(len(sentiment_dict))

mood = 0

for entry in sentiment_dict:
    mood += float(sentiment_dict[entry])
    print(sentiment_dict.values())



print("Mood: " + str(mood))
print("Number of entries: " + str(len(sentiment_dict)))

print("Average Sentiment = " + str(mood/len(sentiment_dict)))

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




