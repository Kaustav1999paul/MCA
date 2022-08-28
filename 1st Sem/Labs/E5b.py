class Student():
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

class Derive1(Student):
	def __init__(self):
		Student.__init__(self)

	total = 0

	def getInfo(self):
		list = []
		for _ in range(5):
			no = int(input("Enter No: "))
			list.append(no)
		for x in list:
			self.total += x

	def display(self):
		print("Total: ", self.total)
		per = (self.total*100)/600
		print("Percent: ", per)

#------------------------------------------------------------

class Derive2(Derive1):
	def __init__(self):
		Derive1.__init__(self)
	def getInfo(self):
		Derive1.getInfo(self)
	def display(self):
		Derive1.display(self)

#------------------------------------------------------------
while True:
        print("1. D1\n2.D2\n3.Exit")
        n = int(input("Enter Option: "))
        if n == 1:
           d1=Derive1()
           d1.getInfo()
           d1.display()
        elif n == 2:
           d2 = Derive2()
           d2.getInfo()
           d2.display()
        elif n == 3:
           exit()
        else:
           break



