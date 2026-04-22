print("this is the global local variable")
a = 13 # this is global variable
def localVariableFunc():
	# a = 12 # this is a local variable
	globals()['a'] = 20
	# suppose we want to change the global variable
	print("inside variable is: ",a)

		# global a #this is how we can use the global variable into the local scope
localVariableFunc()
print("Outside variable: ",a)