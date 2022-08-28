class Employee():
 r=1.3
 def __init__(self):
  self.fname=input("\nEnter the first name : ")
  self.lname=input("Enter the last name : ")
  self.empID=input("Enter employee ID : ")
  self.pay=int(input("Enter the salary : "))

 def display(self):
  print(f"\nName :{self.fname} {self.lname} ")
  print(f"Employee ID : {self.empID}")
  print(f"Salary : {self.pay}")

 def increase(self):
  self.pay=int(self.pay*r)

class Developer(Employee):
 def increase(self):
  r=1.8
  print(f"\n---------Salary increased by {r}---------")
  self.pay=int(self.pay*r)

class Manager(Employee):
 def increase(self):
  r=3
  print(f"\n---------Salary increased by {r}---------")
  self.pay=int(self.pay*r)


E1=Developer()
E2=Manager()
E1.increase()
E2.increase()
E1.display()
E2.display()
