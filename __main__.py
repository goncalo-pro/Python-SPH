import pygame
import sys

from const import *
import setup
import screen
import physics

pygame.init()
font = pygame.font.Font("assets/JetBrainsMonoNerdFont-Bold.ttf" , 18)
clock = pygame.time.Clock()

def main() -> None:
    while True:
        clock.tick(FPS)
        fps = int(clock.get_fps())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        physics.update()
        screen.update(font, fps)

if __name__ == '__main__':
    main()
