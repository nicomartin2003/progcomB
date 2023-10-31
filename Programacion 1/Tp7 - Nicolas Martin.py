# 1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.

def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        intercambio_realizado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Realiza el intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio_realizado = True

        if not intercambio_realizado:
            break

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

ordenamiento_burbuja(numeros)

print("Lista ordenada:", numeros)

# 2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.

def ordenamiento_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

palabras = input("Ingresa una lista de palabras separadas por espacios: ")
lista_palabras = palabras.split()

ordenamiento_seleccion(lista_palabras)

print("Lista ordenada alfabéticamente:")
for palabra in lista_palabras:
    print(palabra)

# 3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.

libros = [
    {"título": "El Gran Gatsby", "autor": "F. Scott Fitzgerald", "año_publicación": 1925},
    {"título": "1984", "autor": "George Orwell", "año_publicación": 1949},
    {"título": "Cien años de soledad", "autor": "Gabriel García Márquez", "año_publicación": 1967},
    {"título": "Matar un ruiseñor", "autor": "Harper Lee", "año_publicación": 1960},
    {"título": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "año_publicación": 1605}
]

def ordenar_por_anio(libro):
    return libro["año_publicación"]

libros_ordenados = sorted(libros, key=ordenar_por_anio)

for libro in libros_ordenados:
    print(f"Título: {libro['título']}, Autor: {libro['autor']}, Año de Publicación: {libro['año_publicación']}")

# 4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

def ordenar_por_longitud(lista_cadenas):
    n = len(lista_cadenas)
    
    for i in range(1, n):
        cadena_actual = lista_cadenas[i]
        j = i - 1
        
        while j >= 0 and len(cadena_actual) < len(lista_cadenas[j]):
            lista_cadenas[j + 1] = lista_cadenas[j]
            j -= 1
        
        lista_cadenas[j + 1] = cadena_actual
    
    return lista_cadenas

lista_cadenas = ["manzana", "pera", "banana", "fresa", "uva"]
lista_ordenada = ordenar_por_longitud(lista_cadenas)
print(lista_ordenada)

# 5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.

def ordenamiento_burbuja_descendente(lista):
    n = len(lista)
    for i in range(n):
        intercambio_realizado = False
        for j in range(0, n - i - 1):
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio_realizado = True

        if not intercambio_realizado:
            break

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

ordenamiento_burbuja_descendente(numeros)

print("Lista ordenada en modo descendente:", numeros)

# 6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

lista = [4, 2, 2, 8, 3, 3, 1]
lista_ordenada = counting_sort(lista)
print("Lista original:", lista)
print("Lista ordenada:", lista_ordenada)

# 7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.

mi_lista = [10, 'manzana', 3, 'banana', 25, 'uva', 1, 'pera']

numeros = [elemento for elemento in mi_lista if isinstance(elemento, (int, float))]
cadenas = [elemento for elemento in mi_lista if isinstance(elemento, str)]

numeros.sort()

cadenas.sort()

mi_lista_ordenada = numeros + cadenas

print(mi_lista_ordenada)

# 8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def merge_sort_numbers(numbers):
    merge_sort(numbers)

numbers = [12, 11, 13, 5, 6, 7]
print("Lista original:", numbers)
merge_sort_numbers(numbers)
print("Lista ordenada:", numbers)
