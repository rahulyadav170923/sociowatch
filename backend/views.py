from flask import Flask,render_template 
app = Flask(__name__)
import tweepy
from twitter import *


govt_twitter_handles=['smritirani','RailMinIndia']


#  to start collecting

@app.route('/collect_historical_data')
def collect_historical_data():
	historical_tweets('@smritirani')
	return "history"



# to show stats of collection of given twitter handle

@app.route('/all_twitter_handles/<string:twitter_handle>')
def twitter_handle_stats(twitter_handle):
	stats={}
	stats['count']=db[twitter_handle].count()
	stats['max_id']=db[twitter_handle].find_one(sort=[('_id',-1)])
	stats['since_id']=db[twitter_handle].find_one()
	tweets=list(db[twitter_handle].find())
	return render_template('twitter_handle.html',stats=stats,tweets=tweets)



# to show all collections and their stats

@app.route('/all_twitter_handles')
def all_twitter_handles():
	collection_names=db.collection_names()
	return render_template('all_twitter_handles.html',collection_names=collection_names[:-1])


# tweet

@app.route('/tweet_json')
def tweet_json():
	pass





