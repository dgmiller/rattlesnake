import re
import numpy as np
import pandas as pd
import string
import nltk
import datetime
import time
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.decomposition import NMF, LatentDirichletAllocation
from matplotlib import pyplot as plt

class TwitterCorpus(object):
    
    def __init__(self,filename,n,m):
        self.data = open(filename,'r').readlines()[n:m]
        self.words = []
        self.user_stats = []
        self.timestamps = []
        self.time = []
        self.pos = None
        err = 0
        for line in self.data:
            line = line.split('\t')
            # get everything except for the tweet
            try:
                # number of followers, statuses, and friends
                self.user_stats.append([float(j) for j in line[1:-1]])
                # time that the tweet was sent
                self.timestamps.append(float(line[0][:10]))
                # content of the tweet
                self.words.append(line[-1])
            except:
                err += 1
        print "Errors: " + str(err)
        # convert to numpy array
        self.timestamps = np.array(self.timestamps)
        self.user_stats = np.array(self.user_stats)
        # other variables defined later
        self.retweets = []
        self.mentions = []
        self.weblinks = []
        self.hashtags = []
        
    def clean_text(self):
        tweetwords = []
        for s in self.words:
            s = s.replace('"""','')
            mentions = re.findall(r'@\w*',s)
            hashtags = re.findall(r'#\w*',s)
            weblinks = re.findall(r'http\S*',s)
            retweets = re.findall('^RT ',s)
            #punc = re.findall(r"[\?:,';]",s)
            #punc_ = re.findall(r'[\.-]',s)
            self.mentions.append(mentions)
            self.hashtags.append(hashtags)
            self.weblinks.append(len(weblinks))
            self.retweets.append(len(retweets))
            for m in mentions:
                s = s.replace(m,"")
            for h in hashtags:
                s = s.replace(h,"")
            for w in weblinks:
                s = s.replace(w,"")
            for r in retweets:
                s = s.replace(r,'')
            s = s.replace("Trump","")
            s = s.replace("Clinton","")
            tweetwords.append(s.lower())
        self.words = tweetwords
        
    def clean_text2(self):
        tagged = []
        for t in self.words:
            tokens = nltk.word_tokenize(t)
            tagged.append(nltk.pos_tag(tokens))
        self.pos = np.array(tagged)
    
    def convert_time(self):
        for t in self.timestamps:
            d = datetime.datetime.fromtimestamp(t)
            self.time.append([d.date(),d.time()])
        self.time = np.array(self.time)
