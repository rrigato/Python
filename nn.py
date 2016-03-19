'''
Simple Neural Network in python

Where x is hours of sleep and hours of studying 
and y is test score.
'''
import numpy as np

x = np.array(([3,5], [5,1], [10,2]), dtype=float)

y = np.array(([75], [82], [93]), dtype=float)
#scale variables cause each value is positive
x = x/np.amax(x, axis=0)
y = y/ 100 #max score on the test
class Neural_Network(object):
    def __init__(self):        
        #Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 3
        
        #Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)
        
    def forward(self, X):
        #Propagate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3) 
        return yHat
        
    def sigmoid(self, z):
        #Apply sigmoid activation function to scalar, vector, or matrix
        return 1/(1+np.exp(-z))
