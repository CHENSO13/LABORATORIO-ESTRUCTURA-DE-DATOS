#EJERCICIO1

def suma(num1, num2):
    if num1 == 1:
        return num2
    else:
        return num1*num2 + suma(num1 - 1, num2)

x = int(input("ingrese el primer numero: "))
y = int(input("ingrese el segundo numero: "))

print(suma(x,y))



#EJERCICIO2

def convertir(num):
    if num == 0:
        return "0"

    res = num % 16

    if res>=10:
        res = chr(ord("A") + res - 10)

    resultado = convertir(num //16)

    return resultado + str(res)

x = int(input("Ingrese un numero: "))
#para el ejercicio 8642
print(convertir(8642))


#EJERCICIO3 
def convertir(num,base):
    if num == 0:
        return "0"
    residuo = num % base 
    
    rpta = convertir(num // base, base)

    return rpta + str(residuo)

n = int(input("Ingrese el numero: "))
p = int(input("Ingrese la base : "))

print(convertir(n,p))


