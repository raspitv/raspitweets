#!/usr/bin/env python2.7
# tweetpic6BLOG.py by Alex Eames http://raspi.tv/?p=6004
# take a photo with the Pi camera, overlay some text
# then overlay a small logo and tweet the final image
import tweepy
from time import sleep
from subprocess import call
from datetime import datetime
import sys

if len(sys.argv) >= 2:
    tweet_text = sys.argv[1]

else:
    tweet_text = "Photo from insert your location here"

if len(tweet_text) > 110:
    print "tweet not sent. Too long. 110 chars Max. Try again."
    sys.exit()

# Twitter Bits. Consumer keys and access tokens, used for OAuth
consumer_key = 'copy your consumer key here'
consumer_secret = 'copy your consumer secret here'
access_token = 'copy your access token here'
access_token_secret = 'copy your access token secret here'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

def photo_tweet():
    i = datetime.now()
    now = i.strftime('%Y%m%d-%H%M%S')
    tweettime = i.strftime('%Y/%m/%d %H:%M:%S')
    photo_name = now + '.jpg'
    cmd = 'raspistill -t 500 -w 1024 -h 768 -o /home/pi/' + photo_name    
    print 'cmd ' +cmd
    print "about to take photo"
    call ([cmd], shell=True)
    print "photo taken"
    photo_path = '/home/pi/' + photo_name
    status = tweet_text + ' #optionalhashtag ' + tweettime 

# Add text overlay of data on the photo we just took
    print "about to set overlay_text variable"
    overlay_text = "/usr/bin/convert "+ photo_path + "  -pointsize 36 -fill white -annotate +40+728 '" + tweettime + "' "
    overlay_text += " -pointsize 36 -fill white -annotate +40+630 'Your Text annotation here ' " + photo_path

    print "overlaying text"
    call ([overlay_text], shell=True)

    print "adding your logo" # you'll need a file called overlay.png in /home/pi
    overlay_text = '/usr/bin/convert '+ photo_path + ' /home/pi/overlay.png -geometry +1+1 -composite ' + photo_path
    call ([overlay_text], shell=True)
    print "added logo 1"

    print "tweeting photo"
    api.update_with_media(photo_path, status=status)    
    print "photo tweeted, deleting .jpg"
    cmd = 'rm ' + photo_path 
    call ([cmd], shell=True)

print 'start of program' 

photo_tweet()