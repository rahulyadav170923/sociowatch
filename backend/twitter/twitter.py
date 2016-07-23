import tweepy
import pdb
import os
import sys
sys.path.append(os.getcwd())

from keys import *

from pymongo import MongoClient
Client=MongoClient()
db=Client['sociowatch']
app_no=0
twitter_key=twitter_keys[app_no]

# initialise api instance
auth = tweepy.OAuthHandler(twitter_key['consumer_key'], twitter_key['consumer_secret'])
auth.set_access_token(twitter_key['access_token'], twitter_key['access_token_secret'])
api = tweepy.API(auth)


# get all historical tweets (including tweets retweets,reply tweets )

def historical_tweets(twitter_handle,page_count,max_id=0):
	for page in tweepy.Cursor(api.search,q='@'+twitter_handle,count=100,max_id=max_id).pages(page_count):
		data=[i._json for i in page]
		db[twitter_handle].insert_many(data)
	return 'done'



# not usable (doubt)
# get retweets to a given tweet
# add yield

def retweet(tweet_id):
	data=api.retweets(id=tweet_id)
	return data


# get replies
def get_replies():
	pass


# search tweets 
def search():
	pass


# popular handle
def popular_handle():
	pass

# accountability
def accountability():
	pass

#sentiment anylasis on replies
def sentiment_anylasis():
	pass

# build database in mongodb
#get all tweets mentioning a specific user
def database():
	pass
	

