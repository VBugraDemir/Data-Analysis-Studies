# You have just used np.genfromtxt() to import data containing mixed datatypes. There is also another function
# np.recfromcsv() that behaves similarly to np.genfromtxt(), except that its default dtype is None.
# In this exercise, you'll practice using this to achieve the same result. names is set to True as default also.

import numpy as np

d = np.recfromcsv("titanic.csv")
print(d[:3])
