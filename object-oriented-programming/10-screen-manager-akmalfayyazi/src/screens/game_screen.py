import pygame
from .base import ScreenBase
from ..ui.button import Button

class GameScreen(ScreenBase):
    def __init__(self, manager, screen_size):
        super().__init__(manager, screen_size)

        self.font = pygame.font.SysFont(None, 28)

        self.back_button = Button("Back", (70, 30), (100, 36),
                                  self.go_back, self.font)

        self.player_pos = [300, 300]
        self.speed = 200
        self.radius = 20

    def go_back(self):
        self.manager.go_to("main_menu")

    def handle_event(self, event):
        self.back_button.handle_event(event)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_pos[0] -= self.speed * dt
        if keys[pygame.K_RIGHT]:
            self.player_pos[0] += self.speed * dt
        if keys[pygame.K_UP]:
            self.player_pos[1] -= self.speed * dt
        if keys[pygame.K_DOWN]:
            self.player_pos[1] += self.speed * dt

    def draw(self, surface):
        surface.fill((10, 10, 30))
        pygame.draw.circle(surface, (0,200,255),
                           (int(self.player_pos[0]), int(self.player_pos[1])),
                           self.radius)
        self.back_button.draw(surface)