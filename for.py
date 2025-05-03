# Explicación y uso de for

# for i in range(3):
#     print("Hola")

# for i in range(1,6):
#     print(i)

# for i in range(5):
#     print(i+1)

# num=9
# for i in range(1,11):
#     print( num,"x",i,"=",i*num)


# for i in range (1,11):
#     print(f"La tabla del {i}")
#     for j in range(1,11):
#         print( i,"x",j,"=",i*j)

## Ingresar la cantidad de notas y promediar

# cantN=int(input("Ingrese la cantidad de notas: "))
# suma=0

# for i in range(cantN):
#     print(f"Ingrese la nota número {i+1}")
#     nota=float(input())
#     suma=suma+nota
# prom=suma/cantN

# print(f"El promedio es {round(prom,1)}")

# if prom>=4:
#     print("Usted aprobó")
# else:
#     print("Usted reprobó")