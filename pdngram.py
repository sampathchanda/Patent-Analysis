#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:22:34 2016

@author: praneetdutta
"""
import collections # optional, but we found the collections.Counter object useful
import scipy.sparse as sp 
import numpy as np

class LanguageModel:
    def __init__(self, docs, n):
        self.counts=collections.defaultdict(lambda :collections.defaultdict(int))
        self.n=n
        for d in docs:
            words=[a for a in d.split(" ") if a !=""]
            for c in zip(*[words[i:] for i in range(n)]):
                self.counts[" ".join(c[:-1])][c[-1]]+=1
        self.count_sums=collections.defaultdict(int,{k:sum(v.values()) for k,v in self.counts.iteritems()})
        self.dictionary=set([a for a in " ".join(docs).split(" ") if a!=""])

    def sample(self,k):
        p0=np.array(self.count_sums.values())
        p0=p0/float(sum(p0))
        text=np.random.choice(np.array(self.count_sums.keys()),p=p0)
        hist=text
        for i in range(k):
            a=self.counts[hist]
            while(sum(a.values())==0):
                text=np.random.choice(np.array(self.count_sums.keys()),p=p0)
                hist=text
                a=self.counts[hist]
            next_word=np.random.choice(a.keys(),p=np.array(a.values())/float(sum(a.values())))
            text+=" "+next_word
            hist= " ".join((hist.split(" ")[1:]+[next_word])[:self.n-1])
        
        return text
                            