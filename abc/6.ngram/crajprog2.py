#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 09:50:35 2017

@author: pesu
"""

from nltk import word_tokenize

file_content = open("in2.txt").read()
wordlist = word_tokenize(file_content)

print('\nTokens List:\n')
print(wordlist)

def getNGrams(input_list, n):
  print('\n',n,'_Grams:\n')  
  result=zip(*[input_list[i:] for i in range(n)])
  return result

#gram=getNGrams(wordlist, 2)
l1 = list(getNGrams(wordlist, 2))
print(l1)