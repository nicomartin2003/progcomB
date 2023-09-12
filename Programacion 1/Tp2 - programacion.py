import math
#1-	Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el 
#computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.
anios = int(input("Ingrese cuantos años tiene su computadora."))

if (anios <= 2):
    print("Su computadora es nueva.")
else:
    print("Su computadora es vieja.")

# #2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
anios = int(input("Ingrese cuantos años tiene su computadora."))

if (anios < 0):
    print("Error.")
elif (anios <= 2):
    print("Su computadora es nueva.")
else:
    print("Su computadora es vieja.")

#3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. 
# A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir 
# ‘no hay coincidencia’.

nombre1 = input("Ingresa el primer nombre: ")
nombre2 = input("Ingresa el segundo nombre: ")

primera_letra_nombre1 = nombre1[0].lower()
primera_letra_nombre2 = nombre2[0].lower()

if (primera_letra_nombre1 == primera_letra_nombre2):
    print("Coincidencia")
else:
    print("No hay coincidencia")

#4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
#Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
voto = str(input("Ingrese a qu candidato votar. A, B o C. ")).lower()

if(voto == "a"):
    print("Voto por el partido rojo.")
elif(voto=="b"):
    print("Voto por el partido verde.")
elif(voto=="c"):
    print("Voto por el partido azul.")
else:
    print("Opcion erronea.")

#5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
#Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
letra = str(input("Ingrese una letra. ")).lower()

if(len(letra)==1):
    if(letra == "a" or letra == "e" or letra == "i" or letra == "a" or letra == "o" or letra == "u"):
        print("Ingreso una vocal.")
    else:
        print("Ingreso una consonante.")
else:
    print("No se puede procesar")

#6-	Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
anio = int(input("Ingrese un año. "))

if (((anio % 4) == 0 and ((anio % 100) != 0)) or (((anio % 100) == 0) and (((anio % 400) == 0)))):
    print("El año es bisiesto.")
else:
    print("El año no fue bisiesto.")

#7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))
num3 = int(input("Ingrese otro numero: "))

menor = num1

if(num2 < menor):
    menor=num2
if(num3 < menor):
    menor = num3
print(f"El menor numero de los 3 es, {menor}")

#8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.

nombre = str(input(" Ingrese su nombre: "))
contraseña = str(input(" Ingrese la contraseña: "))

if(nombre == "Gwenevere")and(contraseña == "excalibur"):
    print(f"Usuario y contrasela correctos.")

else:
    print(f"Acceso denegado")

#9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ").upper()
sexo = input("INgrese su sexo M/F: ").upper()

if(sexo == "F")and(nombre < "M"):
    grupo = "A"
elif(sexo == "M")and(nombre > "N"):
    grupo = "A"
else:
    grupo = "B"

print(f"Usted pertenece al grupo, {grupo}")

#10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.

edad = int(input("Ingrese su edad: "))

if(edad < 4):
    print("Usted pasa gratis")
elif(edad >= 4 and edad <= 18):
    print("Usted tiene que pagae $500")
else:
    print("Usted debe pagar $1000")

    #11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
    #•	Ingredientes vegetarianos: Pimiento y tofu.
    #•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
    #Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza = input("Desea pizza vegariana S/N: ").lower()

if(pizza == "s"):
    print("Ingredientes:")
    print("Opcion 1: Pimiento")
    print("Opcion 2: Tofu")
    ing = (int(input("Seleccione un ingrediente: ")))
    if(ing == 1):
        print("La pizza es vegetariana con pimiento")
    elif(ing == 2):
        print("La pizza es vegetariana con tofu")
if(pizza == "n"):
    print("Ingredientes:")
    print("Opcion 1: Peperoni")
    print("Opcion 2: Jamon")
    print("Opcion 3: Salmon")
    ing = int(input("Seleccion un ingrediente: "))
    if(ing == 1):
        print("La pizza no es vegatariana y tiene Peperoni")
    elif(ing == 2):
        print("La pizza no es vegetaria y tiene Jamon")
    elif(ing == 3):
        print("La pizza no es vegetariana y tiene Salmon")
    
#12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.

anio_actual = int(input("Ingrese el año actual: "))
anio_cualquiera = int(input("INgrese un año cualquiera: "))

if(anio_actual < anio_cualquiera):
   total = anio_cualquiera - anio_actual
   print(f"Faltan {total} años para el año, {anio_cualquiera}")
elif(anio_actual > anio_cualquiera):
    total = anio_actual - anio_cualquiera
    print(f"Han pasado {total} años desde el año, {anio_cualquiera}")

