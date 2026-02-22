import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Mouse Event Handling")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 20)
info_text = "Arahkan mouse ke kotak atau klik kotak."

box_rect = pygame.Rect(150, 150, 100, 100)
box_color = BLUE

mouse_inside = False   # <- WAJIB supaya tidak error

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if box_rect.collidepoint(event.pos):
                box_color = (
                    random.randint(0,255),
                    random.randint(0,255),
                    random.randint(0,255),
                )
                info_text = f"Mouse clicked at {event.pos}"

        elif event.type == pygame.MOUSEMOTION:
            if box_rect.collidepoint(event.pos):
                info_text = f"Mouse moving at {event.pos}"
                mouse_inside = True
            else:
                if mouse_inside:
                    info_text = "Mouse left the box area."
                    mouse_inside = False
    
    screen.fill(BLACK)
    pygame.draw.rect(screen, box_color, box_rect)

    label = font.render(info_text, True, WHITE)
    screen.blit(label, (10, 10))

    pygame.display.flip()
    clock.tick(60)