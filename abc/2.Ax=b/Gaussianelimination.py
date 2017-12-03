#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 08:34:02 2017

@author: pesu
"""

import numpy as np
def Gauss(A, b):
    '''
    Gaussian elimination with no pivoting.
    % input: A is an n x n nonsingular matrix
    %        b is an n x 1 vector
    % output: x is the solution of Ax=b.
    
    '''
    n =  len(A)
    if b.size != n:
        raise ValueError("Invalid argument: incompatible sizes between A & b.", b.size, n)
    for pivot_row in range(n-1):
        for row in range(pivot_row+1, n):
            multiplier = A[row][pivot_row]/A[pivot_row][pivot_row]
            #the only one in this column since the rest are zero
            A[row][pivot_row] = multiplier
            for col in range(pivot_row + 1, n):
                A[row][col] = A[row][col] - multiplier * A[pivot_row][col]
            #Equation solution column
            b[row] = b[row] - multiplier*b[pivot_row]
    print("REUSLTS AFTER GUASSIAN ELIMINATION")
    print('--------------------------------------')
    print(A)
    print(b)
    x = np.zeros(n)
    #print 'before',x
    k = n-1
    x[k] = b[k]/A[k,k]
    #print 'b value is ',b[k]
    while k >= 0:
        x[k] = (b[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
        k = k-1
    return x

if __name__ == "__main__":
    #Take matrix A
    A=np.array([[0.,1.,1.],[2.,0.,3.],[1.,1.,1.]])
    #Take Matrix b
    b=np.array([[2.],[5.],[3.]])
    print(Gauss(A,b))