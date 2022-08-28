#decorator and genrators
from time import time
def calc_time(fn):
    def wrapper(*ar,**kw):
        t1=time()
        result=fn(*ar,**kw)
        t2=time()
        t=(t2-t1)*1000
        print(f"this is time taken to passed an object in function : {t}")
        return result
    return wrapper

@calc_time
def fib(num):
    a=0
    b=1
    for _ in range(0,num):
        yield a
        a,b=b,a+b


n=int(input("enter the n : "))
for x in fib(n):
    print(x)


