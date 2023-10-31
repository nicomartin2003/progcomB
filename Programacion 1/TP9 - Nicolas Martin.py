# 1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona.
# •	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

from Clase_Person import Person

Person1 = Person("Nicolas", 20, 45144162)
Person2 = Person("Valentin", 15, 45123654)
Person3 = Person("Mercedes", 18, 45869579)

Person1.Show()
Person2.Show()
Person3.Show()

print(f"{Person1.Is_of_legal_age()}")
print(f"{Person2.Is_of_legal_age()}")
print(f"{Person3.Is_of_legal_age()}")

# 2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

from Clase_Cuenta import Cuenta

access = Cuenta()
access.show()
while True:
    print("1. Ingresar dinero")
    print("2. retirar dinero")
    print("3. Salir")
    option = int(input("Ingrese una opcion: "))
    if option == 1:
        amount = float(input("Cuanto dinero desea ingresar: "))
        access.get_into(amount)
    elif option == 2:
        amount = float(input("Cuanto dinero desea retirar: "))
        access.withdraw(amount)
    else:
        print("Adios!")
        break

# 3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).

from Clase_Triangulo import Triangulo

lado1 = float(input("Ingrese el valor del primer lado: "))
lado2 = float(input("Ingrese el valor del segundo lado: "))
lado3 = float(input("Ingrese el valor del tercer lado: "))

triangulo = Triangulo(lado1, lado2, lado3)

lado_mayor = triangulo.obtener_lado_mayor()
tipo = triangulo.tipo_triangulo()

print(f"El lado más largo del triángulo es: {lado_mayor}")
print(f"El triángulo es de tipo: {tipo}")

# 4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
# •	Añadir contacto
# •	Lista de contactos
# •	Buscar contacto
# •	Editar contacto
# •	Cerrar agenda

from Clase_admAgenda import Contacto
from Clase_admAgenda import Agenda

agenda = Agenda()
agenda.menu()