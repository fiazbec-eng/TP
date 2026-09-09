import pygame

pygame.init()

WIDTH = 1350
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beat Em Up")

background = pygame.image.load("fondos/fondo.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

clock = pygame.time.Clock()


class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 90)

        self.speed = 5
        self.health = 150
        self.max_health = 150

        self.direction = "right"

        # SALTO
        self.gravity = 0.7
        self.jump_power = -14
        self.velocity_y = 0
        self.on_ground = True

        self.attacking = False
        self.attack_timer = 0

        self.attack_cooldown = 0
        self.attack_cooldown_time = 0.3

        self.has_hit = False

        self.hurtbox = pygame.Rect(
            x, y, 60, 90
        )

        self.hitbox = pygame.Rect(
            0, 0, 0, 0
        )

    def update(self, dt):

        keys = pygame.key.get_pressed()

        # MOVIMIENTO IZQUIERDA
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = "left"

        # MOVIMIENTO DERECHA
        if keys[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = "right"

        # GRAVEDAD
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        # SUELO
        ground_y = HEIGHT - self.rect.height

        if self.rect.y >= ground_y:
            self.rect.y = ground_y
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        # LIMITAR MOVIMIENTO HORIZONTAL
        self.rect.x = max(
            0,
            min(WIDTH - self.rect.width, self.rect.x)
        )

        # ACTUALIZAR HURTBOX
        self.hurtbox.topleft = self.rect.topleft

        # COOLDOWN DEL ATAQUE
        if self.attack_cooldown > 0:
            self.attack_cooldown -= dt

        # ATAQUE
        if self.attacking:

            if self.direction == "right":
                self.hitbox.topleft = (
                    self.rect.right,
                    self.rect.y + 20
                )
            else:
                self.hitbox.topleft = (
                    self.rect.left - 50,
                    self.rect.y + 20
                )

            self.attack_timer -= dt

            if self.attack_timer <= 0:
                self.attacking = False
                self.has_hit = False

                self.hitbox = pygame.Rect(
                    0, 0, 0, 0
                )

    # SALTO
    def jump(self):

        if self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False

    # ATAQUE
    def attack(self):

        if self.attack_cooldown > 0:
            return

        if self.attacking:
            return

        self.attacking = True
        self.attack_timer = 0.15
        self.attack_cooldown = self.attack_cooldown_time
        self.has_hit = False

        if self.direction == "right":

            self.hitbox = pygame.Rect(
                self.rect.right,
                self.rect.y + 20,
                50,
                50
            )

        else:

            self.hitbox = pygame.Rect(
                self.rect.left - 50,
                self.rect.y + 20,
                50,
                50
            )

    # DAÑO
    def take_damage(self, damage):

        self.health -= damage

        print("Jugador recibió", damage, "de daño")
        print("Vida del jugador:", self.health)

    # DIBUJAR
    def draw(self):

        pygame.draw.rect(
            screen,
            (0, 100, 255),
            self.rect
        )

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            self.hurtbox,
            2
        )

        if self.attacking:

            pygame.draw.rect(
                screen,
                (255, 255, 0),
                self.hitbox,
                2
            )


