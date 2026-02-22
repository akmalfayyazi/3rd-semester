from __future__ import annotations
import pygame
from dataclasses import dataclass
from .ball_area import BallArea
import math

@dataclass
class Ball:
    x: float
    y: float
    radius: float
    color: tuple
    speed_x: float = 0.0
    speed_y: float = 0.0

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius))

    def update(self) -> None:
        self.x += self.speed_x
        self.y += self.speed_y

    def collide_with_walls(self, area: BallArea) -> None:
        # Cek kiri/kanan
        if self.x - self.radius < area.min_x or self.x + self.radius > area.max_x:
            self.speed_x = -self.speed_x

        # Cek atas/bawah
        if self.y - self.radius < area.min_y or self.y + self.radius > area.max_y:
            self.speed_y = -self.speed_y

    def collide_with_ball(self, other: "Ball") -> None:
        dx = other.x - self.x
        dy = other.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance == 0:
            return

        if distance < self.radius + other.radius:
            # Sederhana: tukar arah (pantulan kasar)
            self.speed_x = -self.speed_x
            self.speed_y = -self.speed_y
            other.speed_x = -other.speed_x
            other.speed_y = -other.speed_y