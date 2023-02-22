class Vehiculo():

    color = "rojo"
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):

    def __init__(self, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada


ferrari = Coche(330, 1800)

print(ferrari.color)