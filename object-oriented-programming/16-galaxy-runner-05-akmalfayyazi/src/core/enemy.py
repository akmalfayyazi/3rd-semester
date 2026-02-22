import pygame
import random


class Enemy:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.width = 30
        self.height = 30
        self.color = (220, 60, 60)

        self.speed_min = 120
        self.speed_max = 260

        self.reset()

    def reset(self):
        # Spawn di posisi x random, di atas layar
        self.x = random.randint(0, self.screen_width)
        self.y = -self.height  # sedikit di atas layar
        self.speed = random.uniform(self.speed_min, self.speed_max)

    def update(self, dt: float, player_x: float | None = None):
        self.y += self.speed * dt
        # Enemy biasa mengabaikan player_x (AI ada di subclass)

    def is_off_screen(self) -> bool:
        return self.y > self.screen_height + self.height

    def get_rect(self) -> pygame.Rect:
        rect = pygame.Rect(0, 0, self.width, self.height)
        rect.centerx = int(self.x)
        rect.centery = int(self.y)
        return rect

    def draw(self, surface: pygame.Surface):
        rect = self.get_rect()
        pygame.draw.rect(surface, self.color, rect)

class SmartEnemy(Enemy):
    """
    Enemy dengan AI sederhana:
    - tetap jatuh ke bawah
    - tetapi x-nya bergerak pelan mendekati posisi player
    """

    def __init__(self, screen_width: int, screen_height: int, tracking_speed: float = 80.0):
        super().__init__(screen_width, screen_height)
        self.tracking_speed = tracking_speed

    def update(self, dt: float, player_x: float | None = None):
        # Tetap panggil update() parent untuk gerakan vertikal
        super().update(dt, player_x)

        if player_x is None:
            return

        # Gerakan horizontal menuju player_x
        if player_x < self.x:
            self.x -= self.tracking_speed * dt
        elif player_x > self.x:
            self.x += self.tracking_speed * dt