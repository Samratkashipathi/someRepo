from math import log
import operator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def majorityCnt(classList):
	classCount={}
	for vote in classList:
		if vote not in classCount.keys(): classCount[vote] = 0
		classCount[vote] += 1
	sortedClassCount = sorted(classCount.iteritems(),
	 key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]
#for calculting entropy
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
		 labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
   #-------------------------------------------------    
    #missing Code    
	for key in labelCounts:
		prob = float(labelCounts[key]) / numEntries
		shannonEnt -= prob * log(prob, 2)  # log base 2
	return shannonEnt
    #----------------------------------------------------
def createDataSet():
	dataSet = [[1, 1, 'yes'],
	         [1, 1, 'yes'],             
	         [1, 0, 'no'],
	         [0, 1, 'no'],
	         [0, 1, 'no']]
	labels = ['no surfacing','flippers']
	return dataSet, labels

def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet
#choosing the best feature to split
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet)
	bestInfoGain = 0.0; bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)
		newEntropy = 0.0
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)
		infoGain = baseEntropy - newEntropy
		print("feature : " + str(i))
		print("baseEntropy : "+str(baseEntropy))
		print("newEntropy : " + str(newEntropy))
		print("infoGain : " + str(infoGain))
		if (infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i
	return bestFeature
#print("the best feature to split is",chooseBestFeatureToSplit(myDat))

#function to build tree recursively
def createTree(dataSet,labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0]
	if len(dataSet[0]) == 1:
		return majorityCnt(classList)
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]
	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])
	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]
		myTree[bestFeatLabel][value] = createTree(splitDataSet\
		                   (dataSet, bestFeat, value),subLabels)
	return myTree

def createPlot(inTree):
	fig = plt.figure(1, facecolor='blue')
	fig.clf()
	axprops = dict(xticks=[], yticks=[])
	createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)    #no ticks
	#createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses 
	plotTree.totalW = float(getNumLeafs(inTree))
	plotTree.totalD = float(getTreeDepth(inTree))
	plotTree.xOff = -0.5/plotTree.totalW; plotTree.yOff = 1.0;
	plotTree(inTree, (0.5,1.0), '')
	plt.show()
	plt.savefig("temp.png")
	print("Finished")
    
    
myDat,labels=createDataSet()
print("DataSet:",myDat)
mytree = createTree(myDat, labels)
print(mytree)
#createPlot(mytree)