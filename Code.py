import numpy as np
from numpy import linalg as la
import matplotlib.pyplot as plt
data  = np.array([[10,60,90],[20,50,70],[30,50,40],[20,50,60],[10,60,10]])
print('the matrix is ')
print(data)
print()
mean = np.mean(data.T, axis=1)
print('Mean is ')
print (mean)
Z = data - mean
print ('centerized data' )
print(Z)
print('Covariance Matrix')
COV = np.cov(Z.T,bias='true')
print(COV)
values, vectors = la.eig(COV)
print('eigenvectors')
print(vectors)
print('eigenvalues')
print(values)
print('projected matrix')
P = vectors.T.dot(Z.T)
print(P.T)
print('Scatterplot ')
x=[10,20,30,20,10]
y=[60,50,50,50,60]
z=[90,70,40,60,10]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
