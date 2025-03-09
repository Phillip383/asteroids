import pygame
from constants import *
import player as plyer
import asteroid
import asteroidfield
import projectile

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    projectiles = pygame.sprite.Group()
    
    projectile.Projectile.containers = (updatables, drawables, projectiles)
    asteroidfield.AsteroidField.containers = (updatables)
    asteroid.Asteroid.containers = (updatables, drawables, asteroids)
    plyer.Player.containers = (updatables, drawables)

    player = plyer.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    
    asteroid_field = asteroidfield.AsteroidField()


    dt = 0
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, pygame.color.Color("black"))
        dt = clock.tick(60) / 1000
        updatables.update(dt)

        for space_rock in asteroids:
            if space_rock.colliding(player):
                pygame.quit()
            if len(projectiles) > 0:
                for bullet in projectiles:
                    if space_rock.colliding(bullet):
                        space_rock.kill()
                        bullet.kill()


        for drawable in drawables:
            drawable.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
