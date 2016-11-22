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
    
    def __init__(self,filename):
        self.data = open(filename,'r').readlines()
        self.words = []
        self.user_stats = []
        self.timestamps = []
        for line in self.data:
            line = line.split('\t')
            # get everything except for the tweet
            try:
                self.user_stats.append([float(j) for j in line[1:-1]])
                self.timestamps.append(float(line[0][:10]))
            except:
                self.user_stats.append([-999,-999,-999])
                self.timestamps.append(-9999999999)
            # get the content of the tweet
            self.words.append(line[-1])
        # convert to numpy array
        self.timestamps = np.array(self.timestamps)
        self.user_stats = np.array(self.user_stats)
        # other variables defined later
        self.retweets = []
        self.mentions = []
        self.weblinks = []
        self.hashtags = []
        
    def clean_text(self,n,m):
        tweetwords = []
        for s in self.words[n:m]:
            mentions = re.findall(r'@\w*',s)
            hashtags = re.findall(r'#\w*',s)
            weblinks = re.findall(r'https\S*',s)
            retweets = re.findall('"RT ',s)
            punc = re.findall(r"[\?:,';]",s)
            punc_ = re.findall(r'[\.-]',s)
            self.mentions.append(mentions)
            self.hashtags.append(hashtags)
            self.weblinks.append(weblinks)
            self.retweets.append(retweets)
            for m in mentions:
                s = s.replace(m,"")
            for h in hashtags:
                s = s.replace(h,"")
            for w in weblinks:
                s = s.replace(w,"")
            for r in retweets:
                s = s.replace(r,'"')
            s = s.replace('"""','')
            for p in punc:
                s = s.replace(p,'')
            for p in punc_:
                s = s.replace(p,' ')
            extraspace = re.findall(r'\s+',s)
            for wsp in extraspace:
                s = s.replace(wsp,' ')
            s = s.lower()
            s = s.replace("trump","")
            s = s.replace("donald","")
            s = s.replace("hillary","")
            s = s.replace("clinton","")
            s = s.replace("obama","")
            tweetwords.append(s)
        self.words = tweetwords
        
    def clean_text2(self):
        tagged = []
        for t in self.tweets:
            tokens = nltk.word_tokenize(t)
            tagged.append(nltk.pos_tag(tokens))
        return tagged
        
    def top_words(self,m,feature_names,n):
        for i,topic in enumerate(m.components_):
            fnames = [feature_names[j] for j in topic.argsort()[:-n-1:-1]]
            print("Topic " + str(i))
            print(" ".join(fnames))
    
    def show_stats(self):
        return 0