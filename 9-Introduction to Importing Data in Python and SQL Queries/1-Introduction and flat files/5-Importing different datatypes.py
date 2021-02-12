import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("seaslug.txt", delimiter="\t", dtype=str)
print(data[0])

data_float = np.loadtxt("seaslug.txt", delimiter="\t", dtype=float, skiprows=1)
print(data_float[9])

plt.scatter(data_float[:,0], data_float[:,1])
plt.xlabel("Time")
plt.ylabel("percentage of larvae")
plt.show()
