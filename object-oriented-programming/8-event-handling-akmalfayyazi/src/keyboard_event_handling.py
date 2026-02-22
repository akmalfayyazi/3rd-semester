import pygame
pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Keyboard Event Handling")

circle_x, circle_y = 250, 200
radius = 30
speed = 200

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,220,0)

font = pygame.font.SysFont(None, 20)
info_text = "Gunakan tombol panah untuk menggerakkan lingkaran."

clock = pygame.time.Clock()
running = True

while running:
    dt = clock.tick(60) / 1000.0
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        circle_x -= speed * dt
    if keys[pygame.K_RIGHT]:
        circle_x += speed * dt
    if keys[pygame.K_UP]:
        circle_y -= speed * dt
    if keys[pygame.K_DOWN]:
        circle_y += speed * dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                info_text = "SPACE ditekan!"
            elif event.key == pygame.K_ESCAPE:
                running = False
    circle_x = max(radius, min(circle_x, 500 - radius))
    circle_y = max(radius, min(circle_y, 400 - radius))

    screen.fill(BLACK)
    pygame.draw.circle(screen, GREEN, (int(circle_x), int(circle_y)), radius)

    label = font.render(info_text, True, WHITE)
    screen.blit(label, (10, 10))

    pygame.display.flip()
