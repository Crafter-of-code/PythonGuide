print("This is factorial program ")
def fact(num):
	mul = 1
	while(num>=1):
		mul*=num
		num-=1
	return mul
def factUsingFor(num):
	mul = 1
	for num in range(1,num+1):
		mul*=num
	return mul

# factorialResult = fact(5)
factorailResultByUsingFor = factUsingFor(5)
print(factorailResultByUsingFor)

