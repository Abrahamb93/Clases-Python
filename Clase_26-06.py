juegos={
    1:{"Nombre": "Metroid Dread",
       "Precio": 55000,
       "Code": "MTDr2022"
       },
    2:{"Nombre": "Zelda TOTK",
       "Precio": 65000,
       "Code": "zdtk2025"}
}

def mostrar_juegos(dict):
    for j, dato in dict.items():
        print(j, dato)

def insert_juego(dict):
    while True: 
        nombre=input("Ingrese el nombre: ")
        if validar_nombre(nombre):
            break
        else:
            print("El nombre del juego debe tener al menos 2 palabras")
    while True: 
        precio=int(input("Ingrese el precio: "))
        if valida_precio(precio):
            break
        else:
            print("El precio debe estar entre $8000 y $10000")
    while True: 
        codigo=input("Ingrese el código: ")
        if valida_code(codigo):
            pos=list(dict.keys())[-1]
            dict[pos+1]={"Nombre": nombre, "Precio": precio, "Code": codigo}
            break
        else:
            print("No se agregó el juego")

def borrar_juegos(dict):
    mostrar_juegos(dict)
    borrar=int(input("Qué juego desea borrar: "))
    del juegos[borrar]


def act_juegos(dict):
    mostrar_juegos()
    act=int(input("Seleccione el juego a actualizar?: "))
    while True:
        print('''
        1.- Nombre
        2.- Precio
        3.- Código
        4.- Salir''')
        dato=int(input("Qué dato va aactualizar?"))
## Validaciones  
'''
El nombre debe tener por lo menos 2 palabras
El precio debe estar entre $8000 y $100000
El código del juego debe tener 2 mayusculas, 2 minusculas y 4 números '''

def valida_code(code):
    Mayuscula=0
    Minuscula=0
    Numero=0
    for palabra in code:
        if palabra.isupper():
            Mayuscula+=1
        if palabra.islower():
            Minuscula+1
        if palabra.isdigit():
            Numero+=1
    if Minuscula==2 and Minuscula==2 and Numero==4:
        print("La código está bien escrito")
        return True
    else:
        print("La código está mal escrito")
        return False

def valida_precio(precio):
    if precio>=8000 and precio<=100000:
        return True
    else:
        return False
    
def validar_nombre(nombre):
    for l in nombre:
        if " " ==l:
            return True
        

while True: 
    try:
        print('''
        1.- Registrar un juego
        2.- Mostrar juegos
        3.- Actualizar juego
        4.- Borrar juego
        5.- Salir
            ''')
        op=int(input("Seleccione una opción: "))
        match op:
            case 1:
                insert_juego(juegos)
            case 2:
                mostrar_juegos(juegos)
            case 3:
                print("")
            case 4:
                borrar_juegos(juegos)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")
    except Exception as e:
        print("El error es: ", e)