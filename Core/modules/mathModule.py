import math
from math import ceil,floor
def getSquareRoot(x):
	return math.sqrt(x);
##
def getSquare(x):
	return math.pow(x,2)
##
def getCiel(x):
	return ceil(x)

def getFloor(x):
	return floor(x);

##
result = getSquareRoot(10)
rootResult = getSquare(10)
cielResult = getCiel(10.5)
floorResult = getFloor(10.9)
print(result)
print(rootResult)
print(cielResult)
print(floorResult)