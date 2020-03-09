# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:38:51 2020

@author: Salman
"""

import tweepy
import time
from textblob import TextBlob 

CONSUMER_KEY = '-'
CONSUMER_SECRET = '-'
ACCESS_KEY = '-'
ACCESS_SECRET = '-'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id_SA.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def apply_sentiment_analysis():
    print('Looking for tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    public_tweets = api.search(q='Trump',since_id = last_seen_id,count = 5,tweet_mode='extended',result_type = 'recent ')
    for tweets in reversed(public_tweets):
        print('TWEET ALERT - ' + str(tweets.id) + '-' + tweets.full_text, flush=True)
        last_seen_id = tweets.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        analysis = TextBlob(tweets.full_text)
        print(analysis.sentiment)
        print('\n')
        
while True:
    apply_sentiment_analysis()
    time.sleep(5)
    
#while True:
#    public_tweets = api.search('HelloWorld112211',tweet_mode='extended')
#    print("Looking for tweets...")
#    for tweet in public_tweets:
#        print('TWEET ALERT - ' + str(tweet.id) + '-' + tweet.full_text, flush=True)
#        #    analysis = TextBlob(tweet.text)
#        #    print(analysis.sentiment)
#        time.sleep(5)
