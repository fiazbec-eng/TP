import pygame, random

class Enemigo():
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida    

class OrcoRojo(Enemigo):
    def __init__(self):
        super().__init__("Orco Rojo", 100)

class Carnicero(Enemigo):
    def __init__(self):
        super().__init__("Carnicero", 100)

class MinotauroNaranja(Enemigo):
    def __init__(self):
        super().__init__("Minotauro Naranja", 100)

class Jokai(Enemigo):
    def __init__(self):
        super().__init__("Jokai", 100)

class HombreLoboRojo(Enemigo):
    def __init__(self):
        super().__init__("HombreLoboRojo", 100)

class Mago(Enemigo):
    def __init__(self):
        super().__init__("Mago", 100)

class Cthulhu(Enemigo):
    def __init__(self):
        super().__init__("Cthulhu", 100)

class Cerbero(Enemigo):
    def __init__(self):
        super().__init__("Cerbero", 100)

class OrcoRojo2(Enemigo):
    def __init__(self):
        super().__init__("Orco Rojo 2", 100)

class Demonio(Enemigo):
    def __init__(self):
        super().__init__("Demonio", 100)

class CaballeroInfernal(Enemigo):
    def __init__(self):
        super().__init__("Caballero Infernal", 100)

class Dragon(Enemigo):
    def __init__(self):
        super().__init__("Dragon", 100)

enemigos_normales = [OrcoRojo, MinotauroNaranja, Jokai, HombreLoboRojo, Demonio, Dragon]
enemigos_jefes = [Carnicero, Cthulhu, Cerbero, OrcoRojo2, CaballeroInfernal]

def crear_enemigos():
    enemigo = random.choice(enemigos_normales)
    v_ataque = 5
    while enemigo.vida != 0:
        pygame.time.set_timer()

        pass
