#How Do You Handle Exceptions With Try/Except/Finally In Python? 
#Explain with coding snippets.
#----The try block lets you test a block of code for errors. 
# The except block lets you handle the error. 
# The else block lets you execute code when there is no error. 
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# Python code to illustrate
# working of try()
def divide(x, y):
	try:
		result = x // y
		print("Your answer is :", result)
	except ZeroDivisionError:
		print("Sorry ! You are dividing by zero ")

divide(3, 6)
divide(3, 0)
