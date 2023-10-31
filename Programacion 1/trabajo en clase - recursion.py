# # Escribir una función que simule el siguiente experimento: Se tiene una rata en una
# jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
# probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
# minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
# La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
# quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula

import random

def tiempo_para_salir(tiempo = 0):
    

    Camino_elegido = random.choice([1, 2, 3])

    if Camino_elegido == 1:
        return tiempo_para_salir(tiempo+3)
    elif Camino_elegido == 2:
        return tiempo_para_salir(tiempo+5)
    elif Camino_elegido == 3:
        tiempo+= 7

    return tiempo
tiempo_salida = tiempo_para_salir()

print(f"El raton se tardo en salir {tiempo_salida} minutos ")

# Escribir una consigna apropiada para la siguiente función. Asumir que n es un número
# entero.

def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

print(f(123))


# El código que se muestra en la imagen define una función llamada f() que toma un número entero como entrada y devuelve una cadena que es la representación invertida del número.

# La función funciona de la siguiente manera:

# La función primero convierte el número entero en una cadena usando la función str().
# Luego, la función usa la función len() para determinar la longitud de la cadena.
# Si la longitud de la cadena es menor o igual a 1, la función simplemente devuelve la cadena original.
# De lo contrario, la función devuelve la última letra de la cadena, más la salida de la función f() llamada con el número entero que representa la cadena sin la última letra.