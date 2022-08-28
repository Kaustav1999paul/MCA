class student():
 def __init__(self):
  print("-------This is the super class-------")
  self.name=input("\nEnter your name : ")
  self.age=int(input("Enter your age : "))
  self.usn=input("Enter your USN : ")

class derived1(student):
 def __init__(self):
  student.__init__(self)
  print("-------This is the derived class 1-------")
  self.sem=int(input("Enter your semester : "))
  derived1.display(self)

 def display(self):
  print(f"\n\nName : {self.name}")
  print(f"Age : {self.age}")
  print(f"USN : {self.usn}")
  print(f"Semester : {self.sem}")

class marks(derived1):
 def __init__(self):
  derived1.__init__(self)
  print("-------This is the derived class 2 derived from derived class 1-------")
  self.sub1=int(input("\nEnter the marks of Subject 1 : "))
  self.sub2=int(input("\nEnter the marks of Subject 2 : "))
  self.sub3=int(input("\nEnter the marks of Subject 3 : "))
  self.sub4=int(input("\nEnter the marks of Subject 4 : "))
  self.sub5=int(input("\nEnter the marks of Subject 5 : "))
  marks.percentage(self)

 def percentage(self):
  total=self.sub1+self.sub2+self.sub3+self.sub4+self.sub5
  per=(total/250)*100
  print(f"The marks scored are\nSubject 1 : {self.sub1}\nSubject 2 : {self.sub2}\nSubject 3 : {self.sub3}\nSubject 4 : {self.sub4}\nSubject 5 : {self.sub5}")
  print(f"The percentage scored is {per.__round__(2)}")

print("*******Welcome*******")

while True:
 ch=int(input("\n\n1)Just enter student details.\n2)Enter student details and calculate percentage.\n3)Press 0 to Exit.\n\nEnter your choice :  "))
 if ch==1:
  stud=derived1()
 elif ch==2:
  stud=marks()
 elif ch==0:
  break

print("\n\n*******Thank You*******")
