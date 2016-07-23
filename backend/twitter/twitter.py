import tweepy

import os
import sys
sys.path.append(os.getcwd())

from keys import twitter1_keys

from pymongo import MongoClient
Client=MongoClient()
db=Client['sociowatch']

# get all historical tweets (including tweets retweets,reply tweets )

def historical_tweets(twitter_handle,page_count,max_id=0):
	for page in tweepy.Cursor(api.search,q=twitter_handle,count=100,max_id=max_id).pages(page_count):
		page=[i._json for i in page]
		result=db[twitter_handle].insert_many(page)



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
	





if __name__=='__main__':
	auth = tweepy.OAuthHandler(twitter1_keys['consumer_key'], twitter1_keys['consumer_secret'])
	auth.set_access_token(twitter1_keys['access_token'], twitter1_keys['access_token_secret'])
	api = tweepy.API(auth)
	historical_tweets()
