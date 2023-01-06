#%%
#recursivo
from timeit import default_timer
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

i = default_timer()

fibonacci = fibo(10)
print('Fibonacci de orden 10:')
print(fibonacci)
f = default_timer()
print(f-i)

#%%
#no recursivo

def fibonacci(n):
    x=1
    y=1
    if n ==1:
        print("0")
    elif n==2:
        print("0","1")
    else:
        print("0")
        print(x)
        print(y)        
        for i in range(n-3):
            total = x+y
            x=y
            x = total
            print(total)
ia = default_timer()
fibonacci(10)
ff = default_timer()
print(ff-ia)            
#%% 