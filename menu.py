def mostrar_menu():
    print("Menú:")
    print("1. Calculate grades")
    print("2. regresion logistica")
    print("3. Salir")

def calculategrades():
    print("Has seleccionado la Opción 1.")

def regresionlogistica():
    print("Has seleccionado la Opción 2.")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        calculategrades()
    elif opcion == "2":
        regresionlogistica()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida.")