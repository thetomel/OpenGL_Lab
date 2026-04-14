import pygame
from Mesh3D import *
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,
                                 screen_height),
                                DOUBLEBUF | OPENGL)
# mesh = Mesh3D()
gluPerspective(30, (screen_width/screen_height),0.1,100.0)
glTranslatef(0.0, 0.0, -3)
mesh = Cube()

pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255,255,255)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh.draw()
    glRotatef(0.01, 0.11, 0, 0.1)
    pygame.display.flip()
pygame.quit()