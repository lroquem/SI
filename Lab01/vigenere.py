a27 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def generar_ascii():
    caracteres = ""
    for i in range(191):
        caracteres += chr(i)
    return caracteres

def leer_archivo():
    archivo = input("Ingrese direccion del archivo:")
    with open(archivo, 'r') as file:
        contenido = file.read()
    return contenido

def preprocesamiento_texto(texto, alfabeto):
    texto_limpio = ""
    texto = texto.upper()
    for caracter in texto:
        if caracter in alfabeto:
            texto_limpio += caracter
    return texto_limpio

def cifrado_vigenere(texto, k, alfabeto):
    resultado = [] 
    indice_clave = 0
    for c in texto:
        num = alfabeto.find(c)
        if num != -1:
            num += alfabeto.find(k[indice_clave])
            num %= len(alfabeto)
            resultado.append(alfabeto[num])
            indice_clave += 1
            if indice_clave == len(k):
                indice_clave = 0 
    return("". join(resultado)) 

def descifrado_vigenere(texto, k, alfabeto):
    resultado = [] 
    indice_clave = 0
    for c in texto:
        num = alfabeto.find(c)
        if num != -1:
            num -= alfabeto.find(k[indice_clave])
            num %= len(alfabeto)
            resultado.append(alfabeto[num])
            indice_clave += 1
            if indice_clave == len(k):
                indice_clave = 0 
    return("". join(resultado)) 

def vigenere(alfabeto, mensaje, clave):
    cifrado = cifrado_vigenere(preprocesamiento_texto(mensaje, alfabeto), clave, alfabeto)
    print()
    print("CIFRANDO")
    print()
    print("Mensaje: ", mensaje)
    print("Clave: ", clave)
    print("Cifrado: ", cifrado)
    print()
    print("Descifrado: ", descifrado_vigenere(cifrado, clave, alfabeto))
    print()
    
def vigenere_clave(alfabeto, mensaje):
    while True:
        print("---- CLAVE ----")
        print("1. Leer archivo")
        print("2. Leer linea")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            clave = leer_archivo()
            vigenere(alfabeto, mensaje, clave)
            break
        elif opcion == '2':
            clave = input("Ingrese clave para cifrar:")
            vigenere(alfabeto, mensaje, clave)
            break
        elif opcion == '0':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def vigenere_mensaje(alfabeto):
    while True:
        print("---- MENSAJE ----")
        print("1. Leer archivo")
        print("2. Leer linea")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mensaje = leer_archivo()
            vigenere_clave(alfabeto, mensaje)
            break
        elif opcion == '2':
            mensaje = input("Ingrese mensaje a cifrar:")
            vigenere_clave(alfabeto, mensaje)
            break
        elif opcion == '0':
            break
        else:
            print("Opción inválida. Intente nuevamente.")
    
def vigenere_menu():
    while True:
        print("Cifrado Vigenere")
        print("---- ALFABETO ----")
        print("1. Alfabeto 27")
        print("2. Alfabeto ASCII")
        print("0. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            alfabeto = a27
            vigenere_mensaje(alfabeto)
        elif opcion == '2':
            alfabeto = generar_ascii()
            vigenere_mensaje(alfabeto)
        elif opcion == '0':
            print("Volviendo al menú principal")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
            
mensaje = "GYLKWQRVEBTPXDJRQDDVQNPHHGQGUWRNPPWHRGCONLJOHMÑCOXEEAVASIÑDOEQPETAPVHEOPEKRXYAEVRUHAÑVNRSIVPZBSXINLEWSMGBSHEEITVDEENSVR"
clave = "PEDRONAVAJA"

print("Cypher: ", mensaje)
print("Clave: ", clave)
print("Descifrado: ", descifrado_vigenere(mensaje, clave, a27))