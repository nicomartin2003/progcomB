import Funciones_p2
dna = []
for i in range(6):
    while True:
        row = input(f"Ingrese la secuencia de ADN (A, T, C o G) para la fila{i + 1}: ").upper()
        if len(row) != 6 or not all(base in "ATCG" for base in row):
            print("Entrada no válida. Introduzca una secuencia de ADN válida.")
        else:
            dna.append(row)
            break

if Funciones_p2.is_mutant(dna): 
    print("Este ADN pertenece a un mutante")
else:
    print("Este ADN no pertenece a ningún mutante")

# Mutante:
# ATGCGA
# CAGTGC
# TTATGT
# AGAAGG
# CCCCTA
# TCACTG

# NO Mutante:
# ATGCGA
# CAGTGC
# TTATTT
# AGACGG
# GCGTCA
# TCACTG