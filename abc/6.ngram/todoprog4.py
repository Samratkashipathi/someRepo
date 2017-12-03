#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:05:53 2017

@author: pesu
"""
'''
Find the total number of words (tokens) in Obama's 2009 speech
(i.e., 2009-Obama.txt). Find the total number of distinct words (word types) 
in the same speech.

'''
from nltk.corpus import inaugural
print(inaugural.fields())