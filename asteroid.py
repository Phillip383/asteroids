import circleshape
import pygame
import constants
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           pygame.color.Color("white"), 
                           self.position,
                           self.radius,
                           2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            a1 = Asteroid(self.position.x, self.position.y,  self.radius - constants.ASTEROID_MIN_RADIUS)
            a2 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
            random_angle = random.uniform(20, 50)
            a1.velocity = self.velocity.rotate(random_angle) * 1.2
            a2.velocity = self.velocity.rotate(-random_angle) * 1.2