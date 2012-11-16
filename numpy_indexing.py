import numpy as np
import matplotlib.pyplot as plt
#create feature descriptors (e.g., SIFT)
features = np.random.random((1000,128))
#create cluster centers
clusters = np.random.random((50,128))
#compute the pairwise difference
pw_diff = features[:,np.newaxis,:] - clusters[np.newaxis,:,:]
#compute the euclidean distance
pw_dist = np.sqrt((pw_diff * pw_diff).sum(axis=2))
#find the nearest neighbors
nearest_neighbors = np.argmax(pw_dist,axis=1)
#build the histogrma
hist, bin_edges = np.histogram(nearest_neighbors, bins=50, range=(0,50))
#plot the histogram
plt.bar(bin_edges[:-1], hist)