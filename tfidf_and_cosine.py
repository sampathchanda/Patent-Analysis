# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:21:40 2016

@author: praneetdutta
"""
import scipy.sparse as sp
import numpy as np 
import sklearn.preprocessing as sk
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords
import collections
#REFERENCE ERIC CODE
def tfidf(abstract):

  all_words=set([a for a in " ".join(abstract).split(" ") if a!=""])
  all_words_dict={k:i for i,k in enumerate(all_words)}
  word_counts=[collections.Counter([a for a in d.split(" ") if a !=""]) for d in abstract]
  data=[a for wc in word_counts for a in wc.values()]
  rows=[i for i,wc in enumerate(word_counts) for a in wc.values()]
  #print all_words_dict
  cols=[all_words_dict[k] for wc in word_counts for k in wc.keys()]
  #print cols,rows
  X=sp.coo_matrix((data,(rows,cols)),(len(abstract),len(all_words)))    
  idf=np.log(float(len(abstract))/np.asarray((X>0).sum(axis=0))[0])
  return X*sp.diags(idf),list(all_words),all_words_dict
  
  
def cosine_similarity(X):
    X=sk.normalize(X,norm='l2',axis=1)
    return X.dot(X.T).todense()
    
