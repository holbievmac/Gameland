import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Spinner Game")

# Cargar la imagen del spinner
spinner_img = pygame.image.load(r'C:\Users\carlo\Downloads\spinner.png')  # Asegúrate de que la ruta esté correctamente escrita
spinner_rect = spinner_img.get_rect(center=(ANCHO // 2, ALTO // 2))

# Variables de rotación
angulo = 0
velocidad_rotacion = 0

# Reloj
clock = pygame.time.Clock()

# Función para rotar una imagen
def rotar_imagen(imagen, rect, angulo):
    """Rotar la imagen mientras mantiene su centro."""
    imagen_rotada = pygame.transform.rotozoom(imagen, -angulo, 1)  # Nota el signo negativo para la dirección correcta
    rect_rotado = imagen_rotada.get_rect(center=rect.center)  # Recalcular el centro para mantenerlo constante
    return imagen_rotada, rect_rotado

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Clic izquierdo aumenta la velocidad
                velocidad_rotacion += 5
            elif event.button == 3:  # Clic derecho disminuye la velocidad
                velocidad_rotacion -= 5

    # Actualizar la rotación
    angulo = (angulo + velocidad_rotacion) % 360  # Asegura que el ángulo no se vuelva demasiado grande
    spinner_rotado, spinner_rect_rotado = rotar_imagen(spinner_img, spinner_rect, angulo)

    # Dibujar
    pantalla.fill((255, 255, 255))  # Fondo blanco
    pantalla.blit(spinner_rotado, spinner_rect_rotado)
    pygame.display.flip()

    # Controlar el tiempo de actualización
    clock.tick(60)
