def myDec(func):
	def wrap(num1,num2):
		if num1<num2:
			num1,num2 = num2,num1
		return func(num1,num2)
	return wrap
@myDec
def divide(num1,num2):
	return num1/num2
result = divide(2,5)
print(result)