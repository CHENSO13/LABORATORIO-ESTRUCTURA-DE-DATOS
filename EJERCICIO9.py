def suma(a,b):
    if a == 0 or b ==0:
        return 0
    elif a == 1 or b == 1:
        return (a+("1"))
    elif a == 2 or b == 2:
        return (a+("1+1"))
    else:
        return suma(a+b) + suma(a+b)
x = int(input("Sumar: "))
y = int(input("Sumando: "))

print(suma(x,y))
        
    
    