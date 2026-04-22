print("To demonstrate high order function")
def square(num):
	return num*num
def operation(num,operation):
	return operation(num)
val = 10
result = operation(10,square)
print(result)