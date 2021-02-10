# importing a flat file
# if all the data are numerical numpy array can be used

import numpy as np
import matplotlib.pyplot as plt

digits = np.loadtxt("MNIST.txt", delimiter=",")
print(type(digits))

im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))
plt.imshow(im_sq, cmap="Greys", interpolation="nearest")
plt.show()
