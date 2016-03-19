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
	def _init_(self):
	#define hyperparameters= parameters that do not change
	self.inputLayerSize = 2
	self.outputLayerSize = 1
	self.hiddenLayerSize = 3
	
	def forward(self, x):
	#propogate inputs through the network
	