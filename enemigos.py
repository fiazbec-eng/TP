import pygame, random
#from jugadores import vida_1, vida_2

class Enemigo():
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

class OrcoRojo(Enemigo):
    def __init__(self, nombre, vida):
        self.nombre 

class esqueletoNegro(Enemigo):
    def __init__(self):
        super().__init__()

orco = OrcoRojo("Orco Rojo", 100)
en = esqueletoNegro()

enemigos = [orco, en]
enemigo = random.choice(enemigos)

print("Te ataca", enemigo.nombre)




def enemigos():
    while vida_1 != 0:
        pass
