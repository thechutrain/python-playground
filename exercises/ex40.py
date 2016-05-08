class ClassExample(object):

	def __init__(self):
		self.name = "example_object"
		self.color = "blue"
		self.number = 4

	def myDetails(self):
		string = "My name is %s and I am %s color, and have the number %d" % (self.name, self.color, self.number)
		print string


example_1 = ClassExample()
example_1.myDetails()
