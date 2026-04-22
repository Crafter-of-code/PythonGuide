print("this is the file to show init method");
class customGreeting:

	def greeting(self):
		print("hello",self.name)
	def __init__(self,name):
		self.name = name

grt = customGreeting("zeno")
grt.greeting()
