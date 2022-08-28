class A:
	def __init__(self):
		self.name = input("Enter Name: ")
		self.age = input("Enter Age: ")
		self.basicPay = input("Enter Basic Pay: ")
		self.HRA = input("Enter HRA: ")
		self.DA = input("Enter DA: ")
		self.Deduct = input("Enter Deduct: ")

# Create an onject of the class
obj = A()
dictionary = obj.__dict__

print(dictionary)
