import scipy.io
import numpy as np
import matplotlib.pyplot as plt

mat = scipy.io.loadmat("ja_data2.mat")
print(type(mat))
print()
print(mat.keys())
print()
print(type(mat["CYratioCyt"]))
print()
print(np.shape(mat["CYratioCyt"]))

data = mat["CYratioCyt"][25,5:]
fig = plt.figure()  # can be commented out
plt.plot(data)
plt.xlabel("time (min.)")
plt.ylabel("normalized fluorescence measure of expression")
plt.show()
# fig, ax = plt.subplots()
# ax.plot(data)
# ax.set_xlabel("time (min.)")
# ax.set_ylabel("normalized fluorescence measure of expression")
# plt.show()