print("this is the recurssion program")
def recursionFunc(num):
	if num == 1:
		return 1
	return num * recursionFunc(num-1)

print(recursionFunc(5))