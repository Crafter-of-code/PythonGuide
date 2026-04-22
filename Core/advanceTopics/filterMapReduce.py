from functools import reduce
# This file is use to demonstrate Filter Map Reduce
print("Filter Map Reduce demonstraction")
# by defaul if we want to take even number
# the traditional way is
list1 = [2,3,5,10,22,14,15,26]
list1Extention=[]
for i in list1:
	if i%2 == 0:
		list1Extention.append(i)
# print(list1Extention)

# using filter with lamda function
listUsingFilterForEven = list(filter(lambda num: num%2==0,list1))
print(listUsingFilterForEven)
listUsingFilterForOdd = list(filter(lambda num: num%2 != 0,list1))
# print(listUsingFilterForOdd)
# using map
listUsingEvenDouble = list(map(lambda num: num*2,listUsingFilterForEven))
print(listUsingEvenDouble)

# using reduce function
numberUsingEvenReduced = int(reduce(lambda num1,num2:num1+num2,listUsingFilterForEven))
print(numberUsingEvenReduced)

