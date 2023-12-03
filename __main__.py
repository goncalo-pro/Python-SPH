import pygame
import sys
import os

from const import *
import setup
import screen
import physics


'''
INITIALIZES PYGAME AND CLOCK, SEARCH PATH, CREATE FONT 
'''
pygame.init()
absolute_path = os.path.dirname(__file__)
relative_path = 'assets/JetBrainsMonoNerdFont-Bold.ttf'
full_path = os.path.join(absolute_path, relative_path)
font = pygame.font.Font(full_path , 18)
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
