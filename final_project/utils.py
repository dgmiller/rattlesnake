import re
from scipy.sparse import csr_matrix
from sklearn.preprocessing import normalize
from sklearn.feature_extraction.text import TfidfVectorizer as Vec
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
    
    def __init__(self,filename,n,m):
        print("Loading file...")
        start = time.time()
        self.data = open(filename,'r').readlines()[n:m]
        self.tweets = []
        self.user_stats = []
        self.timestamps = []
        self.time = []
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
                self.tweets.append(line[-1])
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
        u_h = []
        u_m = []
        for s in self.tweets:
            m_str = ""
            h_str = ""
            s = s.replace('"""','')
            s = s.lower()
            mentions = re.findall(r'@\w*',s)
            hashtags = re.findall(r'#\w*',s)
            weblinks = re.findall(r'http\S*',s)
            retweets = re.findall('^rt ',s)
            self.mentions.append(len(mentions))
            self.hashtags.append(len(hashtags))
            self.weblinks.append(len(weblinks))
            self.retweets.append(len(retweets))
            for m in mentions:
                u_m.append(m)
            for h in hashtags:
                u_h.append(h)
            tweetwords.append(s)
        self.u_mentions = np.unique(u_m)
        self.u_hashtags = np.unique(u_h)
        self.tweets = tweetwords
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

    def make_df(self):
        df = pd.DataFrame()
        df['date'] = self.time[:,0]
        df['timestamp'] = self.timestamps
        df['usr_fol'] = self.user_stats[:,0]
        df['usr_num_stat'] = self.user_stats[:,1]
        df['usr_fri'] = self.user_stats[:,2]
        df['n_weblinks'] = self.weblinks
        df['n_mentions'] = self.mentions
        df['n_hashtags'] = self.hashtags
        df['RT'] = self.retweets
        return df
    
    def tokenize(self):
        start = time.time()
        self.V = Vec(ngram_range=(2,3),
                     stop_words='english',
                     min_df=100,
                     max_df=.8,
                     sublinear_tf=True,
                     use_idf=True)
        self.V.fit(self.tweets)
        end = time.time()
        print("Time: %s" % (end-start))

def load_candidate(n=0,m=-1000):
    """
    Trump: (1284126,)
    Clinton: (,)
    """
    filename = get_file()
    c = TwitterCorpus(filename,n,m)
    print("\nclean_text")
    c.clean_text()
    print("\nconvert time")
    c.convert_time()
    print("\ntokenize")
    c.tokenize()
    return c


