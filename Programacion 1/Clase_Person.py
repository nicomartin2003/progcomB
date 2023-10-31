class Person:

    def __init__(self, name='', age=0, ID=0):
        self.__name = name
        self.__age = age
        self.__ID = ID

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def ID(self):
        return self.__ID
    
    @ID.setter
    def ID(self, new_ID):
        self.__ID = new_ID

    def Show(self):
        print(f"Nombre: {self.name} \n Edad: {self.age} \n DNI: {self.ID}")

    def Is_of_legal_age(self):
        legal = True
        if self.__age >= 18:
            legal = True
        else:
            legal = False
        return legal
