import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"S-w: {SCREEN_WIDTH} and S-h: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game_clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        dt = game_clock.tick(60)/1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        

if __name__ == "__main__":
    main()
