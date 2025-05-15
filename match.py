# Uso y explicación de match

def suma():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print("El resultado de la suma", n1+n2)

def resta():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print("El resultado de la suma", n1-n2)

def multiplicar():
    n1=int(input("Ingrese un número: "))
    n2=int(input("Ingrese otro número: "))
    print("El resultado de la suma", n1*n2)

def dividir():
    try:
        n1=float(input("Ingrese un número"))
        n2=float(input("Ingrese otro número: "))
        print("El resultado de la suma", n1/n2)
    except ZeroDivisionError as division:
        # Código para manejar división por 0
        print(f"Se produjo una excepción {division}")
    



while True: 
    print ('''
    Operaciones Matemáticas:
    ------------------------
    1. Suma
    2. Resta
    3. Multiplicar
    4. Dividir
    5. Salir
    ''')
    op=int(input("Seleccione una opción: "))

    match op:
        case 1:
            print("Suma")
            suma()
        case 2:
            print("Resta")
            resta()
        case 3:
            print("Multiplicar")
            multiplicar()
        case 4:
            print("Dividir")
            dividir()
        case 5:
            print("Saliendo")
            break
        case _:
            print("Opción no válida")

