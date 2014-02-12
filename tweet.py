#!/usr/bin/env python2.7
# tweet.py by Alex Eames http://raspi.tv/?p=5908  
import tweepy
import sys

# Consumer keys and access tokens, used for OAuth
consumer_key = 'type in your consumer key here'
consumer_secret = 'type in your consumer secret here'
access_token = 'type in your access token here'
access_token_secret = 'type in your access token secret here'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

if len(sys.argv) >= 2:
    tweet_text = sys.argv[1]

else:
    tweet_text = "Still messing about with tweepy and twitter API. :)"

if len(tweet_text) <= 140:
    api.update_status(tweet_text)
else:
    print "tweet not sent. Too long. 140 chars Max."