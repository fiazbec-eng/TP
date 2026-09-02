import pygame
import random
import sys

pygame.init()

ANCHO = 800
ALTO = 600

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Legión Caída")

RELOJ = pygame.time.Clock()

NEGRO = (10, 5, 3)
ROJO = (255, 46, 23)
ROJO_OSCURO = (74, 5, 5)
ROJO_MEDIO = (140, 13, 13)
HUESO = (233, 217, 200)
HUESO_OSCURO = (166, 141, 124)

fuente_titulo = pygame.font.Font(None, 58)
fuente_subtitulo = pygame.font.Font(None, 25)
fuente_boton = pygame.font.Font(None, 30)

botones = [
    "Jugar",
    "Personajes",
    "Insignias",
    "Estadísticas",
    "Reiniciar Juego"
]

boton_ancho = 420
boton_alto = 55
espacio = 14

inicio_x = (ANCHO - boton_ancho) // 2
inicio_y = 255
particulas = []

for i in range(28):
    particulas.append({
        "x": random.randint(0, ANCHO),
        "y": random.randint(ALTO, ALTO + 300),
        "velocidad": random.uniform(0.5, 1.5),
        "tamaño": random.randint(2, 4),
        "desplazamiento": random.uniform(-0.5, 0.5)
    })


def dibujar_fondo():
    ventana.fill(NEGRO)

    for radio in range(350, 0, -10):
        intensidad = int(50 * (1 - radio / 350))
        superficie = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)

        pygame.draw.ellipse(
            superficie,
            (140, 13, 13, intensidad),
            (
                ANCHO // 2 - radio,
                ALTO - radio // 2,
                radio * 2,
                radio
            )
        )

        ventana.blit(superficie, (0, 0))


def dibujar_particulas():
    for p in particulas:
        pygame.draw.circle(
            ventana,
            ROJO,
            (int(p["x"]), int(p["y"])),
            p["tamaño"]
        )

        p["y"] -= p["velocidad"]
        p["x"] += p["desplazamiento"]

        if p["y"] < -10:
            p["y"] = ALTO + random.randint(10, 100)
            p["x"] = random.randint(0, ANCHO)


def dibujar_sello():
    centro_x = ANCHO // 2
    centro_y = 105

    pygame.draw.circle(
        ventana,
        ROJO,
        (centro_x, centro_y),
        46,
        2
    )

    pygame.draw.line(
        ventana,
        ROJO_MEDIO,
        (centro_x, centro_y - 42),
        (centro_x, centro_y + 42),
        1
    )

    pygame.draw.line(
        ventana,
        ROJO_MEDIO,
        (centro_x - 42, centro_y),
        (centro_x + 42, centro_y),
        1
    )

    pygame.draw.line(
        ventana,
        ROJO_MEDIO,
        (centro_x - 30, centro_y - 30),
        (centro_x + 30, centro_y + 30),
        1
    )

    pygame.draw.line(
        ventana,
        ROJO_MEDIO,
        (centro_x + 30, centro_y - 30),
        (centro_x - 30, centro_y + 30),
        1
    )

    puntos = [
        (centro_x, centro_y - 30),
        (centro_x + 20, centro_y + 15),
        (centro_x - 23, centro_y - 13),
        (centro_x + 23, centro_y - 13),
        (centro_x - 20, centro_y + 15)
    ]

    pygame.draw.polygon(
        ventana,
        ROJO,
        puntos,
        1
    )


def dibujar_texto():
    titulo = fuente_titulo.render(
        "REQUIEM",
        True,
        HUESO
    )

    titulo_rect = titulo.get_rect(
        center=(ANCHO // 2, 175)
    )

    ventana.blit(titulo, titulo_rect)

    subtitulo = fuente_subtitulo.render(
        "el infierno espera tu mando",
        True,
        HUESO_OSCURO
    )

    subtitulo_rect = subtitulo.get_rect(
        center=(ANCHO // 2, 215)
    )

    ventana.blit(subtitulo, subtitulo_rect)


def dibujar_botones(mouse_pos):
    for i, texto in enumerate(botones):

        y = inicio_y + i * (boton_alto + espacio)

        rect = pygame.Rect(
            inicio_x,
            y,
            boton_ancho,
            boton_alto
        )

        hover = rect.collidepoint(mouse_pos)

        if i == 0:
            color = (179, 18, 18)
            borde = ROJO
        else:
            color = (100, 10, 10)
            borde = (150, 20, 20)

        if hover:
            color = (200, 20, 20)
            borde = ROJO

        pygame.draw.rect(
            ventana,
            color,
            rect,
            border_radius=3
        )

        pygame.draw.rect(
            ventana,
            borde,
            rect,
            1,
            border_radius=3
        )

        if hover:
            pygame.draw.rect(
                ventana,
                ROJO,
                (
                    rect.x,
                    rect.y,
                    4,
                    rect.height
                )
            )

        texto_render = fuente_boton.render(
            texto,
            True,
            HUESO
        )

        texto_rect = texto_render.get_rect(
            midleft=(rect.x + 25, rect.centery)
        )

        ventana.blit(
            texto_render,
            texto_rect
        )


ejecutando = True

while ejecutando:

    mouse_pos = pygame.mouse.get_pos()

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:

                for i, texto in enumerate(botones):

                    y = inicio_y + i * (boton_alto + espacio)

                    rect = pygame.Rect(
                        inicio_x,
                        y,
                        boton_ancho,
                        boton_alto
                    )

                    if rect.collidepoint(evento.pos):
                        print("Seleccionaste:", texto)

                        if texto == "Jugar":
                            print("Comenzando juego...")

                        elif texto == "Personajes":
                            print("Abriendo personajes...")

                        elif texto == "Insignias":
                            print("Abriendo insignias...")

                        elif texto == "Estadísticas":
                            print("Abriendo estadísticas...")

                        elif texto == "Reiniciar Juego":
                            print("Reiniciando juego...")

    dibujar_fondo()
    dibujar_particulas()
    dibujar_sello()
    dibujar_texto()
    dibujar_botones(mouse_pos)

    pygame.display.flip()

    RELOJ.tick(60)

pygame.quit()
sys.exit()