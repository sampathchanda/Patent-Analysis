# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:23:08 2016

@author: praneetdutta
"""

import scipy.sparse as sp
import numpy as np 
import sklearn.preprocessing as sk
import matplotlib.pyplot as plt
import numpy as np
from nltk.corpus import stopwords
import collections
stop_list=stopwords.words('english')
from tfidf_and_cosine import tfidf
from tfidf_and_cosine import cosine_similarity
#stop=[xx.encode('UTF8') for xx in stop_list]
#print stop
import pickle




testp = pickle.load( open( "2016.pkl", "rb" ) )
#print len(testp)
x=testp[1:5000]

x=[xx.encode('UTF8') for xx in x]
#####STOP WORD REMOVAL START########################
test_1=[]
for sentence in x:
    sentence=sentence.lower()
    text = ' '.join([word for word in sentence.split() if word not in (stopwords.words('english'))])
    test_1.append(text)
    
#print test_1
##############STOP WORD REMOVAL COMPLETE############################
    
    
sparse_mat,word_list,dict_words=tfidf(x)



             
###########GETTING MOST SIMILAR DOCUMENTS############
doc_sim=cosine_similarity(sparse_mat)  
#print doc_sim
M,N=(doc_sim).shape
#print M,N
a = np.ones((M, M), int)
np.fill_diagonal(a, 0)
#print a
Cosine_List=np.multiply(doc_sim,a)
#print Cosine_List
Highest_Sim=np.argmax(Cosine_List,axis=1)
High=np.argmax(Highest_Sim)
#print High
#print testp[High]
plt.hist(Highest_Sim,M)
plt.title("Document Similiarty Histogram")
plt.xlabel("Document Number")
plt.ylabel("Frequency")

###############PLOTTING THEM#####################

thres=15
print dict_words
#top=sorted(dict_words, key=c.__getitem__)
top = sorted(dict_words.items(), key=operator.itemgetter(1))
print top
#top_n=top[len(top)-thres:]
#top_n=top_n[::-1]
#print top_n 


#import pylab as plt

#DayOfWeekOfCall = [1,2,3]
#DispatchesOnThisWeekday = [77, 32, 42]

#LABELS = ["Monday", "Tuesday", "Wednesday"]

#plt.bar(DayOfWeekOfCall, DispatchesOnThisWeekday, align='center')
#plt.xticks(DayOfWeekOfCall, LABELS)
#plt.show() 
 

