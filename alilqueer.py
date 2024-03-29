# Retweet bot for Twitter, using Python and Tweepy.
# Specifically checks from a list of known accounts for a given hashtag to retweet
# Author: Sahil Kochar
# Used for Alilqueer

# Modified from https://github.com/0xGrimnir/Simple-Retweet-Bot by Tyler L. Jones

import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!
accounts_file = open("accounts.txt", "r")
account = accounts_file.readline()[:-1]
accounts = []
while account != '':
    accounts.append(account)
    account = accounts_file.readline()[:-1]
print(accounts)
accounts_file.close()
for account in accounts:
       for tweet in tweepy.Cursor(api.user_timeline, id=account, tweet_mode="extended").items(2):
            
           #Checks for the hashtag in the tweet before retweeting
           if '#alilqueer' in tweet.full_text:
               try:
                   print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet the following:')
                   print('\t'+tweet.full_text)

                   tweet.retweet()
                   print('Retweet published successfully.')

                   # Where sleep(10), sleep is measured in seconds.
                   # Change 10 to amount of seconds you want to have in-between retweets.
                   # Read Twitter's rules on automation. Don't spam!
                   sleep(10)

               # Some basic error handling. Will print out why retweet failed, into your terminal.
               except tweepy.TweepError as error:
                   print('\nError. Retweet not successful. Reason: ')
                   print(error.reason)

               except StopIteration:
                   break
