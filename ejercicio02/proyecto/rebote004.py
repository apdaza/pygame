import sys, pygame
from pygame.locals import *

size = width, height = 640, 400
speed = [0, 0]
screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    ball = pygame.image.load("imagenes/basketball.png")
    ballrect = ball.get_rect()
    ballrect.left = (width/2)-(ballrect.width/2)
    ballrect.top = (height/2)-(ballrect.height/2)

    court = pygame.image.load("imagenes/cancha.png")
    courtrect = court.get_rect()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key==K_UP:
                    ballrect.centery = ballrect.centery - 10
                if event.key==K_DOWN:
                    ballrect.centery = ballrect.centery + 10
                if event.key==K_LEFT:
                    ballrect.centerx = ballrect.centerx - 10
                if event.key==K_RIGHT:
                    ballrect.centerx = ballrect.centerx + 10
        
        ballrect = ballrect.move(speed)
        
        if ballrect.top < height/3 or ballrect.bottom > height:
            speed[1] = -speed[1]
                
        screen.blit(court, courtrect)
        screen.blit(ball, ballrect)
        
        pygame.display.update()

if __name__ == '__main__': 
    main()
