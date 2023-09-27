# le pedi el nombre al usuario
name = input("Por favor, ingresa tu nombre: ")

# Le di la bienvenida y le di un menu de opciones
while True:
    print(f" Hola, {name}! Bienvenido al programa.")
    print("Menú de opciones:")
    print("1. juego de numeros.")
    print("2. Juego de palabras.")
    print("0. Salir")
    
    option = input("Ingresa tu opción: ")

    if option == '1':
        # Juego de numeros
        numbers = []
        valid_number = True

        while valid_number:
            num = input("Ingresa un número entero (0 para salir): ")

            if num == '0':
                break

            if num.isdigit():
                numbers.append(int(num))
            else:
                print("Por favor, ingresa un número entero válido.")

        even_numbers = [num for num in numbers if num % 2 == 0]
        odd_numbers = [num for num in numbers if num % 2 != 0]

        if even_numbers:
            max_even = max(even_numbers)
            print(f"El mayor número par es: {max_even}")
        else:
            print("No se ingresaron números pares.")

        if odd_numbers:
            average_odd = sum(odd_numbers) / len(odd_numbers)
            print(f"El promedio de los números impares es: {average_odd:.2f}")
        else:
            print("No se ingresaron números impares.")

    elif option == '2':
        # Juego de palabras
        phrase = input("Ingresa una frase: ")
        phrase = phrase.lower()
        vowels = 'aeiou'
        number_vowels = {vocal: phrase.count(vocal) for vocal in vowels}

        print("Cantidad de cada vocal en la frase:")
        for vocal, amount in number_vowels.items():
            print(f"{vocal}: {amount}")

    elif option == '0':
        print(f"Gracias por jugar, {name}!")
        break
    else:
        print("Opción no válida. Por favor, elige una opción válida.")
