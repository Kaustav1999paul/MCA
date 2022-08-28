class Employee:
	def __init__(self):
		self.name = input("Enter Name: ")
		self.USN = input("Enter USN: ")
		self.pay = int(input("Enter Pay: "))
	def display(self):
		print("---------------------")
		print("Name: ", self.name)
		print("USN: ", self.USN)
		print("Pay: ", self.pay)
		print("---------------------")
	def promotion(self):
		increase = 1.5
		self.pay = float(self.pay*increase)

class Developer(Employee):
	def promotion(self):
		increase = 2.5
		self.pay = float(self.pay * increase)

class Manager(Employee):
	def promotion(self):
		increase = 3.5
		self.pay = float(self.pay * increase)


e1 = Developer()
e2 = Manager()

e1.promotion()
e2.promotion()

e1.display()
e2.display()
