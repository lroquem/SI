import unicodedata
import string

def sustituir(texto):
    sustituciones = {
        'a': 'o',
        'h': 'i',
        'ñ': 'm',
        'k': 'l',
        'u': 'v',
        'w': 'v',
        'z': 'y',
        'x': 'r'
    }
    for clave, valor in sustituciones.items():
        texto = texto.replace(clave, valor)
        texto = texto.replace(clave.upper(), valor.upper())
    return texto

def eliminar_tildes(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

def convertir_a_mayusculas(texto):
    texto_mayusculas = texto.upper()
    return texto_mayusculas

def eliminar_espacios_puntuacion(texto):
    texto_sin_espacios_puntuacion = ''.join(c for c in texto if c not in string.punctuation + ' ' + '¡' + '¿')
    return texto_sin_espacios_puntuacion

def obtener_alfabeto(texto):
    caracteres_unicos = set(texto)
    alfabeto = sorted(caracteres_unicos)
    return alfabeto

def obtener_long_alfabeto(alfabeto):
    longitud_alfabeto = len(alfabeto)
    return longitud_alfabeto

def guardar_texto(texto, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)
        
        
mensaje = "Mi corazón oprimidoSiente junto a la alborada El dolor de sus amores Y el sueño de las distancia. La luz de la aurora lleva Semilleros de nostalgias Y la tristeza sin los ojos De la médula del alma. La gran tumba de la noche Su negro velo levanta Para ocultar con el día La inmensa cumbre estrellada. ¡Qué haré yo sobre estos campos Cogiendo niños y ramas Rodeado de la aurora Y llena de noche el ama! ¡Qué haré si tienes tus ojos Muertos a las luces claras Y no ha de sentir mi carne El calor de tus miradas! ¿Por qué te perdí por siempre En aquella tarde clara? Hoy mi pecho está reseco Como una estrella apagada. ALBA, Federico García Lorca"

print(mensaje)
print("\n***************")
print("SUSTITUCIONES")
print("***************\n")
mensaje = sustituir(mensaje)
print(mensaje)
print("\n***************")
print("ELIMINAR TILDES")
print("***************\n")
mensaje = eliminar_tildes(mensaje)
print(mensaje)
print("\n***************")
print("MAYÚSCULAS")
print("***************\n")
mensaje = convertir_a_mayusculas(mensaje)
print(mensaje)
print("\n***************")
print("ELIMINAR ESPACIOS Y PUNTUACIÓN")
print("***************\n")
mensaje = eliminar_espacios_puntuacion(mensaje)
print(mensaje)
print("\n***************")
print("ALFABETO")
print("***************\n")
alfa = obtener_alfabeto(mensaje)
print(alfa)
print(obtener_long_alfabeto(alfa))

guardar_texto(mensaje,"poema_pre.txt")