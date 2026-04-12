import array
# the small i is use to given that the array is holding the signed integer mean
# the interger is equal to or bigger than zero
arr = array.array("i",[1,2,3,4,5])

for n in arr:
	print(n,end="")
print()

# This is use to add a number in the last of the prgram
arr2 = array.array(arr.typecode,(n for n in arr))
arr.append(77)
arr.reverse();
print(arr.tolist())
print(arr2.tolist())
