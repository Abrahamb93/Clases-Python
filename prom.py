## Ingresar 3 números y ver el mayor de ellos
## Ingresar 3 números y promediarlos 

# n1=int(input("Ingrese un número: "))
# n2=int(input("Ingrese otro número: "))
# n3=int(input("Ingrese otro número: "))

# m=max(n1,n2,n3)
# print(f"El número mayor es: {m}")
# if n1>n2 and n1>n3:
#     print(f"El número mayor es: {n1}")
# elif n2>n3:
#     print(f"El número mayor es: {n2}")
# else:
#     print(f"El número mayor es: {n3}")

n1=int(input("Ingrese un número: "))
n2=int(input("Ingrese otro número: "))
n3=int(input("Ingrese otro número: "))

prom=(n1+n2+n3)/3

print(f"El promedio es {round(prom)}")
print(f"El promedio es {round(prom, 2)}")