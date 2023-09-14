while True:
    print("Menu de opciones")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("e. Opcion 3")
    print("o. Salir")
    option = input("Seleccione una carpeta: ")
    if option == "1":
        print("Ha elegido la opcion 1")
    elif option == "2":
        print("Ha elegido la opcion 2")
    elif option == "3":
        print("Ha elegido la opcion 3")
    elif option == "0":
        print("Saliendo del programa")
        break
    else:
        print("Opcion no valida. Por favor, elija una opcion correcta")