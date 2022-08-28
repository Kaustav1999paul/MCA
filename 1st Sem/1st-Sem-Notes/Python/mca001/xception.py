print("1.ValueError")
print("2.FileNotFoundError")
print("3.TypeError")
print("4.IOError")
print("5.NameError")


while True:
    ch=int(input("enter the choicce : "))
    if ch==1:
        try:
            f=open("f1.txt",'z')
            print("sucess")
        except ValueError as e:
            print("Value Error")
            print(e)
    elif ch==2:
        try:
            f=open("f9.txt",'r')
            print("sucess")
        except FileNotFoundError as e:
            print("file not found error")
            print(e)
    elif ch==3:
        try:
            f=open("f1.txt",'r','w')
            print("sucess")
        except TypeError as e:
            print("Type error")
            print(e)
    elif ch==4:
        try:
            f = open('f3', 'w+')
            f.write("Hello")
            f2 = open('f2', 'r')
            print("Success")
        except IOError as e:
            print("file not found")
            print(e) 
    elif ch==5:
        try:
            f=open("f1.txt",'r')
            print('sucess')
        except NameError as e:
            print("NAme ERROR") 
            print(e)   
    else:
        break