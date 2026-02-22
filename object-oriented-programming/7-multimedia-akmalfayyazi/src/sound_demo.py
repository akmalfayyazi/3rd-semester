import pygame
import os

pygame.init()
pygame.mixer.init()

BASE = os.path.dirname(os.path.dirname(__file__))
SOUND_PATH = os.path.join(BASE, "assets", "sounds", "laser.wav")

laser_sound = pygame.mixer.Sound(SOUND_PATH)

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Sound Demo")

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                laser_sound.play()

font = pygame.font.SysFont(None, 24)

screen.fill((0, 0, 0))
label = font.render("Tekan SPACE untuk memainkan suara", True, (255, 255, 255))
screen.blit(label, (90, 130))

pygame.display.flip()
clock.tick(60)