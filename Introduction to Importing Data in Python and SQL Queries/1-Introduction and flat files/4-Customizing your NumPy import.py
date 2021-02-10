import numpy as np

data = np.loadtxt("MNIST.txt", delimiter=",", skiprows=1, usecols=[0,2])
print(data)
