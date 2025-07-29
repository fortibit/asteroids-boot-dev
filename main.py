import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fill_screen = pygame.Surface.fill(screen, (0, 0, 0))
    refresh = pygame.display.flip()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        fill_screen
        refresh


def check_close_button():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return


if __name__ == "__main__":
    main()
