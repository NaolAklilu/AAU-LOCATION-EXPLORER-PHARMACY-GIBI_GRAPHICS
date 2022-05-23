import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
from figure_renderer import HouseDesign


def init():
    pygame.init()
    display = (600, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)
    glRotatef(-90, 2, 0, 0)


def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1,1, -10, -45)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        HouseDesign()
        pygame.display.flip()
        pygame.time.wait(10)

main()