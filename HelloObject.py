from Object import *

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
pygame.display.set_caption('OpenGL in Python - Lab 3')
done = False
white = pygame.Color(255,255,255)
gluPerspective(60, (screen_width/screen_height),0.1,100.0)
glTranslatef(0.0, 0.0, -3)
glEnable(GL_DEPTH_TEST)
cube = Object("Cube")
cube.add_component(Transform((0,0,-0.1)))
cube.add_component(Cube(GL_POLYGON, "./texture.png")) #ToDo - change to Vars, pathlib
glEnable(GL_LIGHTING)
clock = pygame.time.Clock()
fps = 60

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cube.update()
    glRotatef(0.01, 0.11, 0, 0.1)
    pygame.display.flip()
    clock.tick(fps)
    print( 'tick={}, fps={}'.format(clock.tick(), clock.get_fps()))
pygame.quit()