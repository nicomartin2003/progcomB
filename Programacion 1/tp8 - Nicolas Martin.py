# 1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

def contar_digitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contar_digitos(n // 10)
    
num = int(input("Ingrese un numero entero: "))
cantidad_digitos = contar_digitos(num)
print(f"El numero {num} tiene {cantidad_digitos} digitos")

# 2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.

def es_potencia(n, b):
    if n == 1:
        return True
    if n < b or n % b != 0:
        return False
    return es_potencia(n // b, b)

n = int(input("Ingrese el valor de n: "))
b = int(input("Ingrese el valor de b: "))

resultado = es_potencia(n, b)

print(resultado)

# 3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:

def find_positions(a, b, start=0, positions=None):
    if positions is None:
        positions = [] 

    next_occurrence = a.find(b, start)

    if next_occurrence != -1:
        positions.append(next_occurrence)

        find_positions(a, b, next_occurrence + 1, positions)

    return positions

a = input("Ingrese una frase cualquiera: ")
b = input("Ingrese que letra desea buscar: ")
positions = find_positions(a, b)
print(positions)

# 4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
# •	1 es impar.
# •	Si un número es impar, su antecesor es par; y viceversa.

def par(n):
    if n == 0:
        return True
    else:
        return impar(n - 1)
    
def impar(n):
    if n == 1:
        return True
    else:
        return par(n - 1)
    
numero = int(input("Ingrese un numero entero: "))
if par(numero):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")

# 5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.

def encontrar_mayor_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        sub_max = encontrar_mayor_elemento(lista[1:])
        if lista[0] > sub_max:
            return lista[0]
        else:
            return sub_max

mi_lista = [10, 5, 17, 22, 8, 35, 13]
mayor = encontrar_mayor_elemento(mi_lista)
print("El mayor elemento de la lista es:", mayor)

# 6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

def replicar(lista, n):
    if not lista:
        return []

    return [lista[0]] * n + replicar(lista[1:], n)

mi_lista = [1, 3, 3, 7]
n = 2
resultado = replicar(mi_lista, n)
print(resultado)

# 7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# ● El programa debe pedir al usuario que ingrese un número n, y un número d,
# ● Luego debe calcular el valor de K(n, p) usando una función recursiva,
# ● Debe imprimir el resultado de K(n, p)

def calcular_sumatoria(n, p):
    if n == 1:
        return p
    else:
        return n * p + calcular_sumatoria(n - 1, p)

try:
    n = int(input("Ingresa el valor de n: "))
    p = int(input("Ingresa el valor de p: "))
    resultado = calcular_sumatoria(n, p)
    print(f"El resultado de K({n}, {p}) es: {resultado}")
except ValueError:
    print("Debes ingresar números enteros.")

# 8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.

def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

n = 5
k = 2
resultado = pascal(n, k)
print(f"El valor en la fila {n} y la columna {k} del Triángulo de Pascal es {resultado}")

# 9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos).

def combinaciones(lista, k, actual=[]):
    if k == 0:
        print("".join(actual))
    elif not lista:
        return
    else:
        primer_caracter = lista[0]
        combinaciones(lista, k - 1, actual + [primer_caracter])
        combinaciones(lista[1:], k, actual)

caracteres = ['A', 'B', 'C']
longitud_combinacion = 2
combinaciones(caracteres, longitud_combinacion)

# 10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.
# Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N) calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.

def medidas_hoja_A(N):
    if N == 0:
        return (841, 1189)

    ancho_A_N_1, largo_A_N_1 = medidas_hoja_A(N - 1)

    nuevo_ancho = largo_A_N_1
    nuevo_largo = ancho_A_N_1 / 2

    return (nuevo_ancho, nuevo_largo)

N = 4 
ancho, largo = medidas_hoja_A(N)
print(f"Las medidas de la hoja A{N} son: Ancho={ancho} mm, Largo={largo} mm")
