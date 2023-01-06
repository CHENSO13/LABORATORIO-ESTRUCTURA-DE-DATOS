array = []
tamaño = int(input("Defina el tamaño del Array:"))
funcion = int(input("Ingrese una funcion: "))
a = 0
for n in range(tamaño):
    a = 3*a
    array.append(funcion*3)
    
print(array)