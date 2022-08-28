class operation:
	def __init__(self):
		self.list = []
		self.no = 0

	def __add__(self, others):
		add_list = []
		zip_list = zip(self.list, others.list)
		for i in zip_list:
			add_list.append(i[0] + i[1])
		print(add_list)

	def __sub__(self, others): 
        sub_list = []
        zip_list = zip(self.list, others.list)
        for i in zip_list:
            sub_list.append(i[0] - i[1])
        print(sub_list)

    def __floordiv__(self, others): 
                div_list = []
                zip_list = zip(self.list, others.list)
                for i in zip_list:
                        div_list.append(i[0]//i[1])
                print(div_list)

	def __mul__(self, others): 
                mul_list = []
                zip_list = zip(self.list, others.list)
                for i in zip_list:
                        mul_list.append(i[0] * i[1])
                print(mul_list)


	def listAdd(self, n):
		if n != 4:
			self.no = int(input("Enter the size of list: "))
			for _ in range(self.no):
				self.list.append(int(input("Enter the element: ")))
			print(self.list)
		else:
			# For Division
			self.no = int(input("Enter the size of list: "))
        	for _ in range(self.no):
				j = int(input("Enter the element: "))
				if j != 0:
                	self.list.append(j)
				else:
					self.list.append(j+1)
					print("0 not allowed")

