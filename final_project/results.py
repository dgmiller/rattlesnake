import utils as u
import numpy as np
import nltk

trumpfile = "/media/derek/FAMHIST/Data/final_project/trump.txt"
clintonfile = "/media/derek/FAMHIST/Data/final_project/clinton.txt"

print "starting"
djt = u.TwitterCorpus(trumpfile,None,10000)
djt.clean_text(None,None)

hrc = u.TwitterCorpus(clintonfile,None,10000)
hrc.clean_text(None,None)
