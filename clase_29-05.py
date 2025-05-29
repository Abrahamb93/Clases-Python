'''
Atleta de salto alto
Ingrsese la cantidad de atletas que participaran 
Cada atleta debe hacer un salto alto en el 
rango de 1 Mt y 3.78 metros
los atletas bajo 1.55: no califican 
entre 1.56 y 2 bronce 
entre 2.1 y 3 plata
3.1 y mas adamantium'''
# import random, time
# ncal=0
# bronce=0
# plata=0
# adaman=0
# record=0
# c_atlet=int(input("Ingrese la cantidad de atletas: "))

# for i in range(c_atlet):
#     time.sleep(1)
#     salto=random.uniform(1,3.78)
#     salto=round(salto,2)
#     if salto>record:
#         record=salto
#         print("El record actual es", record)
#     print(f"El atleta {i+1} saltó {salto} metros")
#     if salto<=1.55:
#         print("No clasifica")
#         ncal+=1
#     elif salto>=1.56 and salto <=2:
#         print("Ha obtenido bronce")
#         bronce+=1
#     elif salto>=2.1 and salto<=3:
#         print("Ha obtenido plata")
#         plata+=1
#     else:    
#         print("Ha obtenido adamantium")
#         adaman+=1
# print("Resumen")
# print(f"El el record fue de {record}")
# print("Cantidad de atletas que no clasifican es", ncal)
# print("Cantidad de atletas en categoria Bronce es", bronce)
# print("Cantidad de atletas en categoria Plata es", plata)
# print("Cantidad de atletas en categoria Adamantium es", adaman)

'''
Librería noña 
Crear menú de comics 
1. Comprar
2. Generar boleta
3. Salir 
En la opción de comprar, mostrar los comics con sus precios 
cuando se compra, mostrar la cantidad de articulos que lleva
más el monto neto y monto con IVA
Si ingresa un código de descuento "IAMBATMAN" obtiene 25% 
de descuento al valor neto '''

total = 0
dcto=0
while True:
    try:
        print('''
        Librería Balvoa
        ***************
        1.- Comprar
        2.- Generar boleta
        3.- Salir 
            ''')
        op=int(input("Selecione una opción: "))
        match op:
            case 1:
                while True:
                    try: 
                        print('''
                        Ha seleccionado Comprar
                        1.- Pack de Cartulinas $5000
                        2.- Pack de Lápices de colores $3000
                        3.- Libretas $2000
                        4.- Volver al menú principal''')
                        op2=int(input("Seleccione una opción: "))
                        match op2:
                            case 1:
                                print("Ha selecionado Pack de cartulinas")
                                total+=5000
                            case 2:
                                print("Ha selecionado Pack de lápices de colores")
                                total+=3000
                            case 3:
                                print("Ha selecionado Libretas")
                                total+=2000
                            case 4:
                                print("Volviendo...")
                                break
                            case _:
                                print("opción no válida, intente nuevamente")
                    except Exception:
                        print("Ingrese solo número enteros positivos")
            
            case 2:
                print("Ha seleccionado Generar boleta")
                desc=int(input("Tiene decuento? \n1.- Sí \n2.- No  "))
                
                if desc==1:
                    cod=input("Ingrese código de descuento: ")
                    if cod=="IAMBATMAN":
                        dcto=total*0.25
                        total-=dcto
                        print("Tiene un descuento de", dcto)
                print(f'''
                  Boleta
                ***********
                Subtotal ${total}
                Descuento {dcto}
                Total + IVA {total*1.19}''')
                break
            case 3:
                print("Gracias por su compra")
                break
            case _:
                print("Opción no válida, intente nuevamente")
    except Exception:
        print("Ingrese solo números enteros positivos")

    

