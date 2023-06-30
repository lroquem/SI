import unicodedata

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
