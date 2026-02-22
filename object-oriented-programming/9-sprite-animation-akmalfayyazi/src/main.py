import pygame
from .level import Level

def main():
    pygame.init()
    try:
        level = Level()
        level.run()
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()