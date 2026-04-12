data = [1,2,3,4,5,6]
data2= list(range(10,21));
print(data2)
print(type(data2))
# printin data by using for loop
print("by using for loop")
for value in data:
	print(value," ",end="")
print()
#
## --
#
divider = 0
while(divider<30):
	print("-",end="")
	divider+=1
print()
# printing data by using while loop
index = 0;
while(index<len(data)):
	print(data[index]," ",end="")
	index+=1;
print()
print("this index value now is:", index)
#
## --
#
divider = 0
while(divider<30):
	print("-",end="")
	divider+=1
print()
# binary search code below
low = 0
high = len(data2)
target = 13
while(low<=high):
	mid = int(low+(high-low)/2)
	if(data2[mid] == target):
		print(mid)
		break
	elif(data2[mid]>target):
		# go left
		high = mid-1
	else:
		low = mid+1