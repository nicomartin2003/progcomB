# Función para verificar si una cadena contiene solo letras válidas (A, T, C o G)
def valid_str(string):
    valid_letters = ["A", "T", "C", "G"]
    return all(char in valid_letters for char in string)

# Función para mostrar una matriz
def show_matrix(matrix):
    for row in matrix:
        print(row)

# Función para invertir las filas de una matriz
def invert_rows(matrix):
    return [row[::-1] for row in matrix]

# Función para extraer la diagonal principal de una matriz
def extract_diagonal(matrix):
    return [matrix[i][i] for i in range(6)]

# Función para extraer la diagonal secundaria de una matriz
def extract_secondary_diagonal(matrix):
    return [matrix[i][5 - i] for i in range(6)]

# Función para extraer una diagonal adyacente a la diagonal principal/secundaria
def extract_diagonal_adjacent(matrix, offset):
    return [matrix[i][i + offset] for i in range(5 - offset)]

# Función para extraer una diagonal por debajo de la diagonal principal/secundaria
def extract_diagonal_below(matrix, offset):
    return [matrix[i + offset][i] for i in range(5 - offset)]

# Función para contar secuencias mutantes en una secuencia dada
def count_mutant_sequences(sequence):
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
            if count == 4:
                return 1  # Se encontró una secuencia mutante
        else:
            count = 1
    return 0

# Función principal que verifica si un ADN es mutante o no
def is_mutant(dna):
    # Invertir las filas de la matriz
    inverted_dna = invert_rows(dna)
    mutant_count = 0
    # Extraer y contar secuencias mutantes en varias diagonales y filas/columnas
    diagonals = [
        extract_diagonal(dna),
        extract_secondary_diagonal(dna),
        extract_diagonal_adjacent(dna, 0),
        extract_diagonal_adjacent(dna, 1),
        extract_diagonal_below(dna, 0),
        extract_diagonal_below(dna, 1),
        extract_diagonal_adjacent(inverted_dna, 0),
        extract_diagonal_adjacent(inverted_dna, 1),
        extract_diagonal_below(inverted_dna, 0),
        extract_diagonal_below(inverted_dna, 1)
    ]
    # Sumar el conteo de secuencias mutantes
    mutant_count += sum(count_mutant_sequences(diagonal) for diagonal in diagonals)
    mutant_count += sum(count_mutant_sequences(row) for row in dna)
    mutant_count += sum(count_mutant_sequences(column) for column in zip(*dna))
    # Determinar si el ADN es mutante basado en el conteo
    return mutant_count > 1
