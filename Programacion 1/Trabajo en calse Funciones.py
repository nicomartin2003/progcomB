import FUncion

count = ""
num = int(input("Numero a procesar: "))

while num != 0:
    print(f"Suma: {FUncion.add_digits(num)}")
    num = int(input("Numero a procesar: "))
    if num == "0":
        break
count = int(count + num)
print(f"La suma de todos los digitos es: {FUncion.add_digits(count)}")
print(f"La suma de todos los numeros ingresados es: ")
