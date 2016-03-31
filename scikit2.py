from sklearn import datasets, neighbors



import numpy as np
import matplotlib.pyplot as plt
import warnings
import pylab

iris = datasets.load_iris()

print(iris.keys())
print(iris.data.shape)
print(iris.target_names)


X, y = iris.data, iris.target

# create the model
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# fit the model
knn.fit(X, y)

result = knn.predict([[3, 5, 4, 2],])

print(iris.target_names[result])

#predict using knn model
print(knn.predict_proba([[3, 5, 4, 2],]))


np.random.seed(0)
X = np.random.random(size=(20, 1))
y = 3 * X.squeeze() + 2 + np.random.randn(20)

#basic plot
plt.plot(X.squeeze(), y, 'o');
#making the plot actually show up
pylab.show()
