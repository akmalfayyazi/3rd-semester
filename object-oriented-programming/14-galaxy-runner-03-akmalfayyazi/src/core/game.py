import pygame
from .player import Player
from .starfield import Starfield
from .enemy import Enemy
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
SOUNDS_DIR = os.path.join(ASSETS_DIR, "sounds")

HIT_SOUND_PATH = os.path.join(SOUNDS_DIR, "hit.wav")
SCORE_SOUND_PATH = os.path.join(SOUNDS_DIR, "score.wav")

class Game:
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Buat background bintang
        self.starfield = Starfield(screen_width, screen_height, star_count=100)

        # Buat player di bawah tengah layar
        self.player = Player(
            x=screen_width / 2,
            y=screen_height - 60,
            speed=300,
            screen_width=screen_width,
            lives=3,   # tambahkan ini
        )

        # Buat beberapa enemy
        self.enemies: list[Enemy] = []
        self.enemy_count = 5
        self._create_enemies()

        # --- Inisialisasi sound ---
        pygame.mixer.init()

        self.hit_sound = pygame.mixer.Sound(HIT_SOUND_PATH)
        self.score_sound = pygame.mixer.Sound(SCORE_SOUND_PATH)

        self.background_color = (5, 5, 20)

        pygame.font.init()
        self.hud_font = pygame.font.SysFont(None, 24)

    def _create_enemies(self):
        self.enemies.clear()
        for _ in range(self.enemy_count):
            self.enemies.append(Enemy(self.screen_width, self.screen_height))

    def handle_event(self, event: pygame.event.Event):
        # Tahap 1: belum ada event khusus selain QUIT di main loop
        # Method ini tetap disediakan agar nanti mudah diperluas.
        pass

    def update(self, dt: float):
        self.starfield.update(dt)
        self.player.update(dt)

        # Update semua musuh
        for enemy in self.enemies:
            enemy.update(dt)

            if enemy.is_off_screen():
                enemy.reset()
                self.player.add_score(10)
                self.score_sound.play()

        # Cek tabrakan antara player dan enemy
        self._check_collisions()

    def _check_collisions(self):
        player_rect = self.player.get_rect()

        for enemy in self.enemies:
            if player_rect.colliderect(enemy.get_rect()):
                self.player.lose_life(1)
                enemy.reset()
                self.hit_sound.play()

    def _draw_hud(self, surface: pygame.Surface):
        score_text = self.hud_font.render(f"Score: {self.player.score}", True, (255, 255, 255))
        lives_text = self.hud_font.render(f"Lives: {self.player.lives}", True, (255, 80, 80))

        surface.blit(score_text, (10, 10))
        surface.blit(lives_text, (10, 30))

    def draw(self, surface: pygame.Surface):
        surface.fill(self.background_color)
        self.starfield.draw(surface)

        for enemy in self.enemies:
            enemy.draw(surface)

        self.player.draw(surface)

        # Tambahkan HUD
        self._draw_hud(surface)