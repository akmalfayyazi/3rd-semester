import pygame

class Player:
    ROW_DOWN = 0
    ROW_UP = 1
    ROW_LEFT = 2
    ROW_RIGHT = 3

    TOTAL_FRAMES = 8
    ROWS = 4

    def __init__(self, start_pos, sprite_sheet: pygame.Surface, step_px=10):
        self.sprite_sheet = sprite_sheet
        self.sheet_width, self.sheet_height = self.sprite_sheet.get_size()

        self.frame_width = self.sheet_width // self.TOTAL_FRAMES     # 24 px
        self.frame_height = self.sheet_height // self.ROWS           # 32 px

        self.rect = pygame.Rect(start_pos[0], start_pos[1],
                                self.frame_width, self.frame_height)

        self.current_frame = 0
        self.current_row = self.ROW_DOWN
        self.is_moving = False
        self.step_px = step_px

        self.image = None
        self.update_sprite()

    def walk(self, key, boundary_rect):
        self.is_moving = True
        dx = dy = 0

        if key == pygame.K_DOWN:
            self.current_row = self.ROW_DOWN
            dy = self.step_px
        elif key == pygame.K_UP:
            self.current_row = self.ROW_UP
            dy = -self.step_px
        elif key == pygame.K_LEFT:
            self.current_row = self.ROW_LEFT
            dx = -self.step_px
        elif key == pygame.K_RIGHT:
            self.current_row = self.ROW_RIGHT
            dx = self.step_px
        else:
            self.is_moving = False

        if self.is_moving:
            new_x = self.rect.x + dx
            new_y = self.rect.y + dy

            new_x = max(0, min(new_x, boundary_rect.width - self.rect.width))
            new_y = max(0, min(new_y, boundary_rect.height - self.rect.height))

            self.rect.x = new_x
            self.rect.y = new_y

    def stop_walking(self):
        self.is_moving = False
        self.current_frame = 0
        self.update_sprite()

    def animate(self):
        if self.is_moving:
            self.current_frame = (self.current_frame + 1) % self.TOTAL_FRAMES
            self.update_sprite()

    def update_sprite(self):
        src_rect = pygame.Rect(
            self.current_frame * self.frame_width,
            self.current_row * self.frame_height,
            self.frame_width,
            self.frame_height
        )
        self.image = self.sprite_sheet.subsurface(src_rect)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)