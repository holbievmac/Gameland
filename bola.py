import pygame
import random

# Inicialización de Pygame
pygame.init()

# Constantes
ANCHO = 800
ALTO = 600
COLOR_FONDO = (0, 0, 0)  # Negro
COLOR_BLOQUE = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Colores aleatorios
COLOR_PELOTA = (255, 255, 255)  # Blanco
COLOR_PALETA = (255, 255, 255)  # Blanco
VELOCIDAD_PELOTA = 5
VELOCIDAD_PALETA = 10
FUENTE_PUNTOS = pygame.font.Font(None, 36)

# Configuración de la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego estilo Atari")

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Clases
class Bloque(pygame.sprite.Sprite):
    def __init__(self, color, ancho, alto):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Pelota(pygame.sprite.Sprite):
    def __init__(self, color, radio):
        super().__init__()
        self.image = pygame.Surface([radio * 2, radio * 2])
        self.image.set_colorkey(COLOR_FONDO)
        pygame.draw.circle(self.image, color, (radio, radio), radio)
        self.rect = self.image.get_rect()
        self.velocidad = [VELOCIDAD_PELOTA, VELOCIDAD_PELOTA]

    def update(self):
        self.rect.x += self.velocidad[0]
        self.rect.y += self.velocidad[1]
        if self.rect.right >= ANCHO or self.rect.left <= 0:
            self.velocidad[0] = -self.velocidad[0]
        if self.rect.top <= 0:
            self.velocidad[1] = -self.velocidad[1]
        if self.rect.bottom > ALTO:
            self.kill()  # Eliminar la pelota si toca el fondo

class Paleta(pygame.sprite.Sprite):
    def __init__(self, color, ancho, alto):
        super().__init__()
        self.image = pygame.Surface([ancho, alto])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = (ANCHO - ancho) // 2
        self.rect.y = ALTO - alto - 10

    def mover(self, movimiento):
        self.rect.x += movimiento
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO

# Función para reiniciar y jugar el juego
def main():
    while True:  # Bucle para reiniciar el juego
        bloques = pygame.sprite.Group()
        pelota = Pelota(COLOR_PELOTA, 10)
        paleta = Paleta(COLOR_PALETA, 100, 10)
        todos_los_sprites = pygame.sprite.Group()
        puntos = 0

        for i in range(6):  # 6 filas de bloques
            for j in range(8):  # 8 bloques por fila
                bloque = Bloque(COLOR_BLOQUE, 80, 30)
                bloque.rect.x = 80 * j
                bloque.rect.y = 30 * i
                bloques.add(bloque)
                todos_los_sprites.add(bloque)

        todos_los_sprites.add(pelota)
        todos_los_sprites.add(paleta)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return  # Salir completamente del programa

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paleta.mover(-VELOCIDAD_PALETA)
            if keys[pygame.K_RIGHT]:
                paleta.mover(VELOCIDAD_PALETA)

            pelota.update()

            # Revisar colisión entre pelota y paleta
            if pygame.sprite.collide_rect(pelota, paleta):
                pelota.velocidad[1] = -pelota.velocidad[1]

            # Revisar colisión entre pelota y bloques
            colisiones = pygame.sprite.spritecollide(pelota, bloques, True)
            if colisiones:
                pelota.velocidad[1] = -pelota.velocidad[1]
                puntos += len(colisiones)

            if not pelota.alive():
                texto_perder = FUENTE_PUNTOS.render("Game Over", True, (255, 0, 0))
                pantalla.blit(texto_perder, (ANCHO // 2 - 100, ALTO // 2))
                pygame.display.flip()
                pygame.time.wait(2000)
                break  # Sale del bucle interno para reiniciar el juego

            pantalla.fill(COLOR_FONDO)
            todos_los_sprites.draw(pantalla)
            texto_puntos = FUENTE_PUNTOS.render(f"Puntos: {puntos}", True, (255, 255, 255))
            pantalla.blit(texto_puntos, (10, 10))
            pygame.display.flip()

            reloj.tick(60)

if __name__ == "__main__":
    main()
