#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 08:21:22 2017

@author: pesu
"""
from numpy import linalg as la
import numpy as np
data = [[8,-6,2],[-6,7,-4],[2,-4,3]]
# w,v = la.eig(np.array([[8,-6,2],[-6,7,-4],[2,-4,3]]))
w,v = la.eig(data)
a = np.matrix(data)
print(a*a)
print(w,"\n")
print(v)