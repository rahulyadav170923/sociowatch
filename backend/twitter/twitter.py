import tweepy
#from keys import twitter_keys

auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)


# can i put yeild here 

# tweets by a twitter handler @pmo
#10 requests
#add cursor usage

def tweets(screen_name):
	data=api.user_timeline(id='twitterapi',count=10)
	filter_data=[]
	for i in data:
		filter_data.append(i)
	return filter_data




# not usable (doubt)
# get retweets to a given tweet
# add yield
def retweet(tweet_id):
	data=api.retweets(id=tweet_id)
	return data





