a={"Apple","H","10",20}
b={1,2,3,4,5,6,7,8,9,10}
c={2,4,6,8,10}
Flag=True
while(Flag):
 print("1)Size of set in bytes\n2)Lenght of set\n3)Add element to set\n4)Pop element from set\n5)Intersection of 2 sets\n6)Union of 2 sets\n7)Difference of 2 sets\n8)Symmetric difference of 2 sets\n9)Does set contain this element?\n10)Clearing a set\nPlease select an option.")
 A=input("Enter your choice : ")
 if A=='1':
  print(f"\n\n1)The size of set {a} in bytes is : {a.__sizeof__()}.\n\n")
 elif A=='2':
  print(f"\n\n2)The length of set {c} is : {len(c)}.\n\n")
 elif A=='3':
  print(f"\n\n3)Adding element 101 to set {b} is : {b.add(101)}.\nSet b is {b}.\n\n")
 elif A=='4':
  print(f"\n\n4)The set before pop is {c}.\nNow lets pop an element out  of set : {c.pop()}.\n\n")
 elif A=='5':
  print(f"\n\n5)Set 1 is {b} & set 2 is {c}.Then intersection of both sets is {b.intersection(c)}.\n\n")
 elif A=='6':
  print(f"\n\n6)Set 1 is {b} & set 22 is {c}.Then union of both sets is {b.union(c)}.\n\n")
 elif A=='7':
  print(f"\n\n7)Set 1 is {b} & set 2 is {c}.The difference of both sets is {b-c}.\n\n")
 elif A=='8':
  print(f"\n\n8)Set 1 is {b} & set 2 is {c}.The symmetric difference of both sets is {b^c}.\n\n")
 elif A=='9':
  print(f"\n\n9)Membership of element 10 in set {b} is : {b.__contains__(10)}.\n\n")
 elif A=='10':
  print(f"\n\n10)Clearing the set {c}. {c.clear()}.\nSet c is :{c}\n\n")
 else:
  Flag=False
  print("\n****************************************************************************************\nYou choose none of the options!!!\nExiting the Menu.\n****************************************************************************************")
