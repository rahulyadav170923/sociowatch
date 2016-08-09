
from backend.twitter import *
from config import twitter_handle_list

def update_collection():
    collection_names=db.collection_names()
    for i in twitter_handle_list:
        if i not in collection_names:
            db.create_collection(i)
            user=api.get_user(i)
            db.profiles.insert_one(user)

def create_config():
    db.create_collection('config')
    db.config.insert_one({'twitter_handle_index':0})

if __name__=='__main__':
    update_collection()
    if 'config' not in db.collection_names():
        create_config()
    add_profiles()
