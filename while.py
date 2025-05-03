import random
# numAzar=random.randint(1,10)
# print(numAzar)

## Dado
# import random
# numAzar=random.randit(1,6)
# print(numAzar)

## Necesito al menos 20 puntos para abrir la puerta

# if numAzar>=20:
#     print("Puede pasar")
# else:
#     print("Le falta puntaje")

# Generar un número aleatorio entre 1 y 50
# Pedir al usuario un número
# Si ingresa un número mayor decirle,
# "El número a adivinar es menor"
# Si ingresa un número menor decirle,
# "El número a adivinar es mayor"
# Ej: numeAdivinar=20
# Si ingresa 15 debe decir, "El número a adivinar es mayor"
# Si ingresa 35 debe decir, "El número a adivinar es menor"

## Número a adivinar
# numAdivinar=random.randint(1,50)
# num=int(input("Adivine el número: "))

# while numAdivinar!=num:
#     print(numAdivinar)
#     if num>=numAdivinar:
#         print("El número a adivinar es menor")
#     else:
#         print("El número a adivinar es mayor")
#     num=int(input("Adivine el número: "))
# print("Has adivinado el número")

## Ruleta rusa
# barril=random.randint(1,6)
# rul=int(input("Dispare "))

# while rul!=barril:
#     rul=int(input("Dispare "))
# print("BANG!")

## Casi Ludo
# import time

# meta=30
# turno=1
# j1=0
# j2=0
# while j1<=meta or j2<=meta:
#     if turno % 2==0:
#         print("Turno j1")
#         time.sleep(1)
#         dado=random.randint(1,6)
#         j1+=dado
#         print(f"El j1 saco {dado}")
#         print(f"Avanza hasta la casilla {j1}")
#     else:
#         print("Turno j2")
#         dado=random.randint(1,6)
#         time.sleep(1)
#         j2+=dado
#         print(f"El j1 saco {dado}")
#         print(f"Avanza hasta la casilla {j2}")
#     turno+=1
# if j1>j2:
#     print("El ganador es j1")
# else:
#     print("El gandor es j2")


##Ejercicio de comunas y grupos familiares
# La Florida 20%, la pintana 30%, Puente alto 25%, San joaquin 15%
# Grupo familiar: 1 => 2%, 2 a 4 => 3%, 5 o más => 4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive 
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario y en
# La información dada, calcular su descuento
"""
Ej: 
Ingrese su comuna : La florida 
Ingrese  su grupo familiar (número entero): 4
El total del descuento es 23%
El total a pagar es $154.000
"""

aran=200000
descuento=0

print(""" 
    Comunas 
    1. La Florida 20%
    2. La Pintana 30%
    3. Puente Alto 25%
    4. San Joaquin 15%
    """)
comu=int(input("Seleccione una comuna: "))

if comu==1:
    descuento=20
elif comu==2:
    descuento=30
elif comu==3:
    descuento=25
elif comu==3:
    descuento=15
else:
    print("Selección incorrecta")

grupo=int(input("Ingrese su grupo familiar (número entero usted incluido): "))

if grupo==1:
    descuento+=2
elif grupo<=4 and grupo >=2:
    descuento+=3
elif grupo>=5:
    descuento+=4
else:
    print("Selección incorrecta")

print("El descuento total es ", descuento)
desc=aran*descuento/100
total=aran-desc
print("El total a pagar es $", total)



