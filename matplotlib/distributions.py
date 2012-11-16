import numpy as np
import matplotlib.pyplot as plt

plt.ion()

X = np.random.randn(5000*2).reshape((5,1000,2)) * 0.3

means = np.array([[0,0],[1,1],[1,0],[0,1],[0.5,0.5]])

X = X + means[:,np.newaxis,:]

colors = 'rgbmy'

for x, color in zip(X, colors):
    plt.plot(x[:,0], x[:,1], 'o', markerfacecolor=color, alpha=0.3)

plt.xlim([-1,2])
plt.ylim([-1,2])