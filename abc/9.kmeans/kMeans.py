#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 08:46:13 2017

@author: pesu
"""

import random

def k_means(data, k):
	# 1. k initial "means" are randomly selected from the data set.
    if k < len(data):
        initialCentroidPos = []
        while(len(initialCentroidPos) != k):
            pos = random.randint(0,len(data)-1)
            if(pos not in initialCentroidPos):
                initialCentroidPos.append(pos)
        print(initialCentroidPos)
        centroids = {}
        change = 1
        for i in initialCentroidPos:
            centroids[data[i]] = []
        print("Centroids:",centroids)
        iterations = 0
        while(change == 1):
            for i in centroids:
                centroids[i] = []
            print("ccentroids:",centroids)
            for i in data:
                dist = max(data)
                # print(dist)
                centroid = 0
                for j in centroids:
                    if(abs(i-j) < dist):
                        dist = abs(i-j)
                        centroid = j
                centroids[centroid].append(i)
            print("CCC:",centroids)
            temp = {}
            for i in centroids:
                mean = round(sum(centroids[i])/len(centroids[i]),2)
                temp[mean] = centroids[i]
            print("temp",temp)
            changedCentroids = temp.keys();
            oldCentroids = centroids.keys();
            change = 0;
            if(sorted(changedCentroids) != sorted(oldCentroids)):
                change = 1
            
            centroids = temp;
            iterations += 1;
        print("clusters")
        print(centroids)
        print("Iterations:",iterations)
        return centroids
    	



if __name__ == '__main__':
	Ages = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
	print(list(k_means(Ages, 10)))