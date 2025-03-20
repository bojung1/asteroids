import pygame
from constants import *
import player
from circleshape import *

def main():
    pygame.init()

    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    gameclock = pygame.time.Clock()
    dt = 0

    player1 = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return
        
        screen.fill((0,0,1))
        player1.draw(screen) 
        pygame.display.flip()
        dt = gameclock.tick(60)/1000


if __name__ == "__main__":
    main()
