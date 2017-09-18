import sys, pygame

size = width, height = 640, 400

screen = pygame.display.set_mode(size)

def main():
    pygame.init()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()

if __name__ == '__main__': 
    main()
