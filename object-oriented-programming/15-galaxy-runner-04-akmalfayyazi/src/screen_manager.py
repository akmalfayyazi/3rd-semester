import pygame


class ScreenManager:
    def __init__(self, initial_screen):
        self.current_screen = initial_screen

    def switch_to(self, new_screen):
        self.current_screen = new_screen

    def handle_event(self, event: pygame.event.Event):
        self.current_screen.handle_event(event)

    def update(self, dt: float):
        self.current_screen.update(dt)

    def draw(self, surface: pygame.Surface):
        self.current_screen.draw(surface)