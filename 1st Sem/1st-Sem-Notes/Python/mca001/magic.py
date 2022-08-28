class Op:
 def __init__(self):
  self.L1=[]
 
 def get(self):
  n=int(input("\nEnter the size of the list : "))
  for i in range(n):
   self.L1.append(int(input(f"\nEnter the element {i+1} : ")))
  print(f"\nThe list is : {self.L1}")

 def __add__(self,other):
  newlist=[]
  for i in range(len(self.L1)):
   newlist.append(self.L1[i]+other.L1[i])
  print(f"\nThe List after addition is {newlist}")

 def __sub__(self,other):
  newlist=[]
  for i in range(len(self.L1)):
   newlist.append(self.L1[i]-other.L1[i])
  print(f"\nThe List after subtraction is {newlist}")

 def __mul__(self,other):
  newlist=[]
  for i in range(len(self.L1)):
   newlist.append(self.L1[i]*other.L1[i])
  print(f"\nThe List after multiplication is {newlist}")

 def __floordiv__(self,other):
  newlist=[]
  for i in range(len(self.L1)):
   newlist.append(self.L1[i]//other.L1[i])
  print(f"\nThe List after floor division is {newlist}")

