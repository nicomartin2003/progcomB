# 1. Cree un bucle while con las siguientes características:

# • El valor inicial de la variable x será 0.
# • El valor del incremento será 1.
# • La condición de salida del bucle será mayor o igual a 30.
# • La ejecución debe interrumpirse cuando x es igual a 15.
# • Debes imprimir la siguiente frase cada vez que se ejecuta el bucle: 'El valor del bucle es: ' + x.
# • Debes saltarte las ejecuciones con el valor de x en 4, 6 y 10.
# • En cada salto de ejecución, debe mostrar los valores saltados con este mensaje: 'El valor ' + x ' de x fue omitido'.
# • Cuando se interrumpe la ejecución del bucle se debe mostrar un mensaje indicándolo: 'La ejecución del bucle se interrumpe cuando x era' + x.

x = 0
while x <= 30:
    if x == 15:
        print("La ejecucion del bucle se interrumpio cuando x era", str(x))
        break
        
    if x in (4, 6, 10):
        print("El valor ", str(x), " de x fue omitido ")
        x += 1
        
    print("El valor del bucle es: ", str(x))
    x += 1

# 2.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

lineas = []
while True:
    linea = input("Ingrese una linea (o deje en blanco para finalizar): ")
    if not linea:
        break
    lineas.append(linea)
    for linea in lineas:
        print(linea.upper())

# 3.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50
# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos

print("Bienvenido a su cuenta de banco.")
deposit = 0
aux = 0
while True:
    option = (input("Ingrese D para depositar R para retirar (para finalizar deje el campo vacio): ")).upper()
    if option == "D":
        while True:
            entered = float(input("Ingrese la cantidad de dinero que desea meter: $"))
            if entered <= 0:
                print("Ingrese un valor mayor a 0")
                continue
            else:
                deposit += entered
            option_deposit = (input("Ingrese A para seguir depositando o B para volver al menu: ").upper())
            if option_deposit == "A":
                print("Volviendo al menu")
                break
            else:
                print("Opcion incorrecta, volviendo al menu")
                break
    elif option == "R":
        while True:
            if deposit <= 0:
                print("No tiene dinero para retirar....volviendo al menu")
                break
            else:
                remove = float(input("Ingrese la cantidad de dinero que desea retirar:$ "))
                if remove <= deposit and remove > 0:
                    print(f"Retirando {remove} de su cuenta")
                    continue
                else:
                    print("Error, debe ingresar un numero positivo y mayor a 0. Volviendo al menu")
                    break
    elif option == "":
        print(f"La cantidad de dinero en su cuenta es de {deposit}")
        break
    else:
        print("Opcion ingresada incorrecta. Intentelo otra vez")

# 4.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
# Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

prime_counter = 0
while True:
    num1 = int(input("Ingrese un numero mayor que 1 (o 0 para finalizar): "))
    if num1 == 1 or num1 < 0:
        print("No puede ingresar 1 o numero negativos")
        continue
    if num1 == 0:
        break
    if num1 > 1:
        cousin = True
        for i in range(2, int(num1 ** 0.5) + 1):
            if num1 % 1 == 0:
                cousin = False
                break
            if cousin:
                prime_counter += 1
print(f"La cantidad total de numero primos ingresado es de: {prime_counter}")

# 5.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
# Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

year_inicio = int(input("Ingrese el año de inicio: "))
year_fin = int(input("Ingrese el año de fin: "))
encontrado = False
print(f"Años biciestos y multiplos de 10 en el rango {year_inicio} y {year_fin}")
for year in range(year_inicio, year_fin + 1):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        if year % 10 == 0:
            print(year)
            encontrado = True
if encontrado == False:
    print("No se encontraron años biciestos en el rango especificado")

# 6.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares

for num1 in range(1, 21):
    if num1 % 2 != 0:
        continue
    print(num1)

# 7.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.

numbers = [10, 20, 30, 40, 50]
target = 30
for number in numbers:
    if number == target:
        print("Numero encontrado", number)
        break

# 8.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

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
