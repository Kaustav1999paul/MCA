d=dict()
class employee():
    def input(self):
        self.name=input("Enter the employee name : ")
        self.address=("Enter the employee address : ")
        self.pan=input("Enter the employee PAN details : ")
        self.basicPay=int(input("Enter the basic pay : "))
        self.deduct=int(input("Enter the deductions : ")) 
        self.hra=self.basicPay*1.02
        self.da=self.basicPay*0.25
        self.grossPay=self.basicPay+self.hra+self.da
        self.netPay=self.grossPay - self.deduct
        self.update()

    def update(self):
        d.update({self.name:{
            "Name" : self.name,
            "Address" : self.address,
            "PAN" : self.pan,
            "Basic Pay":self.basicPay,
            "Deductions":self.deduct,
            "HRA":self.hra,
            "DA":self.da,
            "GrossPay":self.grossPay,
            "Salary":self.netPay
        }})

    def printe(self):
        for key in d:
            print(key,d[key])

    def search(self,name):
        flag=0
        for key in d:
            if key==name:
                print("Found")
                flag=1
                for i in d[key]:
                    print(i,d[key][i])
        if flag==0:
            print("Not Found")

em=employee()
while 1:
    print("1.Enter Employee Details\n2.Display All Employees\n3.Search an Employee\nPress 0 to Exit")
    ch=int(input("Enter your choice : "))
    if ch==1:
        em.input()
    if ch==2:
        em.printe()
    if ch==3:
        name=input("Enter name : ")
        em.search(name)
    if ch==0:
        break