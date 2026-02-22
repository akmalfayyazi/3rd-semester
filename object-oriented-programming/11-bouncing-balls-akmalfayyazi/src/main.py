from .ball_area import BallArea
from .ball import Ball
import pygame
import random
import math

class BallSimulation:
    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Bouncing Balls Simulation")

        self.clock = pygame.time.Clock()
        self.running = True

        # Tambahkan area simulasi
        self.area = BallArea(
            
            min_x=50,
            min_y=50,
            max_x=750,
            max_y=550,
            fill_color=(0, 0, 0),
            border_color=(255, 255, 255),
        )

        self.balls: list[Ball] = []
        self._create_initial_balls()

    def run(self):
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)

        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Hanya tambahkan jika klik di dalam area
                if (self.area.min_x < x < self.area.max_x and
                        self.area.min_y < y < self.area.max_y):
                    self._add_ball_at(x, y)

    def _update(self):
        # Update posisi dan tabrakan dengan dinding
        for ball in self.balls:
            ball.collide_with_walls(self.area)
            ball.update()

        # Tabrakan antar bola
        for i in range(len(self.balls)):
            for j in range(i + 1, len(self.balls)):
                self.balls[i].collide_with_ball(self.balls[j])

    def _draw(self):
        self.screen.fill((30, 30, 30))
        self.area.draw(self.screen)

        # Gambar semua bola
        for ball in self.balls:
            ball.draw(self.screen)

        pygame.display.flip()

    def _create_initial_balls(self):
        center_x = (self.area.min_x + self.area.max_x) / 2
        center_y = (self.area.min_y + self.area.max_y) / 2

        # Bola biru yang bergerak
        self.balls.append(
            Ball(
                x=center_x,
                y=center_y,
                radius=20,
                color=(0, 150, 255),
                speed_x=4,
                speed_y=3,
            )
        )

    def _add_ball_at(self, x: int, y: int):
        radius = 15
        speed = 5
        angle_deg = random.randint(0, 359)
        angle_rad = math.radians(angle_deg)

        speed_x = speed * math.cos(angle_rad)
        speed_y = -speed * math.sin(angle_rad)

        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )

        self.balls.append(
            Ball(
                x=x,
                y=y,
                radius=radius,
                color=color,
                speed_x=speed_x,
                speed_y=speed_y,
            )
        )


if __name__ == "__main__":
    sim = BallSimulation()
    sim.run()

from ball_area import BallArea