class Enemy:
    def __init__(self, x, y):

        self.rect = pygame.Rect(
            x, y, 60, 90
        )

        self.speed = 2

        self.health = 120
        self.max_health = 120

        self.direction = "left"

        self.gravity = 0.7
        self.velocity_y = 0

        self.hurtbox = pygame.Rect(
            x, y, 60, 90
        )

        self.hitbox = pygame.Rect(
            0, 0, 0, 0
        )

        self.attacking = False
        self.attack_timer = 0

        self.attack_cooldown = 0
        self.attack_cooldown_time = 0.8

        self.has_hit = False

    def update(self, player, dt):

        # SEGUIR AL JUGADOR
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
            self.direction = "right"

        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
            self.direction = "left"

        # GRAVEDAD
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        ground_y = HEIGHT - self.rect.height

        if self.rect.y >= ground_y:

            self.rect.y = ground_y
            self.velocity_y = 0

        # LIMITAR MOVIMIENTO
        self.rect.x = max(
            0,
            min(WIDTH - self.rect.width, self.rect.x)
        )

        # ACTUALIZAR HURTBOX
        self.hurtbox.topleft = self.rect.topleft

        # COOLDOWN
        if self.attack_cooldown > 0:
            self.attack_cooldown -= dt

        # DISTANCIA AL JUGADOR
        distance_x = abs(
            self.rect.centerx -
            player.rect.centerx
        )

        # ATACAR
        if distance_x < 100:

            if not self.attacking:
                self.attack()

        # ATAQUE
        if self.attacking:

            if self.direction == "right":

                self.hitbox.topleft = (
                    self.rect.right,
                    self.rect.y + 20
                )

            else:

                self.hitbox.topleft = (
                    self.rect.left - 50,
                    self.rect.y + 20
                )

            self.attack_timer -= dt

            if self.attack_timer <= 0:

                self.attacking = False
                self.has_hit = False

                self.hitbox = pygame.Rect(
                    0, 0, 0, 0
                )

    # ATAQUE DEL ENEMIGO
    def attack(self):

        if self.attack_cooldown > 0:
            return

        self.attacking = True
        self.attack_timer = 0.15
        self.attack_cooldown = self.attack_cooldown_time
        self.has_hit = False

        if self.direction == "right":

            self.hitbox = pygame.Rect(
                self.rect.right,
                self.rect.y + 20,
                50,
                50
            )

        else:

            self.hitbox = pygame.Rect(
                self.rect.left - 50,
                self.rect.y + 20,
                50,
                50
            )

    # DAÑO DEL ENEMIGO
    def take_damage(self, damage):

        self.health -= damage

        print("Enemigo recibió", damage, "de daño")
        print("Vida del enemigo:", self.health)

    # DIBUJAR ENEMIGO
    def draw(self):

        pygame.draw.rect(
            screen,
            (255, 50, 50),
            self.rect
        )

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            self.hurtbox,
            2
        )

        if self.attacking:

            pygame.draw.rect(
                screen,
                (255, 150, 0),
                self.hitbox,
                2
            )


# CREAR JUGADOR Y ENEMIGO
player = Player(200, 300)
enemy = Enemy(900, 300)

# DAÑO
player_damage = 20
enemy_damage = 12

running = True

while running:

    # DELTA TIME
    dt = clock.tick(60) / 1000

    # EVENTOS
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # ATAQUE CON F
            if event.key == pygame.K_f:
                player.attack()

            # SALTO CON SPACE
            if event.key == pygame.K_SPACE:
                player.jump()

    # ACTUALIZAR JUGADOR
    player.update(dt)

    # ACTUALIZAR ENEMIGO
    enemy.update(player, dt)

    # GOLPE DEL JUGADOR AL ENEMIGO
    if player.attacking:

        if not player.has_hit:

            if player.hitbox.colliderect(enemy.hurtbox):

                enemy.take_damage(player_damage)

                player.has_hit = True

    # GOLPE DEL ENEMIGO AL JUGADOR
    if enemy.attacking:

        if not enemy.has_hit:

            if enemy.hitbox.colliderect(player.hurtbox):

                player.take_damage(enemy_damage)

                enemy.has_hit = True

    # DIBUJAR FONDO
    screen.blit(background, (0, 0))

    # DIBUJAR SUELO
    pygame.draw.line(
        screen,
        (100, 100, 100),
        (0, HEIGHT - 1),
        (WIDTH, HEIGHT - 1),
        2
    )

    # DIBUJAR JUGADOR
    player.draw()

    # DIBUJAR ENEMIGO
    enemy.draw()

    # ACTUALIZAR PANTALLA
    pygame.display.flip()


pygame.quit()
