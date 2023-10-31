from Motorobike import Motorobike


my_motorbike = Motorobike("red", "317 GQO", 10, 2, "Kayazaki", "Ninja", 1984, 335, 164)
my_motorbike2 = Motorobike("black", "280 AJG", 11, 3, "Dukati", "Panigale V4", 2018, 300, 177)

print("Metodo de arranque ")
my_motorbike.arrancar()
my_motorbike.arrancar()

print("Metodo de detener ")
my_motorbike.detener()
my_motorbike.detener()

my_motorbike.precio = 7418640
my_motorbike.precio_moto()
my_motorbike2.precio_moto()


