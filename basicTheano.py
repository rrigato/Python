import theano
import numpy as np

x = theano.tensor.fvector('x')

target = theano.tensor.fscalar('target')

W = theano.shared(np.asarray([0.2, 0.7]), 'W')


y = (x * W).sum()

cost = theano.tensor.sqr(target - y)

gradients = theano.tensor.grad(cost, [W])
W_updated = W - (.1*gradients[0])
updates = [(W, W_updated)]

f = theano.function([x, target], y, updates= updates)

for i in range(10):
	output = f([1.0, 1.0], 20)
	print(output)
