import numpy as np
import matplotlib.pyplot as plt

def plot_lattice(B, size=20):
    a = np.linspace(-size,size, size+1)
    b = np.linspace(-size,size, size+1)
    X,Y = np.meshgrid(a,b)
    for i in range(size+1):
        for j in range(size+1):
            v = np.array([X[i,j], Y[i,j]])
            w = np.dot(B,v)
            plt.scatter(w[0],w[1])
    plt.ylim((-size/2,size/2))
    plt.xlim((-size/2,size/2))
    plt.axhline()
    plt.axvline()
    plt.show()
