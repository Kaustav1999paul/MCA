import time

def timeit(func):
    def timed(*args, **kw):
        print("")
        print("--------------Before the Timeit decorator-----------------")
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        minutes, seconds = divmod((te-ts), 60)
        print(minutes,"  ",seconds)
        print("time taken %8.2f"%((te-ts)*10**6))
        print("--------------After the Timeit decorator------------------")
        print("")
        return result
    return timed

#---------------------------------------------------------
@timeit
def fib():
    a,b=0,1
    while(1):
        yield a
        a, b=b ,a+b
#---------------------------------------------------------
print("")
num = int(input("Enter the size for fibonacci series: "))
if num < 0:
     print("---------------------Invalid number-------------------")
fibonacci = fib()

for x in range(num):
    print(next(fibonacci))

