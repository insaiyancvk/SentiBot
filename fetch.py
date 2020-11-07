import os
import re
import numpy as np
import tweepy as tw
from requests_oauthlib import OAuth1Session

def clean_tweet(tweet): 
        ''' 
        Utility function to clean tweet text by removing links, special characters 
        using simple regex statements. 
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

consumer_key = "ydKKAoXFmqq97PZWYPs4wfy5S"
consumer_secret = "G1tFaa0Gop0kGCYsZzUpx1RLYjvIFv8qwS9H5dreZkgqlfCEnR"
access_token = "856759533640622080-HhlrgshaitB8gR2TXvrBq60XtNeRnXP"
access_token_secret = "8GYPov3JIJAJD8o2PvkGtdrXwUy5HewqEOXeTdAwKZP5Q"

auth = tw.OAuthHandler(consumer_key, consumer_secret, callback=None)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)


search_words = "elon musk"
date_since = "2018-11-16"

new_search = search_words + " -filter:retweets"
item = 5

tweets = tw.Cursor(api.search,
              q=new_search,
              lang="en",
              since=date_since).items(item)
twe_dict = {}
key = range(item)
tweet_dict = [tweet.text for tweet in tweets]
for i in key:
    twe_dict[i] = clean_tweet(tweet_dict[i])
print(twe_dict)