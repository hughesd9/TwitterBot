import tweepy
import textblob
from textblob import TextBlob

#Set up keys
#Add your keys in the empty quotation makrs
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#Authenticate and create variable to do analysis
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Do sentiment analysis
#Collect tweets that contain certain hash tag

tweets = api.search('#cats')

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
