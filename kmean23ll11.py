from sklearn.datasets import make_blobs

# create a dataset of 200 samples
# and 5 clusters
features, labels = make_blobs(
    n_samples=200,
    centers=5
)
from sklearn.cluster import KMeans

# Instanciate the model with 5 'K' clusters
# and 10 iterations with different
# centroid seed 
model = KMeans(
    n_clusters=5,
    n_init=10,
    random_state=42
    )

# train the model
model.fit(features)

# make a prediction on the data
p_labels = model.predict(features)

import matplotlib.pyplot as plt
plt.style.use('default')

X = features[:,0]
y = features[:,1]

plt.scatter(X, y, c=p_labels, alpha=0.8)

cluster_centers = model.cluster_centers_
cs_x = cluster_centers[:,0]
cs_y = cluster_centers[:,1]

plt.scatter(cs_x, cs_y, marker='*', s=100, c='r')
plt.title('KMeans')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

ks = range(1, 10)

ssr = []
# For each cluster K
for k in ks:
    # create model instance of K clusters
    model = KMeans(n_clusters=k)

    # fit the model
    model.fit(features)

    # append the inertial to a list
    ssr.append(model.inertia_)
    
# Plot
plt.plot(ks, ssr, '-o')
plt.xlabel('Clusters (k)')
plt.ylabel('SSR')
plt.xticks(ks)
plt.title('Elbow method for optimal K')
plt.axvline(x=5,linestyle='--',c='grey')
plt.show()
