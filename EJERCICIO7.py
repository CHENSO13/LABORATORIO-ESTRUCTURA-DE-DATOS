def maneras(n):
  if n == 0:
    return 1
  elif n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return maneras(n-1) + maneras(n-2) + maneras(n-3)

x = int(input("Ingrese la cantidad de metros: "))
print(maneras(x))