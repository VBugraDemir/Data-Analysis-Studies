# it is a hierarchical data format. It can be explored by using the method keys of dictionaries.
# Strain is the data of interest

import h5py

file = "L-L1_LOSC_4_V1-1126259446-32.hdf5"

data = h5py.File(file, "r")
print(type(data))

for key in data.keys():
    print(key)
# print(data["meta"]["UTCstart"][()])