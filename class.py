class MyClass:
	"""A Simple Python class."""
	def __init__(self):
		print(self.__doc__)
	def f(self):
		return 'hello world'
	i = 12345
	
	
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance


class CatDog(MyClass, Dog):
	"""Simple example of mulitple inheritance
	
		All methods in python are virtual.This class
		inherits from MyClass and Dog.
	"""
	def __init__(self, height):
		self.height = height
		print("You are {} inches tall".format(self.height))
	
	def meow(self):
		print(self.__doc__)
		
			
x = MyClass()
print(x.f())

myCat = CatDog(25)
#inherited attribute references
print(myCat.f(), myCat.i)

myCat.meow()
