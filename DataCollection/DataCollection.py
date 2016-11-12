#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 02:09:08 2016

@author: sam
"""

import ijson
import pickle
import time

def dataCollection(year):
    filename = "%s.json" % year
    pkl_file = "%s.pkl" % year
    pkl_handle = open(pkl_file, 'wb')
    with open(filename, 'rb') as in_file:
        keyData = []
        for prefix, event, value in ijson.parse(in_file):
            record = ""
            if prefix.endswith('.webURI') and (event == 'string'):
                record = value
                if record != u' ':
                    keyData.append(record)
          
        # Dump List of titles into a Pickle file
        pickle.dump(keyData, pkl_handle)
        pkl_handle.close()
        
# Example
for yr in [1995]:
    start_time = time.time()

    dataCollection(yr)

    print "Time taken: %s" % (time.time() - start_time)

def loadPickle(year):
    pkl_file = "%s.pkl" % year
    lol = pickle.load(open(pkl_file, "rb"))