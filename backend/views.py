from flask import Flask,render_template,redirect,request,url_for
app = Flask(__name__)
import tweepy
from twitter import *
import pdb
import pymongo


govt_twitter_handles=['smritiirani','RailMinIndia','RashtrapatiBhvn','HRDMinistry']
#current_app_credentials=

#  to start collecting

@app.route('/collect_historical_data/<string:twitter_handle>',methods=['POST'])
def collect_historical_data(twitter_handle):
	pages=int(request.form['pages'])
	if db[twitter_handle].find_one(sort=[('_id',-1)]):
		max_id=db[twitter_handle].find_one(sort=[('_id',-1)])['id']
		historical_tweets(twitter_handle,pages,max_id)
	else :
		historical_tweets(twitter_handle,pages)
	return redirect(url_for('all_twitter_handles'))




# to show stats of collection of given twitter handle

@app.route('/all_twitter_handles/<string:twitter_handle>')
def twitter_handle_stats(twitter_handle):
	stats={}
	stats['twitter_handle']=twitter_handle
	stats['count']=db[twitter_handle].count()
	stats['max_id']=db[twitter_handle].find_one(sort=[('_id',-1)])
	stats['since_id']=db[twitter_handle].find_one()
	tweets=list(db[twitter_handle].find().sort('_id',pymongo.ASCENDING))
	rate_limit=api.rate_limit_status()
	return render_template('twitter_handle.html',stats=stats,tweets=tweets,rate_limit=rate_limit,app_no=app_no)



# to show all collections and their stats

@app.route('/all_twitter_handles')
def all_twitter_handles(): 
	collection_names=db.collection_names()
	if not collection_names:
		for i in govt_twitter_handles:
			db.create_collection(i)
		collection_names=db.collection_names()
	return render_template('all_twitter_handles.html',collection_names=collection_names[:-1])


# to check ratelimit status of the app credentials
@app.route('/app_credentials/<string:twitter_handle>',methods=['GET','POST'])
def change_app_credential(twitter_handle):
	global app_no,twitter_key,twitter_keys
	if app_no<3:
		app_no+=1
	else:
		app_no=0
	twitter_key=twitter_keys[app_no]
	return redirect(url_for('twitter_handle_stats',twitter_handle=twitter_handle))







