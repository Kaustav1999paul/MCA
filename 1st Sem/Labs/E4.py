from operation import*

obj1 = operation()
obj2 = operation()

print("__MENU__")
print("1: Add")
print("2: Sub")
print("3: Mul")
print("4: Div")
print("5: Exit")

n = int(input("Enter option no: "))

obj1.listAdd(n)
obj2.listAdd(n)

while(n != 5):
	print("1: Add")
	print("2: Sub")
	print("3: Mul")
	print("4: Div")
	print("5: Exit")

	if(n == 1):
		obj1+obj2
	elif(n == 2):
		obj1-obj2
	elif(n == 3):
		obj1*obj2
	elif(n == 4):
		obj1//obj2
	elif(n == 5):
		break
	else:
		print("Not a valid Input.")

	n = int(input("Enter option no: "))
