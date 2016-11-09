# Collect Twitter data from the Tonight Show starring Jimmy Fallon
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import pandas as pd
import json
import os
import time

track_kw = raw_input("Track Keyword: ")
filename = raw_input("filename: ")
# Authentication tokens and keys
ckey = "3dKkKQNv4IhDRYTAq6yGuMb8t"
csecret = "jnKsBAXm0dFlKDRasTmu2Y34eBT3EUSdj6YkFRaj4b290vPPJh"
atoken = "2533036867-6NWiHaQRBAWrcjy59g2PM4hX0tuUs1Hw3TTILpk"
asecret = "NgOmykbCoVEWVv6uRFeYlOTmFweH5h2fJOhZi6KGah8pN"

start = time.time()
# The listener receives the data
class listener(StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format which needs to be decoded
        decoded = json.loads(data)
        try:
            # Converts UTF-8 to ASCII
            raw_txt = ""
            #raw_txt += decoded['user']['location'] + '\t'
            raw_txt += decoded['timestamp_ms'].encode('ascii','ignore') + '\t'
            raw_txt += str(decoded['user']['followers_count']) + '\t'
            raw_txt += str(decoded['user']['statuses_count']) + '\t'
            raw_txt += str(decoded['user']['friends_count']) + '\t'
            raw_txt += '"""' + decoded['text'].encode('ascii','ignore').replace('\n',' ') + '"""'
            raw_txt += "\n"
            with open(filename,'a') as F:
                F.write(raw_txt)
                F.close()
        except:
            print('error')
        if time.time() - start > 3600:
            return False
        return True
        
    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

twitterStream.filter(track=[track_kw])
