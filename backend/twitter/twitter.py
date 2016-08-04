import pdb
from keys import *
from backend.twitter import *
from config import twitter_handle_list
# get all historical tweets (including tweets retweets,reply tweets )


def historical_tweets(twitter_handle,page_count,max_id=0):
	for page in tweepy.Cursor(api.search,q='@'+twitter_handle,count=100,max_id=max_id).pages(page_count):
		data=[i._json for i in page]
		db[twitter_handle].insert_many(data)
	return 'done'

# added in cronjob to download new tweets
def get_tweets():
	pass


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
