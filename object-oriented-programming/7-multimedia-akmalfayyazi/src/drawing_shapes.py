import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Drawing Shapes")
clock = pygame.time.Clock()
running = True

WHITE  = (255, 255, 255)
RED    = (255,   0,   0)
GREEN  = (0,   255,   0)
BLUE   = (0,     0, 255)
YELLOW = (255, 255,   0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (50, 50, 120, 80))
    pygame.draw.circle(screen, BLUE, (300, 200), 50)
    pygame.draw.line(screen, GREEN, (100, 350), (500, 350), 5)
    pygame.draw.polygon(screen, YELLOW, [(400, 50), (450, 150), (350, 150)])

    pygame.display.flip()
    clock.tick(60)