import numpy as np
import colorsys
from math import log, log2
import pygame
from pygame.locals import *

MAX_ITER = 40

def mandelbrot(c):
    z = 0
    n = 0
    while (abs(z)) <= 2 and n < MAX_ITER:
        z = z*z + c
        n += 1

    if (n == MAX_ITER):
        return MAX_ITER

    return n + 1 - log(log2(abs(z)))

def main():
    space_x = -1.9, 0.7
    space_y = -1.5, 1.5
    
    dims = 1000, 1000
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode(dims)
    pygame.display.set_caption('Test')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))

    for xi, x in enumerate(np.linspace(space_x[0], space_x[1], dims[0])):
        for yi, y in enumerate(np.linspace(space_y[0], space_y[1], dims[1])):
            m = mandelbrot(complex(x, y))
            hue = m / MAX_ITER
            saturation = 1
            value = 1 if m < MAX_ITER else 0
            color = colorsys.hsv_to_rgb(hue, saturation, value)
            background.set_at((xi, yi), (color[0]*255, color[1]*255, color[2]*255))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
