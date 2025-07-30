import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        
        # just kill if asteroid is of kind small
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize new vectors for split asteroids
        random_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(random_angle)
        velocity_2 = self.velocity.rotate(-random_angle)

        self.radius -= ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
        new_asteroid_1.velocity = velocity_1 * ASTEROID_SPLIT_ACCELERATION
        new_asteroid_2.velocity = velocity_2 * ASTEROID_SPLIT_ACCELERATION

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt