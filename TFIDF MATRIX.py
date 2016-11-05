# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 20:23:08 2016

@author: praneetdutta
"""

def tfidf(docs):

    numberdocs=len(docs)
    allword={}
    i=0
    logup=np.log(numberdocs)
    listofdicts=[]
    for element in docs:
        dictelement={}
        wordinsent=element.split()
        for element1 in wordinsent:
            if element1 in dictelement:
                dictelement[element1]+=1
            else:
                dictelement[element1]=1
        listofdicts.append(dictelement)
        for wordd in dictelement.keys():
            if wordd in allword:
                allword[wordd]+=1
            else:
                allword[wordd]=1
        i+=1
  
