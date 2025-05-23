# # Crear menú con categorias
# cantAr = 0
# total = 0
# while True:
    # while True:
    #     try:
    #         print('''
    #         Selecione una opción:
    #         1.- Teclados
    #         2.- Monitores
    #         3.- Audifonos
    #         4.- Pagar
    #         5.- Salir
    #             ''')
    #         op=int(input())
    #         break
    #     except Exception:
    #         print("Ingrese solo números enteros")
    # match op:
    #     case 1:
    #         while True:
    #             print('''
    #             Seleccione una opción:
    #             1.- Teclado de manco $20.000
    #             2.- Teclado de Gamer $40.000
    #             3.- Teclado normal y aburrido $8.000
    #             4.- Volver al menú principal
    #                 ''')
    #             op=int(input())
    #             match op:
    #                 case 1:
    #                     total+=20000
    #                     cantAr+=1
    #                 case 2:
    #                     total+=40000
    #                     cantAr+=1
    #                 case 3:
    #                     total+=8000
    #                     cantAr+=1
    #                 case 4:
    #                     break
    #                 case _:
    #                     print("Opción no válida.")
    #             print(f"Articulo agregado al carro, lleva {cantAr} en total")
    #             print(f"El total pacial es ${total}")
    #     case 2:
    #         while True:
    #             print('''
    #             Seleccione una opción:
    #             1.- Monitor Xth67cv $200.000
    #             2.- Monitor $140.000
    #             3.- Monitor $8.000
    #             4.- Volver al menú principal
    #                 ''')
    #             op=int(input())
    #             match op:
    #                 case 1:
    #                     total+=200000
    #                     cantAr+=1
    #                 case 2:
    #                     total+=140000
    #                     cantAr+=1
    #                 case 3:
    #                     total+=8000
    #                     cantAr+=1
    #                 case 4:
    #                     break
    #                 case _:
    #                     print("Opción no válida.")
    #             print(f"Articulo agregado al carro, lleva {cantAr} en total")
    #             print(f"El total pacial es ${total}")
    #     case 3:
    #         while True:
    #             print('''
    #             Seleccione una opción:
    #             1.- Audifono JBL 720 $60.000
    #             2.- Audifono Gamer $40.000
    #             3.- Audifonno normal y aburrido $8.000
    #             4.- Volver al menú principal
    #                 ''')
    #             op=int(input())
    #             match op:
    #                 case 1:
    #                     total+=60000
    #                     cantAr+=1
    #                 case 2:
    #                     total+=40000
    #                     cantAr+=1
    #                 case 3:
    #                     total+=8000
    #                     cantAr+=1
    #                 case 4:
    #                     break
    #                 case _:
    #                     print("Opción no válida.")
    #             print(f"Articulo agregado al carro, lleva {cantAr} en total")
    #             print(f"El total pacial es ${total}")
    #     case 4:
    #         print("------0------")
    #         print(f"Total de articulos {cantAr}")
    #         print(f"Total neto {total}")
    #         print(f"Total + IVA {total*1.19}")
    #         print("------0------")
    #     case 5:
    #         print("Saliendo...")
    #     case _:
    #         print("Opción no válida.")
# deuda = 100000
# while True:
    # while True:
    #     try: 
    #         print('''
    #         Seleccione una opción:
    #         1.- Pago de tarjeta de credito
    #         2.- Simulación de compra
    #         3.- Salir
    #             ''')
    #         op=int(input())
    #         break
    #     except Exception:
    #         print("Ingrese solo números enteros.")
    # match op:
    #     case 1:
    #         while True:
    #             monto=int(input("Ingrese monto que desea pagar: "))
    #             if monto<=0:
    #                 print("El monto no puede ser negativo.")
    #                 print("intente de nuevo.")
    #             elif monto>deuda:
    #                 print(f"El monto excede la deuda (${deuda})")
    #             else:
    #                 print(f"Pago de ${monto} aceptado. Deuda restante: ${deuda-monto}")
    #                 break
    #     case 2:
    #         saldot=int(input("Ingrese el saldo inical de la tarjeta: "))
    #         n_comp= int(input("¿Cuántas compras desea simular?: "))
    #         s_com=0
    #         for i in range(n_comp):
    #             monto=int(input(f"Ingrese el monto de la compra {i+1}"))
    #             if monto<=0:
    #                 print("El monto no puede ser negativo.")
    #                 continue
    #             if monto>saldot:
    #                 print("Saldo insuficiente para realizar la compra ")
    #                 continue
    #             saldot-=monto
    #             s_com+=monto
    #             print(f"Compra realizada, saldo restante: {saldot}")
    #         print(f"Total gastado: ${s_com}")
    #         print(f"Saldo final en la tarjeta: ${saldot}")
    #     case 3:
    #         print("Saliendo")
    #         break

total=0
cantP=0
pik=0
otak=0
pulp=0
ang=0

print('''
Delivey Sushi
1.- Pikachu Roll ''')

