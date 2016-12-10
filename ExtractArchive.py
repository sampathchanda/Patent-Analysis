#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:24:27 2016

@author: praneetdutta
""" 


import numpy as np
import os
import gzip
import pdngram
from pdngram import LanguageModel

#path='/Users/praneetdutta/Desktop/data /cs'
path='./data /cs'
listp=[]
for filename in os.listdir(path):
    #print filename
    
    pathh=path+'/'+filename
    if(pathh.endswith('gz')):
     with gzip.open(pathh, 'rb') as f:
      file_content = f.read()
      
      #print "FILE CONTENT",file_content
      z=file_content[16:]
      z=" ".join(z.split())
      #print "z",z
      listp.append(z)
      
      
print "hi"      
our_ngram=LanguageModel(listp[:800],4)
print our_ngram.sample(200)

     