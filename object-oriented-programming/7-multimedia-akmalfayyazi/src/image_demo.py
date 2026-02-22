import pygame
import os

pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

BASE = os.path.dirname(os.path.dirname(__file__))
IMG_PATH = os.path.join(BASE, "assets", "images", "spaceship.png")

image = pygame.image.load(IMG_PATH).convert_alpha()

image = pygame.transform.scale(image, (80, 80))
x, y = 250, 150

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    screen.blit(image, (x, y))

    pygame.display.flip()
    clock.tick(60)