class ABC:
	def Hello(self, a=None, b=None):
		if a!=None and b!=None:
			print("----------------------------")
			print("O/P:  Hello ",a,"of age ",b)
			print("----------------------------")
		elif a!=None:
			print("-----------------")
			print("O/P:  Hello ", a)
			print("-----------------")
		else:
			print("-------------")
			print("O/P:  Hello")
			print("-------------")

#----------------------------------------------------------------------

s1 = ABC()
stt = str(input("Enter Name: "))
age = str(input("Enter Age: "))

#----------------------------------------------------------------------

while True:
	print("MENU")
	print("1. 0 parameter\n2. 1 parameter\n3. 2 parameter\n4. EXIT")
	n = int(input("Enter option: "))

	if n == 1:
		s1.Hello()
	elif n == 2:
		s1.Hello(stt)
	elif n == 3:
		s1.Hello(stt,age)
	elif n == 4:
		exit()
	else:
		break

#---------------------------------------------------------------------
