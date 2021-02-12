# Much of the time you will need to import datasets which have different datatypes in different columns;
# one column may contain strings and another floats, for example. The function np.loadtxt() will freak at
# this. There is another function, np.genfromtxt(), which can handle such structures. If we pass
# dtype=None to it, it will figure out what types each column should be.

# Accessing rows and columns of structured arrays is super-intuitive: to get the ith row,
# merely execute data[i] and to get the column with name 'Fare', execute data['Fare'].

import numpy as np

data = np.genfromtxt("titanic.csv", delimiter=",", names=True, dtype=None)
print(data["Survived"][-4:])
