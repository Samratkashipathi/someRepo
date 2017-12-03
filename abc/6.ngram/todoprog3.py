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
from nltk import word_tokenize
from nltk.corpus import inaugural
#print(inaugural.fields())

def getNGrams(input_list, n):
    print('\n',n,'_Grams:\n')
    return [input_list[i:i+n] for i in range(len(input_list)-(n-1))]

words = list(inaugural.words('2009-Obama.txt'))
# words = word_tokenize(inaugural.words('2009-Obama.txt'))
print(words)

d = dict()

for word in words:
	if word in d:
		d[word] = int(d[word]) + 1
	else:
		d[word] = 1
print(len(d))


def keyfunction(k):
    return d[k]

# sort by dictionary by the values and print top 3 {key, value} pairs
for key in sorted(d, key=keyfunction, reverse=True)[:10]:
    print("%s: %i" % (key, d[key]))

big = getNGrams(words,2)
# print(big)

biDict = dict()
for uni in big:
	oo = ""
	for word in uni:
		# print(word)
		oo = oo + word + " "
	if oo in biDict:
		biDict[oo] += 1
	else:
		biDict[oo] = 1

# print(biDict)

def keyfunction1(k):
    return biDict[k]

for key in sorted(biDict,key=keyfunction1,reverse=True)[:2]:
	print("%s: %i" % (key, biDict[key]))