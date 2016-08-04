from backend.twitter import *

def get_tweets(twitter_handle):
    for page in tweepy.Cursor(api.search,q='@'+twitter_handle,count=100,since_id=since_id).pages(10):
		data=[i._json for i in page]
        db[twitter_handle].insert_many(data)

def setup_tweets():
    for page in tweepy.Cursor(api.search,q='@'+twitter_handle,count=100).pages(10):
		data=[i._json for i in page]
        db[twitter_handle].insert_many(data)


def update_collection():
    collection_names=db.collection_names()
	if not collection_names:
		for i in govt_twitter_handles:
			db.create_collection(i)




if __name__ == '__main__':
    update_collection()
     # get last run twitter handle
     config=db.config.find_one({}) # details of cron job
     twitter_handles=db.config.find_one({})
     twitter_handle=twitter_handles[index]
     if
     while m['resources']['search']['/search/tweets']['remaining']-10>10 :
         get_tweets()
         m=api.rate_limit_status()
         config={}
         db.config.update({})
