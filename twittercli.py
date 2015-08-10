import os
import sys

consumer_key = os.environ.get("twitterConsumerKey")
consumer_secret = os.environ.get("twitterConsumerSecret")
access_token_key = os.environ.get("twitterAccessTokenKey")
access_token_secret = os.environ.get("twitterAccessTokenSecret")

try:
    from TwitterAPI import TwitterAPI
except ImportError:
    print("TwitterAPI module missing!")
    sys.exit(1)

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

status = input("Status: ")
r = api.request('statuses/update', {'status': status})

if r.status_code == 200:
    print("Status updated!")
else:
    print("Error!", r.status_code)
