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
        dt = clock.tick(60) / 1000 # return frame time in seconds


if __name__ == "__main__":
    main()
