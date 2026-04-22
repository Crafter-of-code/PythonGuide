# there are three type of method
# 1: class method: this type of method works with class variable
# 2: instance method: this type of method workds with instance variable
# 3: static method: this type of method works with static variable
print("hello world");
class typesOfMethodClass:
	classNumber = "this is my class number"
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def getName(self):
		return self.name
	@classmethod
	def getClassNumber(self,cls):
		return cls.classNumber
	@staticmethod
	def operationMethod(self,value):
		return (value*2)

tpMthdClass = typesOfMethodClass("uzair",20)
name = tpMthdClass.getName()
operation = tpMthdClass.operationMethod(4)
classNUmber = tpMthdClass.getClassNumber(typesOfMethodClass)
print("name is: ",name," ","operation: ",operation)
print(classNUmber)