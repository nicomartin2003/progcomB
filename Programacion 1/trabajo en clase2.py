#Ejercicio 1
for i in range(5):
    num_auxiliar = ""
    str_auxiliar = ""
    men_cod = ""
    cantidad_aux = ""
    cantidad = int(input("Ingrese la cantidad de lugares que se movera: "))
    men = input("Ingrese el mensaje que desee mandar: ")
    abcd = "abcdefghijklmnñopqrstuvwxyz"
    long = len(men)
    list_men = list(men)

    for n in range(long):
        num_auxiliar = abcd.find(list_men[n])
        if list_men[n] in abcd:
            num_auxiliar += cantidad
            if num_auxiliar > 26:
                cantidad_aux = num_auxiliar - 26
                num_auxiliar = 0
                num_auxiliar += cantidad_aux
            str_auxiliar = abcd[num_auxiliar]
            list_men[n] = str_auxiliar
    for c in range(long):
        men_cod += list_men[c]
    print(men_cod)

#Ejercicio 2
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
