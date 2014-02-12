#!/usr/bin/env python2.7
# twitterwin.py by Alex Eames http://raspi.tv/?p=5281
import tweepy
import random

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

follow2 = api.followers_ids() # gives a list of followers ids
print "you have %d followers" % len(follow2)

show_list = str(raw_input("Do you want to list the followers array?"))
if show_list == ('y' or 'yes' or 'Y' or 'Yes' or 'YES'):
    print follow2

def pick_winner():
    random_number = random.randint(0, len(follow2)-1)
    winner = api.get_user(follow2[random_number])
    print winner.screen_name, random_number

while True:
    pick = raw_input("Press Enter to pick a winner, Q to quit.")
    if pick == ('q' or 'Q' or 'quit' or 'QUIT' or 'Quit'):
        break
    pick_winner()