import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()    
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    gameclock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2) 

    asfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return
        
        
        screen.fill((0,0,1))
  
        updatable.update(dt)
        for ass in asteroids:
            for bullet in shots:
                if ass.coll_check(bullet):
                    bullet.kill()
                    ass.split()


            if ass.coll_check(player):
               print ("Game over!")
               sys.exit()



        for drawablething in drawable:
            drawablething.draw(screen)

        pygame.display.flip()
        dt = gameclock.tick(60)/1000


if __name__ == "__main__":
    main()
