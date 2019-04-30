#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tweepy
from tweepy import StreamListener
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import json

 
ACCESS_TOKEN = 'Enter your access token'
ACCESS_SECRET = 'Enter your access secret token'
CONSUMER_KEY = 'Enter your consumer key'
CONSUMER_SECRET = 'Enter your consumer secret'



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
print('hi')

#override tweepy.StreamListener to add logic to on_status
class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)
        
    def on_data(self, data):
        print(data)
        return True
    
    def on_error(self, status_code):
        if status_code == 420:
            return False

        
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    print('hi')
    stream = Stream(auth, l)
    x = stream.filter(track=['IranFloods'])
    with open('iranfloods.json', 'w') as f:
    	json.dump(x,f)


