#!/usr/bin/env python2.7
# tweetpic.py take a photo with the Pi camera and tweet it
# by Alex Eames http://raspi.tv/?p=5918
import tweepy
from subprocess import call
from datetime import datetime
 
i = datetime.now()               #take time and date for filename
now = i.strftime('%Y%m%d-%H%M%S')
photo_name = now + '.jpg'
cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name 
call ([cmd], shell=True)         #shoot the photo

# Consumer keys and access tokens, used for OAuth
consumer_key = 'copy your consumer key here'
consumer_secret = 'copy your consumer secret here'
access_token = 'copy your access token here'
access_token_secret = 'copy your access token secret here'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Send the tweet with photo
photo_path = '/home/pi/' + photo_name
status = 'Photo auto-tweet from Pi: ' + i.strftime('%Y/%m/%d %H:%M:%S') 
api.update_with_media(photo_path, status=status)
