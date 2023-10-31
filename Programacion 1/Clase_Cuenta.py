class Cuenta:

    def __init__(self, holder = "", amount = 0):
        self.__holder = holder
        self.__amount = amount

    @property
    def holder(self):
        return self.__holder
    
    @holder.setter
    def holder(self, new_holder):
        self.__holder = new_holder

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, new_amount):
        self.__amount = new_amount

    def show(self):
        while True:
            self.holder = input("Ingrese su nombre: ")
            if self.holder == "":
                print("Ingrese un nombre válido.")
            else:
                print(f"¡Hola, {self.holder}!")
                break 

    def get_into(self, amount):
        if amount > 0:
            self.__amount += amount
            print(f"Se han ingresado ${self.amount}. Nuevo saldo: ${self.__amount}")
        else:
            print("La cantidad introducida es negativa o igual a cero. No se realizará la operación.")

    def withdraw(self, amount):
        if amount > 0:
            self.__amount -= amount
            print(f"Se han retirado ${amount}. Nuevo saldo: ${self.__amount}")
        else:
            print("La cantidad introducida es negativa o igual a cero. No se realizará la operación.")
            