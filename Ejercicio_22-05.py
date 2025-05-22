# Perros de caza 
# Pida al usuariola cantidad de perros 
# Muestre cual es la cuota minima de conejos
# Luego consulte cuantos conejs trajo 
# Si el perro trajo la cantidad minima 
# cumplio la cuota, sino, se queda sin filete
# mostrar resumen de perro que cumplieron y los que no

# import random
# import time
# cuota=4
# pcum=0
# conejt=0
# while True:
#     try: 
#         cperros = int(input("Ingrese la cantidad de perros : "))
#         break
#     except Exception:
#         print("Solo se permiten números enteros")
# for i in range(cperros):
#     time.sleep(1)
#     conejos=random.randint(0,7)
#     conejt+=conejos
#     print(f"¿Cuánto conejos trajo el perro {i+1}? ")
#     print(f"El perro {i+1} trajo {conejos} conejos")
#     if conejos>=cuota:
#         print("El perro tiene filete")
#         pcum+=1
#     else:
#         print("El perro se queda sin filete")
# print(f'''
# Resumen:
# La cantidad de perros que cumplieron fue {pcum}
# La cantidad de perros que no cumplieron fue {cperros-pcum}
# La cantidad de conejos totales fue de {conejt}
# ''')

# while True:
#     try:
#         op=int(input("Ingrese un número: "))
#         break
#     except Exception:
#         print("Solo se permiten números enteros")

''' 
Quiere pasar el ramo?
Pregunte la cantidad de rojos en el curso 
los talleres que hay en el semestre son 4
Por cada taller asistido obtiene 0.3 décimas 
Si el alumno tiene más de 1 punto
tiene la bendición del profesor 
sino, no se le puede ayudar
ingrese la nota final y sume las decimas acomuladas 
Muestre si aprueba o reprueba
'''
import random
cantAR=int(input("Ingrese la cantidad de alumnos con nota roja: "))
talleres=4

for al in range(cantAR):
    deci=0
    for t in range(talleres):
        print(f"El alumno aisitió al taller {t+1}? ")    
        resp=random.randint(1,2)
        if resp==1:
            deci+=0.3
        if deci>=1:
            print("Tiene la bedición del profesor")
        else:
            print("No recibe ayuda")
    nt=float(input("Cuál es la nota final? "))
    print("Sus décimas totales fueron", deci) 
    nt+=deci
    if nt>=4:
        print("El alumno aprobó")
    else:
        print("El alumno reprobó")



