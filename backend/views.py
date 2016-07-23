from flask import Flask,render_template 
app = Flask(__name__)
import tweepy
from twitter import *


govt_twitter_handles=['smritirani','RailMinIndia','RashtrapatiBhvn','HRDMinistry']
#current_app_credentials=

#  to start collecting

@app.route('/collect_historical_data',methods=['POST'])
def collect_historical_data(twitter_handle):
	pages=request.form['pages']
	if db[twitter_handle].find_one(sort=[('_id',-1)])['id']:
		max_id=db[twitter_handle].find_one(sort=[('_id',-1)])['id']
		historical_tweets(twitter_handle,pages,max_id)
	else :
		historical_tweets(twitter_handle,pages)
	return redirect(url_for('twitter_handle_stats'),twitter_handle=twitter_handle)




# to show stats of collection of given twitter handle

@app.route('/all_twitter_handles/<string:twitter_handle>')
def twitter_handle_stats(twitter_handle):
	stats={}
	stats['twitter_handle']=twitter_handle
	stats['count']=db[twitter_handle].count()
	stats['max_id']=db[twitter_handle].find_one(sort=[('_id',-1)])
	stats['since_id']=db[twitter_handle].find_one()
	tweets=list(db[twitter_handle].find())
	return render_template('twitter_handle.html',stats=stats,tweets=tweets)



# to show all collections and their stats

@app.route('/all_twitter_handles')
def all_twitter_handles(): 
	collection_names=db.collection_names()
	if not collection_names:
		for i in govt_twitter_handles:
			db.create_collection(i)
		collection_names=db.collection_names()
	return render_template('all_twitter_handles.html',collection_names=collection_names[:-1])


# to check ratelimit status of the app





