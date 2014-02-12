#!/usr/bin/env python2.7
# tweet2.py by Alex Eames http://raspi.tv/?p=5941
import tweepy
import sys
import os
from datetime import datetime
 
i = datetime.now()
degree = unichr(176)         # code for degree symbol

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

if len(sys.argv) >= 2:        # use entered text as tweet
    tweet_text = sys.argv[1]

else:                         # if no entered text, tweet the temp
    now = i.strftime('%Y/%m/%d %H:%M:%S')
    cmd = '/opt/vc/bin/vcgencmd measure_temp'
    line = os.popen(cmd).readline().strip()
    temp = line.split('=')[1].split("'")[0]
    print now + ' Pi Processor Temperature is '+ temp + ' ' + degree +'C'
    tweet_text = now + ' Pi Processor Temperature is '+ temp + ' ' + degree +'C'

if len(tweet_text) <= 140:
    api.update_status(tweet_text)
else:
    print "tweet not sent. Too long. 140 chars Max."