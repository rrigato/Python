'''
Working with machine learning algorithms in python
'''

#all of the following packages are already installed with anaconda with the 
#exception being seaborn


import scipy
print('scipy:', scipy.__version__)

import matplotlib
print('matplotlib:', matplotlib.__version__)

import urllib.request

import sklearn
print('scikit-learn:', sklearn.__version__)

print(sklearn.__path__)

#conda install seaborn
import seaborn
print('seaborn', seaborn.__version__)

from sklearn.datasets import load_iris
iris = load_iris()



import numpy as np
import matplotlib.pyplot as plt

x_index = 0
y_index = 1

# this formatter will label the colorbar with the correct target names
formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])

plt.scatter(iris.data[:, x_index], iris.data[:, y_index],
            c=iris.target, cmap=plt.cm.get_cmap('RdYlBu', 3))
plt.colorbar(ticks=[0, 1, 2], format=formatter)
plt.clim(-0.5, 2.5)
plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index]);
