 def maneras(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  else:
    return maneras(n-1) + maneras(n-2)

x = int(input("Ingrese la cantidad de metros: "))
print(maneras(x))