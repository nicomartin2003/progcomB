# 1-	Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra cualquiera: ")
for times in range(10):
    print(f"la palabra es: {word}")
# 2-	Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age1 = int(input("Ingrese su edad: "))
age2 = 0
for times in range(age1):
    age2 += 1
    print(age2)

# 3-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

num = int(input("Ingrese un numero entero positivo: "))
num2 = 0
for times in range(num):
    num2 += 1
    if (num2 % 2 != 0):
        print(num2,end=", ")

# 4-	Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input("Ingrese un numero entero positivo: "))
for i in range(num+1):
    print(num,end= ", ")
    num = num - 1

# 5-	Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cash = int(input("Ingrese la cantidad de dinero que quiere invertir: "))
annual_interest = int(input("Ingrese el interes anual: "))
years = int(input("Ingrese el numero de años: "))
bank = ""
for i in range(years):
    total = (annual_interest * cash)/100
    cash = cash + total
    bank = cash
    print(f"tu porcentaje anual es: {bank}")

# 6-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

num = int(input("Ingrese un numero entero: "))
for i in range(num):
    for j in range(i + 1):
        print("*", end= " ")
    print("")

# 7-	Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

num1 = 1
num2 = 1

for i in range(10):
    for j in range(10):
        print((i +1), "x", (j + 1), "=", (i+1)*(j+1))
    print("-------------------------")

# 8-	Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

height = int(input("Ingrese la altura del triangulo: "))
for i in range(1, height + 1):
    print("*" * i)

# 9-	Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

pasword = "contraseña123"
while True:
    password_entered = input("Ingrese la contraseña: ")

    if (pasword == password_entered):
        print("Contraseña correcta, Bienvenido")
        break
    else:
        print("Contraseña Incorrecta, intente nuevamente")

# 10-	Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

num = int(input("Por favor, ingrese un numero entero: "))
if num <= 1:
    print(f"{num} no es un numero primo")
else:
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{num} es un numero primo")
    else:
        print(f"{num} no es un numero primo")


# 11-	Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

word = input("Por favor, ingrese una palabra: ")
letter = len(word)
for i in range(1, letter+1):
    print(word[-i])

# 12-	Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

phrase = input("Ingrese una frase: ")
letter = input("Ingrese una letra: ")
count = 0
for char in phrase:
    if char.lower() == letter.lower():
        count += 1
print(f"La letra {letter} aparece {count} veces en la frase {phrase}")

# 13-	Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    user_input = input("Ingrese un mensaje (escribe salir para finalizar): ")
    if user_input.lower() == "salir":
        break
    print("Eco: ", user_input)

# 14-	Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

start = int(input("Ingrese el primer número entero: "))
end = int(input("Ingrese el segundo número entero: "))

if start > end:
    start, end = end, start

print("Números pares entre", start, "y", end, ":")
for number in range(start, end + 1):
    if number % 2 == 0:
        print(number, end=" ")

print("\nNúmeros impares entre", start, "y", end, ":")
for number in range(start, end + 1):
    if number % 2 != 0:
        print(number, end=" ")

# 15-	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

num = int(input("Por favor, ingrese un numero entero mayor que cero: "))

if num <= 0:
    print("El numero debe ser mayor que cero")
else:
    print("Los divisores de ", num, " son: ")
    for i in range(1, num + 1):
        if num % 1 == 0:
            print(i)

# 16-	Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y escriba cuántos negativos ha introducido.

num = int(input("¿Cuántos números vas a introducir? "))
count_negativos = 0
for i in range(num):
    num = float(input("Introduce un número: "))
    if num < 0:
        count_negativos += 1
print(f"Has introducido {count_negativos} números negativos.")

# 17-	Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase = input("Por favor, ingrese una frase: ")
vowels = ["a", "e", "i", "o", "u"]
vowels_found = []
for character in phrase:
    character = character.lower()
    if character in vowels and character not in vowels_found:
        vowels_found.append()
print("Vocales encontradas en la frase: ", vowels_found)

# 18-	Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

first_num = 0
second_num = 1
print(first_num)
for i in range(9):
    next_num = first_num + second_num
    print(next_num)
    first_num = second_num
    second_num = next_num

# 19-	Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.

savings = float(input("Ingrese la meta a la que desea ahorrar: "))
conditional = True
total_saved = 0
while conditional:
    money_deposited = float(input("Ingrese la cantidad de dinero que desea ahorrar: "))
    if money_deposited > 0:
        total_saved += money_deposited
    else:
        print("Solo numeros positivos")
    if total_saved >= savings:
        print("Meta alcanzada")
        conditional = False

# 20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

conditional = 1
counter = 0
while conditional != 0:
    conditional = int(input("Ingrese un numero entero: "))
    if conditional != 0:
        counter += conditional
print(f"La suma de los numeros ingresados es: {count}")

# 21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.

conditional = 1
num_mayor = 0
while conditional != 0:
    conditional = int(input("Ingrese un numero entero: "))
    if conditional != 0:
        if conditional > num_mayor:
            num_mayor = conditional
print(f"El numero mayor ingresado es: {num_mayor}")

# 22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

pair_numbers = 0
while True:
    numbers = int(input("Ingrese un numero entero positivo (0 - 1 para terminar): "))
    if numbers == -1:
        break
    if numbers % 2 == 0:
        pair_numbers += 1
    digit_sum = 0
    num_temp = abs(numbers)
    while num_temp > 0:
        digito = num_temp % 10
        digit_sum += digito
        num_temp //= 10
    print(f"La suma de los digitos de {numbers} es {digit_sum}")
print(f"Se ingresaron {pair_numbers} numeros pares")

# 23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

conditional = 1
while conditional > 0:
    conditional = int(input("Ingrese el valor del producto: "))
    if conditional == 0:
        break
print("Fin de la ejecucion")

# 24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

conditional = 1
total = 0
while conditional > 0:
    conditional = int(input("Ingrese el valor del producto: "))
    if conditional > 0:
        total += conditional
    elif conditional < 0:
        print("Error ingrese de nuevo el numero")
    elif conditional == 0:
        break
if total >= 1000:
    print(f"Felicidades obtuvo un descuento y 10%, el total de la compra es: ${total-(total*0.10)}")
else:
    print(f"La cantidad a pagar es de: ${total}")


# 25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.

num = int(input("Ingrese un numero entero positivo: "))
if num < 0:
    print("El numero ingresado debe ser positivo")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= 1
    print(f"El factorial de {num} es: {factorial}")
    