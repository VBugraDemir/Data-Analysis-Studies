import h5py
import numpy as np
import matplotlib.pyplot as plt

file = "L-L1_LOSC_4_V1-1126259446-32.hdf5"

data = h5py.File(file, "r")

group = data["strain"]
for key in group.keys():
    print(key)

strain = data["strain"]["Strain"][()] # it was actually .value instead of [()] on datacamp but it has been changed.

num_samples = 10000
time = np.arange(0, 1, 1/num_samples)

plt.plot(time, strain[:num_samples])
plt.xlabel("GPS time (s)")
plt.ylabel("strain")
plt.show()
