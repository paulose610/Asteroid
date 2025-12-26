import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"S-w: {SCREEN_WIDTH} and S-h: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable, drawable, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(),pygame.sprite.Group(),pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)

    game_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        dt = game_clock.tick(60)/1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for u in updatable:
            u.update(dt)
        
        for d in drawable:
            d.draw(screen)
        
        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game Over!!")
                sys.exit()
            for s in shots:
                if s.collides_with(a):
                    s.kill()
                    a.split()

        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
