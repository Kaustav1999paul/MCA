class student():
 def __init__(self):
  print("-------This is the super class-------")
  self.name=input("\nEnter your name : ")
  self.age=int(input("Enter your age : "))
  self.usn=input("Enter your USN : ")

class ugstudent(student):
 def __init__(self):
  student.__init__(self)
  print("-------This is the derived class 1-------")
  self.sem=int(input("Enter your semester : "))
  self.fee=int(input("Enter your fee : "))
  self.stipend=int(input("Enter the stipend : "))
  ugstudent.display(self)

 def display(self):
  print(f"\n\nName : {self.name}")
  print(f"Age : {self.age}")
  print(f"USN : {self.usn}")
  print(f"Semester : {self.sem}")
  print(f"Fees : {self.fee}")
  print(f"Stipend : {self.stipend}")

class pgstudent(student): 
 def __init__(self):
  student.__init__(self)
  print("-------This is the derived class 2-------")
  self.sem=int(input("Enter your semester : "))
  self.fee=int(input("Enter your fee : "))
  self.stipend=int(input("Enter the stipend : "))
  ugstudent.display(self)

 def display(self):
  print(f"\n\nName : {self.name}")
  print(f"Age : {self.age}")
  print(f"USN : {self.usn}")
  print(f"Semester : {self.sem}")
  print(f"Fees : {self.fee}")
  print(f"Stipend : {self.stipend}")

print("\n*******Welcome*******\n")
while True:
 ch=int(input("\n\n1)UG Student Details.\n2)PG Student Details.\n3)Press 0 to Exit.\nEnter your choice : "))
 if ch==1:
  ug=ugstudent()
 elif ch==2:
  pg=pgstudent()
 elif ch==0:
  break

print("\n\n*******Thank You*******")
