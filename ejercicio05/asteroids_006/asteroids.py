import sys, pygame, random
from pygame.locals import *
from ship import Ship
from asteroid import Asteroid

size = width, height = 800, 600
screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sonidos/viento.mp3")
    pygame.mixer.music.play(1)
    background_image = pygame.image.load("imagenes/space.png")
    background_rect = background_image.get_rect()
    
    pygame.display.set_caption( "asteroids" )
    
    ship = Ship(size)
    
    asteroids = []
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        screen.blit(background_image, background_rect)        
        
        ship.update()
        
        if random.randint(0,100) % 25 == 0 and len(asteroids) < 10:
            asteroids.append(Asteroid(size))
            
        for bullet in ship.bullets:
            bullet.update()
            if bullet.alcance == 0:
                ship.bullets.remove(bullet)
            screen.blit(bullet.image, bullet.rect) 
        screen.blit(ship.image, ship.rect)
        
        for asteroid in asteroids:
            asteroid.update()
            screen.blit(asteroid.image, asteroid.rect)
            for bullet in ship.bullets:
                if asteroid.rect.colliderect(bullet.rect):
                    ship.bullets.remove(bullet)
                    if asteroid in asteroids:
                        asteroid.explotar()
                        screen.blit(asteroid.image, asteroid.rect)
                        asteroids.remove(asteroid)
                        
        pygame.display.update()
        pygame.time.delay(10)
            
if __name__ == '__main__': 
    main()
