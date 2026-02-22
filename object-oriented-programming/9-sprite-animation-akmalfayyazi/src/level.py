import os
import pygame
from .player import Player

class Level:
    PLAYER_INITIAL_POSITION_X = 50
    PLAYER_INITIAL_POSITION_Y = 50
    ANIMATION_INTERVAL = 0.1

    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("OOP Sprite Animation")

        self.font = pygame.font.SysFont("Arial", 16)
        self.total_frame_count = 0

        base_dir = os.path.dirname(os.path.dirname(__file__))
        sprite_path = os.path.join(base_dir, "assets", "images", "rpg_sprite_walk.png")

        sprite_sheet = pygame.image.load(sprite_path).convert_alpha()

        self.player = Player(
            start_pos=(self.PLAYER_INITIAL_POSITION_X,
                       self.PLAYER_INITIAL_POSITION_Y),
            sprite_sheet=sprite_sheet
        )

        self.animation_accumulator = 0
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_keydown(self, event):
        if event.key == pygame.K_ESCAPE:
            self.running = False
        else:
            self.player.walk(event.key, self.screen.get_rect())

    def handle_keyup(self, event):
        self.player.stop_walking()

    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.animation_accumulator += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event)
                elif event.type == pygame.KEYUP:
                    self.handle_keyup(event)

            while self.animation_accumulator >= self.ANIMATION_INTERVAL:
                self.animation_accumulator -= self.ANIMATION_INTERVAL
                self.total_frame_count += 1
                self.player.animate()

            self.render()

    def render(self):
        self.screen.fill((211, 211, 211))

        label = self.font.render(
            f"Total frames: {self.total_frame_count}", True, (0, 0, 0)
        )
        self.screen.blit(label, (10, 10))

        self.player.draw(self.screen)
        pygame.display.flip()

