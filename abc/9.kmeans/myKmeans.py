import random

def k_means(data,k):
	if(k<len(data)):
		initialCentroidPos = []
		while(len(initialCentroidPos) != k):
			pos = random.randint(0,len(data)-1)
			if(pos not in initialCentroidPos):
				initialCentroidPos.append(pos)
		print(initialCentroidPos)
		centroids = {}
		for i in initialCentroidPos:
			centroids[data[i]] = []
		change = 1
		while(change == 1):
			for i in centroids:
				centroids[i] = []

			for i in data:
				dist  = max(data)
				centroid = 0
				for j in centroids:
					if(abs(i-j)<dist):
						dist = abs(i-j)
						centroid = j
				centroids[centroid].append(i)

			temp = {}

			for i in centroids:
				mean = round(sum(centroids[i])/len(centroids[i]),2)
				temp[mean] =  centroids[i]
			
	return [10,10]
if __name__ == '__main__':
	Ages = [15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65]
	print(list(k_means(Ages, 10)))