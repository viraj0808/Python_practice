#How to Define a Class in Python? What Is Self? 
#---A class in Python can be defined using the class keyword. As per the syntax above, a class is defined using the class keyword followed by the class name and : operator after the class name,
#which allows you to continue in the next indented line to define class members.
#Give An Example Of A Python Class
class Person:
	def __init__(self, name):
		self.name = name
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('viraj')
p.say_hi()
