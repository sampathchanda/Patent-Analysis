# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:23:08 2016

@author: praneetdutta
"""
import collections # optional, but we found the collections.Counter object useful
import scipy.sparse as sp
import numpy as np 


import pickle

def tfidf(abstract):

  all_words=set([a for a in " ".join(abstract).split(" ") if a!=""])
  all_words_dict={k:i for i,k in enumerate(all_words)}
  word_counts=[collections.Counter([a for a in d.split(" ") if a !=""]) for d in abstract]
  data=[a for wc in word_counts for a in wc.values()]
  rows=[i for i,wc in enumerate(word_counts) for a in wc.values()]
  cols=[all_words_dict[k] for wc in word_counts for k in wc.keys()]
  X=sp.coo_matrix((data,(rows,cols)),(len(abstract),len(all_words)))    
  idf=np.log(float(len(abstract))/np.asarray((X>0).sum(axis=0))[0])
  return X*sp.diags(idf),list(all_words)


testp = pickle.load( open( "2016.pkl", "rb" ) )
print len(testp)
x=testp[1:500]

x=[xx.encode('UTF8') for xx in x]

a,b=tfidf(x)
a[0].get_shape()
#favorite_color = pickle.load( open( "save.p", "rb" ) )
 
 
 

