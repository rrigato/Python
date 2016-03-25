'''
Making A script that is accesible from the command line
'''
import sys

def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

#if the script is called from the command line,
#Get the first arguement after the name of the script
# and pass that into the fib2 function
if __name__ == "__main__":
	print(fib2(int(sys.argv[1])))