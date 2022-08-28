def Reverse():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 if (not(S)) or (not(s)):
  print("\nEMPTY STRINGS!\nPlease Enter both the strings!!!")
 else: 
  print(f"\nThe string 1 {S} reversed is {S[::-1]}")
  print(f"\n1)The string {s} reversed is {s[::-1]}")

def Uppercase():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 if (not(S)) or (not(s)):
  print("\nEMPTY STRINGS!\nPlease Enter both the strings!!!")
 elif s.isalnum() or S.isalnum():
  print("\nEnter String without numeric characters")
 else : 
  print(f"The string 1 {S} in upper case is : {S.upper()}")
  print(f"The string 2 {s} in upper case is : {s.upper()}")

def Lowercase():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 print(f"The string 1 {S} in lower case is : {S.lower()}")
 print(f"The string 2 {s} in lower case is : {s.lower()}")

def Title():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 print(f"The string 1 {S} in title form is : {S.title()}")
 print(f"The string 2 {s} in title form is : {s.title()}")

def IsUpper():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 print(f"Is the string 1 {S} completly in upper case : {S.isupper()}")
 print(f"Is the string 2 {s} completly in upper case : {s.isupper()}")

def IsLower():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 print(f"Is the string 1 {S} completly in lower case : {S.islower()}")
 print(f"Is the string 2 {s} completly in lower case : {s.islower()}")

def Join():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 print(f"Lets join String 1 {S} with each letter of string 2 {s} in between : {S.join(s)}")

def Replace():
 S=input("Enter the String : ")
 a=input("Enter the element you want to replace : ")
 b=input("Enter the elemene you want to replace it with : ")
 print(f'Lets replace {a} with {b} in string {S} : {S.replace(a,b)}')

def Swapcase():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 print(f"Lets Swapcase of string 1 {S} : {S.swapcase()}")
 print(f"Lets swapcase of string 2 {s} : {s.swapcase()}")

def Casefold():
 S=input("Enter the 1st String : ")
 s=input("Enter the 2nd String : ")
 print(f"Casefold of string 1 {S} is : {S.casefold()}")
 print(f"Casefold of string 2 {s} is : {s.casefold()}")

def fIndex():
 S=input("Enter the 1st String : ")
 print(f"The string is {S}")
 a=input("Enter the element of which you need the index : ")
 print(f'Lets find index of {a} in string {S} : {S.find(a)}')

def Slice():
 S=input("Enter the 1st String : ")
 print(f"The string is {S}")
 print("Enter the start and end range where you wish to slice the string : ")
 a=int(input())
 b=int(input())
 print(f'Lets slice the string {S} fromr {a} to {b} : {S[a:b]}')

while True:
 ch=int(input("\n-------------Enter your choice-------------\n1)Reverse\n2)Uppercase\n3)Lowercase()\n4)Title\n5)Is Upper?\n6)Is Lower?\n7)Join\n8)Replace\n9)Swapcase\n10)Casefold\n11)find index of element\n12)Slicing\n13)Press 0 to Exit\n\n"))
 if ch==1:
  Reverse()
 elif ch==2:
  Uppercase()
 elif ch==3:
  Lowercase()
 elif ch==4:
  Title()
 elif ch==5:
  IsUpper()
 elif ch==6:
  IsLower()
 elif ch==7:
  Join()
 elif ch==8:
  Replace()
 elif ch==9:
  Swapcase()
 elif ch==10:
  Casefold()
 elif ch==11:
  fIndex()
 elif ch==12:
  Slice()
 elif ch==0:
  break
