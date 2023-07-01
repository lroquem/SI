import string

def frecuencias(nombre_archivo):
    frecuencia_letras = {}
    
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read()
        for letra in texto:
            frecuencia_letras[letra] = frecuencia_letras.get(letra, 0) + 1
            
    frecuencia_letras = dict(sorted(frecuencia_letras.items(), key=lambda x: x[1], reverse=True))        
    return frecuencia_letras

def imprimir_primeros_campos(diccionario):
    contador = 0

    for clave, valor in diccionario.items():
        if contador < 5:
            print(f"{clave}: {valor}")
            contador += 1
        else:
            break

archivo = "poema_pre.txt"
frec = frecuencias(archivo)
imprimir_primeros_campos(frec)