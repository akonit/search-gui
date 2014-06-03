#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
import os

# search results
wfPath = "./json_output"

# search request
rfPath = "./web_request"

print "start emulator"

if not os.path.exists(wfPath):
    os.mkfifo(wfPath) 

if not os.path.exists(rfPath):
    os.mkfifo(rfPath) 

while True:
    rp = open(rfPath, 'r')
    request = rp.read()
    print "Recieve request %s" % request
    rp.close()

    wp = open(wfPath, 'w')
    wp.write("[[1, 'snipt1. some random text here'], [2, 'snipt2'], [3, 'snipt3'], [4, 'snipt4'], [5, 'snipt5'], [6, 'snipt6'], [7, 'snipt7'], [8, 'snipt8'], [9, 'snipt9'], [10, 'snipt10'], [11, 'snipt11'], [12, 'snipt12']]")		
    wp.close()
