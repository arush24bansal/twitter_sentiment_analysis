# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 19:20:10 2023

@author: Arush
"""

import dotenv as de
import tweepy
import os

de.load_dotenv()

bearer_token = os.getenv("BEARER_TOKEN")
api_key = os.getenv("API_KEY")
api_key_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

#auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
#api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token)

search_query = 'x "Elon Musk" Name -filter:retweets AND -filter:replies AND -filter:links'
tweets_limit = 1

try:
    #tweets = api.search_recent_tweets(search_query, count=tweets_limit, tweet_mode='extended')
    tweets = client.search_recent_tweets(search_query, max_results=tweets_limit)
    print(tweets)
except BaseException as err:
    print(f'status: Failed. {err}')