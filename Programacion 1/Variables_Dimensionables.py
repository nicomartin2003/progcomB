# # 1)
passengers = []
cities = []

def agregar_pasajero():
    name = input("Ingrese nombre del pasajero: ")
    dni = int(input("Ingrese DNI del pasajero: "))
    destination = input("Ingrese destino del pasajero: ")
    passengers.append((name, dni, destination))
    print("Pasajero agregado correctamente.")

def agregar_ciudad():
    city = input("Ingrese nombre de la ciudad: ")
    country = input("Ingrese nombre del país al que pertenece la ciudad: ")
    cities.append((city, country))
    print("Ciudad agregada correctamente.")

def buscar_ciudad_por_dni():
    dni = int(input("Ingrese DNI del pasajero: "))
    for passenger in passengers:
        if passenger[1] == dni:
            destination = passenger[2]
            print(f"El pasajero {passenger[0]} viajo a {destination} ")
        else:
            print("No se encontró el pasajero con ese DNI.")

def contar_pasajeros_por_ciudad():
    city = input("Ingrese nombre de la ciudad: ")
    contador = 0
    for passenger in passengers:
        if passenger[2] == city:
            contador += 1
    print("Cantidad de pasajeros que viajan a", city + ":", contador)

def buscar_pais_por_dni():
    dni = int(input("Ingrese DNI del pasajero: "))
    for passenger in passengers:
        if passenger[1] == dni:
            destination = passenger[2]
            for city in cities:
                if city[0] == destination:
                    print("El pasajero viaja a", city[1])
                    return
    print("No se encontró el pasajero con ese DNI.")

def contar_pasajeros_por_pais():
    country = input("Ingrese nombre del país: ")
    contador = 0
    for passenger in passengers:
        destination = passenger[2]
        for city in cities:
            if city[0] == destination and city[1] == country:
                contador += 1
    print("Cantidad de pasajeros que viajan a", country + ":", contador)

while True:
    print("MENÚ")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver por DNI de pasajero")
    print("4. Ver cantidad de pasajeros por ciudad")
    print("5. Ver país por DNI de pasajero")
    print("6. Ver cantidad de pasajeros por país")
    print("7. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        agregar_pasajero()
    elif opcion == 2:
        agregar_ciudad()
    elif opcion == 3:
        buscar_ciudad_por_dni()
    elif opcion == 4:
        contar_pasajeros_por_ciudad()
    elif opcion == 5:
        buscar_pais_por_dni()
    elif opcion == 6:
        contar_pasajeros_por_pais()
    elif opcion == 7:
        break
    else:
        print("Opción no válida. Intente nuevamente.")

print("¡Gracias por utilizar el programa!")

# 2)

def get_unique_addresses(sales):
    addresses = set()
    for sale in sales:
        address = sale[3]
        addresses.add(address)
    return list(addresses)

sales = [('Nuria Costa', 5, 1234.5, 'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741')]

addresses = get_unique_addresses(sales)

print("Domicilios de clientes a los que se les debe enviar una factura de compra:")
for address in addresses:
    print(address)

# 3) 

members = {
    1: {
        'nombre': 'Amanda Núñez',
        'fecha_ingreso': '17/03/2009',
        'cuota_al_dia': True
    },
    2: {
        'nombre': 'Bárbara Molina',
        'fecha_ingreso': '17/03/2009',
        'cuota_al_dia': True
    },
    3: {
        'nombre': 'Lautaro Campos',
        'fecha_ingreso': '17/03/2009',
        'cuota_al_dia': True
    }
}

def mostrar_cantidad_socios():
    cantidad_socios = len(members)
    print("Cantidad de socios: ", cantidad_socios)

def registrar_pago_cuotas(member_number):
    if member_number in members:
        member = members[member_number]
        member['cuota_al_dia'] = True
        print("Se han registrado todas las cuotas adeudadas del socio n°", member_number)
    else:
        print("No se encontró un socio con ese número.")

def modificar_fecha_ingreso():
    corrected_date = '14/03/2018'
    for member in members.values():
        if member['fecha_ingreso'] == '13/03/2018':
            member['fecha_ingreso'] = corrected_date
    print("Fecha de ingreso corregida exitosamente para todos los socios que ingresaron el 13/03/2018.")

def dar_de_baja_socio(first_name, last_name):
    for member_number, member in members.items():
        if member['nombre'] == first_name and member['apellido'] == last_name:
            members.pop(member_number)
            print("Socio", first_name, last_name, "dado de baja exitosamente.")
            return
    print("No se encontró un socio con ese nombre y apellido.")

def imprimir_listado_socios():
    print("Listado de socios:")
    for member_number, member in members.items():
        print("Socio n°", member_number)
        print("Nombre:", member['nombre'])
        print("Fecha de ingreso:", member['fecha_ingreso'])
        cuota_estado = "Al día" if member['cuota_al_dia'] else "Adeuda cuotas"
        print("Estado de la cuota:", cuota_estado)
        print()

mostrar_cantidad_socios()

member_number = int(input("Ingrese el número de un socio que ha pagado todas las cuotas adeudadas: "))
registrar_pago_cuotas(member_number)

modificar_fecha_ingreso()

first_name = input("Ingrese el nombre del socio que desea dar de baja: ")
last_name = input("Ingrese el apellido del socio que desea dar de baja: ")
dar_de_baja_socio(first_name, last_name)

imprimir_listado_socios()
