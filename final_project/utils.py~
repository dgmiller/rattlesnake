import re
import numpy as np
import pandas as pd
import string
import nltk
import datetime
import time
from matplotlib import pyplot as plt

trumplab = '/run/media/derekgm@byu.local/FAMHIST/Data/final_project/trump.txt'
clintonlab = '/run/media/derekgm@byu.local/FAMHIST/Data/final_project/clinton.txt'
trumpmint = '/media/derek/FAMHIST/Data/final_project/trump.txt'
clintonmint = '/media/derek/FAMHIST/Data/final_project/clinton.txt'

def get_file():
    print("""\n\tOptions\n
            1: trump from lab computer\n
            2: trump from linux mint\n
            3: clinton from lab computer\n
            4: clinton from linux mint\n\n""")
    name = raw_input("Enter number >> ")
    if name == "1":
        return trumplab
    elif name == "2":
        return trumpmint
    elif name == "3":
        return clintonlab
    elif name == "4":
        return clintonmint
    else:
        print "invalid input"

class TwitterCorpus(object):
    
    def __init__(self,filename,n):
        print("Loading file...")
        start = time.time()
        self.data = open(filename,'r').readlines()[:n]
        self.words = []
        self.user_stats = []
        self.timestamps = []
        self.time = []
        self.pos_tag = None
        err = 0
        for i,line in enumerate(self.data):
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
                print i,line
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
        self.u_mentions = []
        self.u_hashtags = []
        end = time.time()
        print("Time: %s" % (end-start))
        
    def clean_text(self):
        start = time.time()
        tweetwords = []
        for s in self.words:
            s = s.replace('"""','')
            mentions = re.findall(r'@\w*',s)
            hashtags = re.findall(r'#\w*',s)
            weblinks = re.findall(r'http\S*',s)
            retweets = re.findall('^RT ',s)
            self.mentions.append(mentions)
            self.hashtags.append(hashtags)
            self.weblinks.append(len(weblinks))
            self.retweets.append(len(retweets))
            for m in mentions:
                self.u_mentions.append(m)
            for h in hashtags:
                self.u_hashtags.append(h)
            for w in weblinks:
                s = s.replace(w,"")
            for r in retweets:
                s = s.replace(r,'')
            tweetwords.append(s.lower())
        self.words = tweetwords
        end = time.time()
        print("Time: %s" % (end-start))
        
    def tokenize_tag(self):
        start = time.time()
        L = len(self.words)
        tagged = []
        for i,t in enumerate(self.words):
            if i % int(L/4):
                print(float(i)/L)
            tokens = nltk.word_tokenize(t)
            tagged.append(nltk.pos_tag(tokens))
        self.pos_tag = tagged
        end = time.time()
        print("Time: %s" % (end-start))
    
    def convert_time(self):
        start = time.time()
        for t in self.timestamps:
            d = datetime.datetime.fromtimestamp(t)
            self.time.append([d.date(),d.time()])
        self.time = np.array(self.time)
        end = time.time()
        print("Time: %s" % (end-start))
        
def load_candidate():
    filename = get_file()
    c = TwitterCorpus(filename,None)
    print("\nclean_text")
    c.clean_text()
    print("\nconvert time")
    c.convert_time()
    return c
    
filepath = '/media/derek/FAMHIST/Data/final_project/'
filenames = ['trump_oct19.csv','trump_oct20.csv',
             'trump_oct24.csv','trump_oct26.csv',
             'trump_nov01.csv','trump_nov02.csv',
             'trump_nov03.csv','trump_nov05.csv',
             'trump_nov06.csv','trump_nov07.csv',
             'trump_nov08.csv','trump_nov09.csv']
def load_trump_df():
    """docstring"""
    f0 = filepath + filenames[0]
    tdf = pd.read_csv(f0)
    for f in filenames[1:]:
        f_ = filepath + f
        df = pd.read_csv(f_)
        tdf = tdf.append(df)
    return tdf

def get_items_from_lists(datalist):
    uni = []
    for L in datalist:
        if len(L) > 0:
            for entry in L:
                uni.append(entry)
    return uni
