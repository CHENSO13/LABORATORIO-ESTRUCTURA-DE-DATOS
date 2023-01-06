print("Metodo recursivo")
from timeit import default_timer
def fac(n):
    if n<0:
        return "ERROR!"
    if n == 0 or n ==1:
        return 1
    for i in range (1,n):
        n = n*i
    return n
x=int(input("Ingresa un numero: "))
inicio = default_timer()
print(fac(x))
fin =default_timer()
print(fin - inicio)

print("/////////")
def factorial(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *=1
    return resultado
x=int(input("Ingrese un numero: "))
inicio = default_timer()
print(factorial(x))
fin =default_timer()
print(fin - inicio)    

#%%