import sys, pygame

size = width, height = 640, 400

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
                
        screen.blit(court, courtrect)
        screen.blit(ball, ballrect)
        
        pygame.display.update()

if __name__ == '__main__': 
    main()
