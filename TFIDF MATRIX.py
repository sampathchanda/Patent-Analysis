# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:23:08 2016

@author: praneetdutta
"""
import collections # optional, but we found the collections.Counter object useful
import scipy.sparse as sp
import numpy as np 
import sklearn.preprocessing as sk
import matplotlib.pyplot as plt
import numpy as np


import pickle

#####INSERT DATA CLEANING REMOVING STOP WORDS#########
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


testp = pickle.load( open( "2016.pkl", "rb" ) )
#print len(testp)
x=testp[1:500]

x=[xx.encode('UTF8') for xx in x]

a,b,c=tfidf(x)



def cosine_similarity(X):
    X=sk.normalize(X,norm='l2',axis=1)
    return X.dot(X.T).todense()
    
def cosine_similarity2(X):
    
    import numpy as np
    rowp=X.shape[0]
    M=np.zeros((rowp,rowp))
    for i in range(rowp):  
        for j in range(rowp):
            if(i==j):
                M[i][j]=0
            else:
                first=(X.getrow(i).toarray()[0])
                second=(X.getrow(j).toarray()[0])
                numerator=np.dot(first,second)
                xfirst=pow(sum([l*l for l in first]),0.5)
                xsecond=pow(sum([l*l for l in second]),0.5)
                denominator=xfirst*xsecond
                M[i][j]=float(numerator/denominator)
              
                
            
 
    return M
    pass
     
    
#doc_sim=cosine_similarity2(a)  
#print doc_sim
#plt.hist(gaussian_numbers)
##plt.title("Gaussian Histogram")
#plt.xlabel("Value")
#plt.ylabel("Frequency")

thres=15
print c
top=sorted(c, key=c.__getitem__)
top_n=top[len(top)-thres:]
#top_n=top_n[::-1]
print top_n 


import pylab as plt

DayOfWeekOfCall = [1,2,3]
DispatchesOnThisWeekday = [77, 32, 42]

LABELS = ["Monday", "Tuesday", "Wednesday"]

plt.bar(DayOfWeekOfCall, DispatchesOnThisWeekday, align='center')
plt.xticks(DayOfWeekOfCall, LABELS)
plt.show()
 
 

