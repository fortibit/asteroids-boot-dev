import pygame
from constants import *
from player import Player
from asteroids import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # create sprite groups
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # assign player to containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)

    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0  # delta time


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update sprites from updatables
        updatable.update(dt)
        screen.fill("black")

        # draw sprites from drawable group
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        #  limit framerate to 60 FPS and return frame time in seconds
        dt = clock.tick(60) / 1000 


if __name__ == "__main__":
    main()
