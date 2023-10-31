class Motorobike:
    status = "new"
    motor = False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso

    @property
    def private_at(self):
        return self.__private_at
    
    @private_at.setter
    def private_at(self, new_at):
        self.__private_at = new_at

    @private_at.deleter
    def private_at(self):
        del self.__private_at

    def arrancar(self):
        if (self.motor is False):
            self.motor = True
            print("El motor esta encendido ")
        else:
            print("El motor ya esta encendido ")

    def detener(self):
        if (self.motor is True):
            print("El motor esta detenido ")
            self.motor = False
        else:
            print("El motor ya esta detenido ")

    def precio_moto(self):
        print(f"El precio de la moto {self.marca} {self.modelo} es: {self.precio}")
