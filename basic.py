'''
Basic python commands from the python 3.5 documentation pages
'''


#fibonaci numbers
def fib(n):
	'''Returns fibonanci numbers
	
	Expecting for N to be a positive integer. Returns
	a list using appends
	'''
	x, y = 0, 1
	result = []
	while y < n:
		result.append(y)
		#this demonstrates python's multiple assignment
		#the right hand side is evaluated before the 
		#values of the variables are assigned
		x, y = y, x + y 
	
	return result
#demonstrating iterating over a list
words = ['time', 'slime', 'dime', 'crime']

for z in words:
	print(z, len(z))
	
	

#call the fibonaci function
print(fib(1000))


	