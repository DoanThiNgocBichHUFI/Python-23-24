# k-mean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
%matplotlib inline

X= -2 * np.random.rand(200,2)
X1 = 1 + 2 * np.random.rand(100,2)
X[100:200, :] = X1
plt.scatter(X[ : , 0], X[ :, 1], s = 50, c = 'b')
plt.show()

Kmean = KMeans(n_clusters=2)
Kmean.fit(X)

print(Kmean.cluster_centers_)

plt.scatter(X[ : , 0], X[ : , 1], s =50, c='b')
plt.scatter(Kmean.cluster_centers_[0][0], Kmean.cluster_centers_[0][1], s=100, c='g', marker='s')
plt.scatter(Kmean.cluster_centers_[1][0], Kmean.cluster_centers_[1][1], s=100, c='r', marker='s')
plt.show()

print(Kmean.labels_)

