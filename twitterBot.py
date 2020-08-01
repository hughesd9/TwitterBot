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

#tweets = api.search('#cats')

keyword = input("Please enter a keyword you would like to search for:\n")
print(f'You entered {keyword}')

numberOfTweets = input("Please enter the number of tweets you would like to search for:\n")
print(f'You entered {numberOfTweets}')
numberOfTweets = int(numberOfTweets)

polarityNumber = input("Please enter the minimum polarity you would like a tweet to have:")
print(f'You entered {polarityNumber}')
polarityNumber = int(polarityNumber)

for tweet in tweepy.Cursor(api.search, keyword).items(numberOfTweets):
    try:
        #print(tweet.text)
        analysis = TextBlob(tweet.text)
        #print(analysis.sentiment)
        #print(analysis.sentiment[0])
        polarity = analysis.sentiment[0]
        if(polarity > polarityNumber):
            tweet.favorite()
            print('Favourited tweet')
    except tweepy.TweepError as e:
        print(e.reason)

