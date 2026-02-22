import pygame
from .base import ScreenBase
from ..ui.button import Button

class MainMenuScreen(ScreenBase):
    def __init__(self, manager, screen_size):
        super().__init__(manager, screen_size)

        self.font_title = pygame.font.SysFont(None, 48)
        self.font_button = pygame.font.SysFont(None, 28)

        cx = screen_size[0] // 2
        cy = screen_size[1] // 2 - 40

        self.buttons = [
            Button("Start Game", (cx, cy), (180, 40), self.start_game, self.font_button),
            Button("High Score", (cx, cy + 60), (180, 40), self.go_high_score, self.font_button),
            Button("Exit", (cx, cy + 120), (180, 40), self.exit_game, self.font_button),
        ]

    def start_game(self):
        self.manager.go_to("game")

    def go_high_score(self):
        self.manager.go_to("high_score")

    def exit_game(self):
        pygame.quit()
        raise SystemExit

    def handle_event(self, event):
        for b in self.buttons:
            b.handle_event(event)

    def update(self, dt): pass

    def draw(self, surface):
        surface.fill((30, 30, 40))
        title = self.font_title.render("Galaxy Runner", True, (255,255,255))
        surface.blit(title, (self.screen_width//2 - 150, 120))

        for b in self.buttons:
            b.draw(surface)