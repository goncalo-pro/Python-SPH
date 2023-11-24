import pygame

from const import *
import physics

screen = pygame.display.set_mode((X_RES, Y_RES))
pygame.display.set_caption('Fluid Simulator - V3')

def print_particles(font) -> None:
    num = str(len(physics.particles))
    num_text = font.render(f'Particles: {num}', 1, pygame.Color("WHITE"))
    screen.blit(num_text, (10, 30))

def print_fps(font, fps) -> None:
    fps = str(fps)
    fps_text = font.render(f'FPS: {fps}', 1, pygame.Color("WHITE"))
    screen.blit(fps_text, (10,10))

def update(font, fps) -> None:
    screen.fill(BG)
    for particle in physics.particles:
        pygame.draw.circle(screen, particle.color, (particle.x, particle.y), RAD)
    print_fps(font, fps)
    print_particles(font)
    pygame.display.flip()
