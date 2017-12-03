#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:53:12 2017

@author: pesu
"""

'''

Python program that outputs a list of n-grams represented as string and a 
dictionary containing n-gram and its count as key-value pairs.

'''
from nltk import word_tokenize

file_content = open("in1.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def getNGrams(input_list, n):
    print('\n',n,'_Grams:\n')
    return [input_list[i:i+n] for i in range(len(input_list)-(n-1))]

list =getNGrams(wordlist, 1)
di=dict()

for i in list:
	d=""
	for j in i:
		d=d + j + " "
		
	print(d)
	if(d in di):
		di[d]=di[d]+1 
	else:
		di[d]=1

print(di)
