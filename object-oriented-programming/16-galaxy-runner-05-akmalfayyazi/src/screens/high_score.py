import pygame
from .base import BaseScreen
from ..ui.button import Button
from ..core.high_scores import HighScoreManager

class HighScoreScreen(BaseScreen):
    def __init__(self, manager, screen_width: int, screen_height: int, recent_score: int | None = None):
        super().__init__(manager, screen_width, screen_height)

        self.background_color = (20, 10, 40)
        self.title_font = pygame.font.SysFont(None, 48)
        self.text_font = pygame.font.SysFont(None, 28)

        self.back_button = Button(
            pygame.Rect(20, screen_height - 70, 160, 40),
            "Back to Menu",
            self.text_font,
        )

        self.recent_score = recent_score
        self.high_score_manager = HighScoreManager()

    def handle_event(self, event: pygame.event.Event):
        if self.back_button.handle_event(event):
            from .main_menu import MainMenuScreen
            new_screen = MainMenuScreen(self.manager, self.screen_width, self.screen_height)
            self.manager.switch_to(new_screen)

    def update(self, dt: float):
        pass

    def draw(self, surface: pygame.Surface):
        surface.fill(self.background_color)

        # Judul
        title_surf = self.title_font.render("High Scores", True, (255, 255, 255))
        title_rect = title_surf.get_rect(center=(self.screen_width // 2, 60))
        surface.blit(title_surf, title_rect)

        y = 120

        # Jika ada skor terbaru, tampilkan di atas
        if self.recent_score is not None:
            recent_text = f"Last run score: {self.recent_score}"
            recent_surf = self.text_font.render(recent_text, True, (200, 220, 255))
            recent_rect = recent_surf.get_rect(center=(self.screen_width // 2, y))
            surface.blit(recent_surf, recent_rect)
            y += 40

        # Tampilkan daftar high scores
        scores = self.high_score_manager.get_top_scores(limit=10)
        if scores:
            for idx, entry in enumerate(scores, start=1):
                line = f"{idx}. {entry['name']} - {entry['score']}"
                line_surf = self.text_font.render(line, True, (230, 230, 230))
                line_rect = line_surf.get_rect(center=(self.screen_width // 2, y))
                surface.blit(line_surf, line_rect)
                y += 30
        else:
            no_data = self.text_font.render("Belum ada high score.", True, (200, 200, 200))
            no_data_rect = no_data.get_rect(center=(self.screen_width // 2, y))
            surface.blit(no_data, no_data_rect)
            y += 30

        self.back_button.draw(surface)