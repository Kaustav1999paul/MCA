while True:
 print("1)ValueError\n2)FileNotFoundError\n3)TypeError\n4)IOError\n5)NameError\n6)Press 0 to exit\n")
 ch=int(input("Enter your choice : "))
 if ch==0:
  break
 elif ch==1:
  try:
   f=open("file1.txt",'z')
   print("Success!!")
  except ValueError as e:
   print(f"\nValue Error has occurred\nError Message : {e}\n")
  finally:
   f.close()
   print("Successfully Closed the file\n")
 elif ch==2:
  try:
   f=open("file1.txt",'r')
   print("Success")
  except FileNotFoundError as e:
   print(f"\nFileNotFoundError has occurred\nError Message : {e}\n")
  finally:
   f.close()
   print("Successfully Closed the file\n")
 elif ch==3:
  try:
   f=open("file1.txt",'r','w')
   print("Success!!")
  except TypeError as e:
   print(f"\nTypeError has occurred\nError Message : {e}\n")
  finally:
   f.close()
   print("Successfully Closed the file\n")
 elif ch==4:
  try:
   f=open("file1.txt",'r')
   print("Success!!")
  except IOError as e:
   print(f"\nIOError has occurred\nError Message : {e}\n")
  finally:
   f.close()
   print("Successfully Closed the file\n")
 elif ch==5:
  try:
   f=open("file1.txt",'r')
   print("Success!!")
  except NameError as e:
   print(f"\nNameError has occurred\nError Message : {e}\n")
  finally:
   f.close()
   print("Successfully Closed the file\n")

