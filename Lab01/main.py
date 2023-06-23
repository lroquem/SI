from cesar import cesar_menu
from vigenere import vigenere_menu

def main_menu():
    while True:
        print("---- CIFRADO ----")
        print("1. Cifrado Cesar")
        print("2. Cifrado Vigenere")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cesar_menu()
        elif opcion == '2':
            vigenere_menu()
        elif opcion == '0':
            print("Cerrando el programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.") 
             
main_menu()