from backend.twitter.twitter import historical_tweets
from pymongo import MongoClient
import tweepy
import os


Client=MongoClient()
db=Client['sociowatch']
# initialise api instance
auth = tweepy.OAuthHandler(os.environ['consumerKey'], os.environ['consumerSecret'])
auth.set_access_token(os.environ['accessToken'], os.environ['accessTokenSecret'])
api = tweepy.API(auth)
