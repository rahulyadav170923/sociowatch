import os
import sys
sys.path.append(os.getcwd())
from backend.twitter import *
from config import twitter_handle_list


def get_tweets(twitter_handle,since_id,twitter_handle_index):
    print "get tweets for {} from {}".format(twitter_handle,since_id)

    for page in tweepy.Cursor(api.search,q='@'+twitter_handle,count=100,since_id=since_id).pages(10):
        data=[i._json for i in page]
        print "{} tweets".format(len(data))
        if len(data)<10:
            print " {} tweets".format(len(data))
            twitter_handle_index+=1
            break
        db[twitter_handle].insert_many(data)
    return twitter_handle_index


def setup_tweets(twitter_handle):
    for page in tweepy.Cursor(api.search,q='@'+twitter_handle,count=100).pages(10):
        data=[i._json for i in page]
        db[twitter_handle].insert_many(data)



if __name__ == '__main__':
    config=db.config.find_one() # details of cron job
    twitter_handle_index=config['twitter_handle_index']
    twitter_handle=twitter_handle_list[twitter_handle_index]
    #import pdb;pdb.set_trace()
    while 1 :
        if db[twitter_handle].find_one():
            twitter_handle=twitter_handle_list[twitter_handle_index]
            since_id=db[twitter_handle].find_one(sort=[('_id',-1)])['id']
            twitter_handle_index=get_tweets(twitter_handle,since_id,twitter_handle_index)
        else :
            setup_tweets(twitter_handle)

        m=api.rate_limit_status()
        if m['resources']['search']['/search/tweets']['remaining']-10<20:
            print "exiting with {} left ".format(m['resources']['search']['/search/tweets']['remaining'])
            break
    if twitter_handle_list[twitter_handle_index]==twitter_handle_list[len(twitter_handle_list)-1]:
        twitter_handle_index=0
    else :
        twitter_handle_index+=1
    config={'twitter_handle_index':twitter_handle_index}
    db.config.update(db.config.find_one(),config)
