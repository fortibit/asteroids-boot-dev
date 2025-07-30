import pygame
import sys
from constants import *
from player import Player
from bullet import Bullet
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # create sprite groups
    bullets = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # assign sprites to groups
    Bullet.containers = (bullets, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)

    # create asteroid field
    asteroid_field = AsteroidField()

    # create player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # delta time, controls speed of the game
    dt = 0  

    # check for quit button click
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update sprites from updatables group
        updatable.update(dt)

        # check collision between player and asteroid
        for asteroid in asteroids:
            if asteroid.check_collision(player):
                sys.exit("Game over!")

        # add background
        screen.fill("black")

        # draw sprites from drawable group
        for sprite in drawable:
            sprite.draw(screen)

        # refresh screen
        pygame.display.flip()

        #  limit framerate to FPS and return frame time in seconds
        dt = clock.tick(FPS) / 1000 


if __name__ == "__main__":
    main()
