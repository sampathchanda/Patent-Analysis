#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 02:09:08 2016

@author: sam
"""

import ijson
import pickle
import time
import os

def dataCollection(filename):
    filepath, file_ext = os.path.splitext(filename)
    pkl_file = filepath + ".pkl"
    pkl_handle = open(pkl_file, 'wb')

    with open(filename, 'rb') as in_file:
        keyData = []

        for prefix, event, value in ijson.parse(in_file):
            #print prefix, event, value
            record = ""
            #if prefix.endswith('.webURI') and (event == 'string'):
            if prefix.endswith('.inventionTitle.content.item') and (event == 'string'):
                record = value
                if record != u' ':
                    keyData.append(record)

        # Dump List of titles into a Pickle file
        pickle.dump(keyData, pkl_handle)
        pkl_handle.close()

def loadPickle(filename):
    lol = pickle.load(open(filename, "rb"))
    return lol
        
# Example
#dataCollection('2016.json')
#lol = loadPickle('2016.pkl')
#print lol

#for yr in [1995]:
#    start_time = time.time()

#    dataCollection(yr)

#    print "Time taken: %s" % (time.time() - start_time)


