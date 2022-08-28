class Student:
	def __init__(self):
		self.name = str(input("Enter Name: "))
		self.usn = str(input("Enter USN: "))
		self.age = int(input("Enter Age: "))

	def display(self):
		print("Super Class")
		print("-----------")
		print("Name: ", self.name)
		print("USN: ", self.usn)
		print("Age: ", self.age)
		print("-----------")

#-------------------------------------------------------------------

class UGStudent(Student):
	def __init__(self):
		Student.__init__(self)
		self.course = str(input("Enter Course: "))
		self.years = int(input("Enter Years: "))

	def displayUG(self):
		Student.display(self)
		print("Course: ", self.course)
		print("Years: ", self.years)

#-------------------------------------------------------------------

class PGStudent(Student):
	def __init__(self):
		Student.__init__(self)
		self.course = str(input("Enter Course: "))
		self.years = int(input("Enter Years: "))

	def displayPG(self):
		Student.display(self)
		print("Course: ", self.course)
		print("Years: ", self.years)
#------------------------------------------------------------------

while True:
	print("1. UG\n2.PG\n3.Exit")
	n = int(input("Enter Option: "))

	if n == 1:
		ug = UGStudent()
		ug.displayUG()
	elif n == 2:
		pg = PGStudent()
		pg.displayPG()
	elif n == 3:
		exit()
	else:
		break

#------------------------------------------------------

