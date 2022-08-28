from magic import *


A=Op()
B=Op()
A.get()
B.get()


while True:
 try:
  ch=int(input("\n---------------------Pick the operation to perform---------------------\n1)Press 1 for Addition\n2)Press 2 for Subtraction\n3)Press 3 for Multiplication\n4)Press 4 for floor division\n5)Press 0 to exit\n\n"))
  if ch==1:
   A+B
  elif ch==2:
   A-B
  elif ch==3:
   A*B
  elif ch==4:
   A//B
  elif ch==0:
   break
 except Exception as err:
  print(f"\nAn error has occurred : {err}")
print("\nThe program is completed.")
