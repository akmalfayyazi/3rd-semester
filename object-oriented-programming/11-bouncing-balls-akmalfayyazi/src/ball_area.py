import pygame
from dataclasses import dataclass

@dataclass
class BallArea:
    min_x: int
    min_y: int
    max_x: int
    max_y: int
    fill_color: tuple = (0, 0, 0)
    border_color: tuple = (255, 255, 255)

    def draw(self, surface: pygame.Surface) -> None:
        width = self.max_x - self.min_x
        height = self.max_y - self.min_y

        # Menggambar area berwarna
        pygame.draw.rect(surface, self.fill_color, (self.min_x, self.min_y, width, height))
        # Menggambar garis tepi
        pygame.draw.rect(surface, self.border_color, (self.min_x, self.min_y, width, height), 2)