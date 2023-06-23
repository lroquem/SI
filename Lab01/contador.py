def contar_letras():
    entrada = input("Ingrese una cadena de texto: ")
    contador = {}
    entrada = entrada.upper()
    # Contar la cantidad de veces que se repiten las letras
    for letra in entrada:
        if letra.isalpha():
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1
    
    # Ordenar las letras por cantidad de mayor a menor
    letras_ordenadas = sorted(contador.items(), key=lambda x: x[1], reverse=True)
    
    # Mostrar los resultados en un cuadro
    print("Carácter\tCantidad")
    print("------------------------")
    for letra, cantidad in letras_ordenadas:
        print(f"{letra}\t|\t{cantidad}")
# Llamada a la función
contar_letras()