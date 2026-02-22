import pygame
from .base import ScreenBase
from ..ui.button import Button

class HighScoreScreen(ScreenBase):
    def __init__(self, manager, screen_size):
        super().__init__(manager, screen_size)

        self.font_title = pygame.font.SysFont(None, 36)
        self.font_text = pygame.font.SysFont(None, 24)

        self.back_button = Button("Back", (70, 30), (100, 36),
                                  self.go_back, self.font_text)

        self.scores = [1500, 1100, 900]

    def go_back(self):
        self.manager.go_to("main_menu")

    def handle_event(self, event):
        self.back_button.handle_event(event)

    def update(self, dt): pass

    def draw(self, surface):
        surface.fill((20,20,20))
        title = self.font_title.render("High Scores", True, (255,255,255))
        surface.blit(title, (self.screen_width//2 - 80, 120))

        y = 200
        for s in self.scores:
            txt = self.font_text.render(str(s), True, (220,220,220))
            surface.blit(txt, (self.screen_width//2 - 20, y))
            y += 40

        self.back_button.draw(surface)