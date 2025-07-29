import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    refresh = pygame.display.flip()
    clock = pygame.time.Clock()
    dt = 0  # delta time

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        refresh
        #  limit framerate to 60 FPS and return frame time in seconds
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()
