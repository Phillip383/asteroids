import circleshape
import pygame
from constants import *


class Projectile(circleshape.CircleShape):
    def __init__(self, x, y, direction):
        super().__init__(x, y, PROJECTILE_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(direction) * PROJECTILE_SPEED
    
    def draw(self, screen):
        pygame.draw.circle(screen, 
                           pygame.color.Color("blue"),
                           self.position,
                           self.radius,
                           2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)