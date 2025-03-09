import pygame
from constants import *
import player as plyer

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    dt = 0
    clock = pygame.time.Clock()
    plyer.Player.containers = (updatables, drawables)
    player = plyer.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, pygame.color.Color("black"))
        dt = clock.tick(60) / 1000
        updatables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
