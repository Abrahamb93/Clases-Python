# total=0

# cant=int(input("Ingrese la cantidad de productos: "))

# for i in range(cant):
#     print("""
#         Qué producto llevará?
#         1. Diazepam $9000
#         2. Metametazona $18500
#         3. Oblea China $1000
#         """)
#     op=(int(input("Seleccione una opción: ")))
    
#     if op==1:
#         print("Usted lleva Diazepam")
#         total=total+9000
#     elif op==2:
#         print("Usted lleva Metametazona")
#         total=total+18500
#     elif op==3:
#         print("Usted lleva Oblea China ")
#         total=total+1000
#     else:
#         print("Error, opción no válida")
# print("El total neto es: ", total)
# print("El total + IVA es: ", total*1.19)

## VOTATOON
# Designe 2 candidatos. Pregunte cuántos votantes son
# por cada votante, debe preguntar por quén votará
# cuente la cantidad de votos y muestre los resultados
# definir quén ganó la votación. Considere empate

c1="Shaggy"
c2="Dexter"

cv1=0
cv2=0

cant=int(input("Ingrese la cantidad de votantes: "))

for i in range(cant):
    print(f"Seleccione a su candidato: 1.- {c1}, 2.- {c2}")
    voto=int(input("Selececione una opción: "))

    if voto==1:
        cv1+=1
        #cv1=cv1+1
    else:
        cv2+=1
print(f"La cantidad de votos de {c1} es {cv1}")
print(f"La cantidad de votos de {c2} es {cv2}")

if cv1>cv2:
    print(f"El ganador es {c1}")
elif cv1==cv2:
    print("Los candidatos han empatado")
else:
    print(f"El ganador es {c2}")