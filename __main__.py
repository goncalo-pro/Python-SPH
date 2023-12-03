import pygame
import sys

from const import *
import setup
import screen
import physics


'''
INITIALIZES PYGAME, FONT AND CLOCK 
'''
pygame.init()
font = pygame.font.Font("assets/JetBrainsMonoNerdFont-Bold.ttf" , 18)
clock = pygame.time.Clock()

'''
MAIN LOOP
'''
def main() -> None:
    while True:
        clock.tick(FPS)
        fps = int(clock.get_fps())

        '''
        DETECT QUIT
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        physics.update()
        screen.update(font, fps)

if __name__ == '__main__':
    main()
