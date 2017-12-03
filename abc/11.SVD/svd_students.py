from scipy import linalg
import numpy as np
Data=np.array([[4.9,3.0,1.4,0.2],
	[4.7,3.2,1.3,0.2],
	[4.6,3.1,1.5,0.2],
	[5.0,3.6,1.4,0.2],
	[5.4,3.9,1.7,0.4],
	[4.6,3.4,1.4,0.3],
	[5.0,3.4,1.5,0.2],
	[4.4,2.9,1.4,0.2],
	[4.9,3.1,1.5,0.1],
	[5.4,3.7,1.5,0.2]])
print(" ")
print("The given Original Matrix is")
print(" ")
print(Data)

[m,n] = Data.shape
print(" ")
print("Original Matrix Shape is")
print(" ")
print("m : ", m,' ',"n : ", n)
#U = Data*Data.T(Data)
#print("Original Matrix is Decomposed into U Sigma and V Transpose as ")
#print(" ")
U, s, V = np.linalg.svd(Data)

print(U)
print(U.shape)
print("*"*50)
print("eigen values")
print(s)
print("*"*50)
print(V)
print(V.shape)
#Fill the missing code and print the sizes of U matrix, Sigma matrix and V Tranpose matrix

            





