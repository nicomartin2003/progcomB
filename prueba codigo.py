num = 1
contador_pares_total = 0
contador_impares_total = 0

while num != 0:
    num = int(input("Ingrese un número (0 para terminar): "))
    contador_pares = 0
    contador_impares = 0    

    if num == 0:
        break
    
    num_str = str(abs(num))  
    
    for digito in num_str:
        digito = int(digito)
        if digito % 2 == 0:
            contador_pares += 1
            contador_pares_total += 1
        else:
            contador_impares += 1
            contador_impares_total += 1
    print(f"La cantidad de dígitos pares fue de {contador_pares} y la cantidad de dígitos impares fue de {contador_impares}")

print(f"La cantidad total de dígitos pares fue de {contador_pares_total} y la cantidad total de dígitos impares fue de {contador_impares_total}")
