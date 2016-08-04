from backend.twitter.twitter import historical_tweets,twitter_key
from pymongo import MongoClient
import tweepy


Client=MongoClient()
db=Client['sociowatch']
# initialise api instance
auth = tweepy.OAuthHandler(twitter_key['consumerKey'], twitter_key['consumerSecret'])
auth.set_access_token(twitter_key['accessToken'], twitter_key['accessTokenSecret'])
api = tweepy.API(auth)