#13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 <= 0 or num2 <= 0:
    print("Los valores deben ser positivos y diferentes de cero.")
else:
        if num1 > num2:
            mayor = num1
            menor = num2
        else:
            mayor = num2
            menor = num1
        if mayor % menor == 0:
            print(f"{mayor} es múltiplo de {menor}.")
        else:
            print(f"{mayor} no es múltiplo de {menor}.")

#14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
#Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
#x = -b / a

coeficiente1 = int(input("Ingrese el primer coeficiente: "))
coeficiente2 = int(input("Ingrese el segundo coeficiente: "))

if(coeficiente1 == 0):
    if(coeficiente2 == 0):
        print("Es solucion Infinita")
    else:
        print("La solucion es nula")
else:
    x = -coeficiente2 / coeficiente1
    print(f"La solucion es: {x}")

#15-	Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.

area = str(input("Desea calcular el area de un triangulo o de un circulo?(T/C): ")).lower()
if(area == "c"):
    radio = float(input("Ingrese el radio del circulo: "))
    calculo_area = math.pi * (radio**2)
    print(f"El radio del criculo es, {calculo_area}")
elif(area == "t"):
    base_t = float(input("Ingrese la base del triangulo: "))
    altura_t = float(input("Ingrese la altura del triangulo: "))
    calculo_area_t = (base_t * altura_t) /2
    print(f"El area del triangulo es, {calculo_area_t}")


#16-	Haz una calculadora básica pida al usuario dos valores, a y b.
#Según la opción que desean, realizar la operación:
#•	Si operación es 1 entonces debemos ver el resultado de a + b
#•	Si operación es 2 entonces debemos ver el resultado de a * b
#•	Si operación es 3 entonces debemos ver el resultado de a - b
#•	Si operación es 4 entonces debemos ver el resultado de a / b

print("Calculadora Básica")
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

print("Opciones:")
print("1. Suma")
print("2. Multiplicación")
print("3. Resta")
print("4. División")

operacion = int(input("Selecciona una opción (1/2/3/4): "))

if operacion == 1:
    resultado = a + b
    print(f"El resultado de {a} + {b} es: {resultado}")
elif operacion == 2:
        resultado = a * b
        print(f"El resultado de {a} * {b} es: {resultado}")
elif operacion == 3:
    resultado = a - b
    print(f"El resultado de {a} - {b} es: {resultado}")
elif operacion == 4:
    if b != 0:
            resultado = a / b
            print(f"El resultado de {a} / {b} es: {resultado}")
    else:
            print("No se puede dividir entre 0.")
else:
    print("Opción inválida. Por favor selecciona una opción válida (1/2/3/4).")

#17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

dia_semana = input("Ingresa un día de la semana: ")
dia_semana = dia_semana.lower()

if dia_semana == "lunes":
    print("Es un día laboral, comienza la semana.")
elif dia_semana == "viernes":
    print("¡Es viernes! ¡Fin de semana a la vista!")
elif dia_semana == "sabado" or dia_semana == "sábado" or dia_semana == "domingo":
    print("¡Es fin de semana! Disfruta y descansa.")
else:
    print("No es ni lunes, ni viernes, ni fin de semana. ¡Ánimo!")

#18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
#La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
#Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.

jornada_minima = 48
tarifa_normal = float(input("Ingrese el salario por hora: "))
horas_trabajadas = float(input("Ingrese el total de horas trabajadas en el mes: "))
    
if horas_trabajadas > jornada_minima:
    horas_extras = horas_trabajadas - jornada_minima
    salario_total = (jornada_minima * tarifa_normal) + (horas_extras * tarifa_normal * 1.1)
    print(f"Horas extras trabajadas: {horas_extras:.2f}")
else:
    horas_extras = 0
    salario_total = horas_trabajadas * tarifa_normal
    
print(f"Salario total: ${salario_total:.2f}")

#19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.

cantidad_lapices = int(input("Ingrese cuantos lapices quiere comprar: "))
lapiz = int(input("Cuantas lapices se va a llevar?"))

if(lapiz>= 1000):
    tot=60*lapiz-((60*0.07)*lapiz)
    print(f"El total es de ${tot}")
else:
    print(f"El total es de ${lapiz*60}")

#20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.
num1 = float(input("Ingrese la nota 1: "))
num2 = float(input("Ingrese la nota 2: "))
num3 = float(input("Ingrese la nota 3: "))
num4 = float(input("Ingrese la nota 4: "))

prom = (num1 + num2 + num3 + num4)/4

if (prom > 6):
    print("Esta aprobado.")
else:
    print("Desaprobo.")
