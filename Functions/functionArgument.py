print("default arguemnet")
# we a providing default argument if the user do not provide the value in the argument it automatically decide it as zero

def addByDefaultArgument(num1 = 0,num2=0):
	return num1+num2
result = addByDefaultArgument(1);
print(result)

def addByVariableLengthArgument(num1,*num2):
	sum = 0
	sum += num1
	for num in num2:
		sum+=num
	return sum

result = addByVariableLengthArgument(1,2,3)
print(result)

# keyword argument
def printByKeywordArugment(name,age=18):
	print("name is: ",name,end="")
	print(" age is: ",age)

printByKeywordArugment(age=10,name="uzair")


# but suppose if we passing mutiple value in the argument with key value pair
def printByKeyValue(name,**kwrd):
	print("name is: ",name)
	print(kwrd)
	for k,v in kwrd.items():
		print("key: ",k," value: ",v,)

printByKeyValue(name="uzair",age=30,location="noida")