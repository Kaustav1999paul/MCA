from multipledispatch import dispatch

@dispatch(bool)
def Hello(a):
 print("\nHey There, Hello!")

@dispatch(str)
def Hello(a):
 print(f"\nHey There, Hello! {a}")

@dispatch(str,int)
def Hello(a,b):
 print(f"\nHey There, Hello!{a}.\nAre you {b}years Old.")

@dispatch(int,int)
def prog(a,b):
 print(f"\nThe sum is {a+b}")

@dispatch(int,str)
def prog(a,b):
 a=str(a)
 print(f"\nThe concantenation is {a+b}")

@dispatch(int,int,int)
def prog(a,b,c):
 print(f"\nThe multipliation is {a*b*c}")

@dispatch(int,float,float)
def prog(a,b,c):
 #a,b,c=float(a),float(b),float(c)
 print(f"\nThe addition is {a+b+c}")

while True:
 i=int(input("\n\n1)Hello Method No parameter\n2)Hello Method with 2 parameters\n3)Hello method with 2 parameters\n4)Program with 2 parameter\n5)Prog with 2 parameter\n6)Program with 3 parameter\n7)Program with 3 parameter\n8)Exit\nEnter the program you wanna run : "))
 if i==1:
  Hello(True)
 elif i==2:
  a=input("\nEnter your name : ")
  Hello(a)
 elif i==3:
  a=input("\nEnter your name : ")
  b=int(input("Enter your age : "))
  Hello(a,b)
 elif i==4:
  a=int(input("\nEnter first number : "))
  b=int(input("Enter second number : "))
  prog(a,b)
 elif i==5:
  a=int(input("\nEnter any number :"))
  b=input("Enter any Text :")
  prog(a,b)
 elif i==6:
  a=int(input("\nEnter first number :"))
  b=int(input("Enter second number :"))
  c=int(input("Enter third number :"))
  prog(a,b,c)
 elif i==7:
  a=int(input("\nEnter an integer number :"))
  b=float(input("Enter a float number :"))
  c=float(input("Enter a float number :"))
  prog(a,b,c)
 elif i==8:
  break

