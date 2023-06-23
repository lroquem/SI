alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def leer_archivo():
    archivo = input("Ingrese direccion del archivo:")
    with open(archivo, 'r') as file:
        contenido = file.read()
    return contenido

def preprocesamiento_texto(texto):
    texto_limpio = ""
    texto = texto.upper()
    for caracter in texto:
        if caracter in alfabeto:
            texto_limpio += caracter
    return texto_limpio

def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        indice = (alfabeto.index(caracter) + desplazamiento) % len(alfabeto)
        nuevo_caracter = alfabeto[indice]
        resultado += nuevo_caracter
    return resultado

def descifrado_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        indice = (alfabeto.index(caracter) - desplazamiento) % len(alfabeto)
        nuevo_caracter = alfabeto[indice]
        resultado += nuevo_caracter
    return resultado

def leer_desplazamiento():
    while True:
        try:
            numero = int(input("Ingrese el desplazamiento (numero entero positivo): "))
            if numero > 0:
                return numero % 27
            else:
                print("¡Error! El número debe ser mayor a cero.")
        except ValueError:
            print("¡Error! Ingrese un número entero válido.") 

def cesar(mensaje, desplazamiento):
    cifrado = cifrado_cesar(preprocesamiento_texto(mensaje), desplazamiento)
    print()
    print("CIFRANDO")
    print()
    print("Mensaje: ", mensaje)
    print("Desplazamiento: ", desplazamiento)
    print("Cifrado: ", cifrado)
    print()
    print("Descifrado: ", descifrado_cesar(cifrado, desplazamiento))
    print()
    
def cesar_menu():
    while True:
        print("Cifrado Cesar")
        print("---- MENÚ ----")
        print("1. Leer archivo")
        print("2. Leer linea")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mensaje = leer_archivo()
            desplazamiento = leer_desplazamiento()
            cesar(mensaje, desplazamiento)
        elif opcion == '2':
            mensaje = input("Ingrese mensaje a cifrar:")
            desplazamiento = leer_desplazamiento()
            cesar(mensaje, desplazamiento)
        elif opcion == '0':
            print("Volviendo al menú principal")
            break
        else:
            print("Opción inválida. Intente nuevamente.")