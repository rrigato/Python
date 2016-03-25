import sys

while True:
	try: 
		x = int(input("Please Enter a Number"))
		print('Double your number is:', x*2)
		break
	except (RuntimeError, ValueError):
		print("That was not a number.")

	except:
		print("Unknown Error:", sys.exc_info()[0])
		#forces a specified exception to occur
		raise