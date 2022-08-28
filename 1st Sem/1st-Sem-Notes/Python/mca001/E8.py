while True:
	print(".......OPTIONS......")
	print("1. Value Error")
	print("2. File Not Found")
	print("3. Type Error")
	print("4. Name Error")
	print("5. IO Error")
	print("6. Exit")
	print("....................")

	n = int(input("Enter Option: "))
	if n == 1:
		try:
			f = open('f1.txt', 'z')
			print("Success")
		except ValueError:
			print("Value Error")
	elif n == 2:
		try:
			f = open('f9.txt', 'r')
			print("Success")
		except FileNotFoundError:
			print("File Not Found")
	elif n == 3:
		try:
			f = open('f1.txt', 'r',"w")
			print("Success")
		except TypeError:
			print("Type Error")
	elif n == 4:
		try:
			f = open('f1.txt', 'z')
			print("Success")
		except ValueError:
			print("Name Error")
	elif n == 5:
		try:
			f = open('f2', 'w+')
			f.write("Hello")
			f2 = open('f2', 'r')
			print("Success")
		except IOError:
			print("IOError")
	elif n == 6:
		exit()
	else:
		break
