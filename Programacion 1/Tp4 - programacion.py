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


