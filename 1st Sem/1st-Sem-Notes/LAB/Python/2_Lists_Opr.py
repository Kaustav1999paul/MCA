a=[1,2,3,4,5,6,7,8,9,10]
b=[2,3,4,6,8,10,12]
while(True):
 print("1)Concantinate 2 lists.\n2)Repeating list n number of times\n3)Slicing the list\n4)Range slicing the list\n5)Iterating through the a list\n6)Length of a list\n7)Membership of element in list\n8)Minimum element in a list\n9)Maximum element in a list\n10)Inserting into the list\n")
 A=int(input("Enter your choice : "))
 if A==1:
  print(f"\n\n1)Concantination of {a} and {b} is : {a+b}.\n\n")
 elif A==2:
  print(f"\n\n2)Repetition of list {b} for 3 times is : {b*3}.\n\n")
 elif A==3:
  print(f"\n\n3)Slicing the list {a} is : {a[:5]}\n\n")
 elif A==4:
  print(f"\n\n4)Range slicing the list {a} from 1 to 6 is : {a[1:6]}.\n\n")
 elif A==5:
  print(f"\n\n5)Iterating through list {b} is :")
  for i in b:
   print(i)
 elif A==6:
  print(f"\n\n6)Lenght of list {a} is : {len(a)}.\n\n")
 elif A==7:
  print(f"\n\n7)Is element 10 in list {b} : {10 in b}.\n\n")
 elif A==8:
  print(f"\n\n8)Minimum element of list {a} is : {min(a)}.\n\n")
 elif A==9:
  print(f"\n\n9)Maximum element of list {a} is {max(a)}.\n\n")
 elif A==10:
  print(f"\n\n10)Insertig element 101 into list {b} is {b.insert(1,101)}.\nList is {b}.\n\n")
 else:
  exit()
