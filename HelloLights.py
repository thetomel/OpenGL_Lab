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


pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255,255,255)
gluPerspective(60, (screen_width/screen_height),0.1,100.0)
glTranslatef(0.0, 0.0, -3)
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glLight(GL_LIGHT0, GL_POSITION, (5,5,5,1))
glLightfv (GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
glEnable(GL_LIGHT0)
glMaterialfv(GL_FRONT, GL_DIFFUSE, (0,1,0,1))

mesh = Cube(GL_POLYGON, "texture.png")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    mesh.draw()
    glRotatef(0.01, 0.11, 0, 0.1)
    pygame.display.flip()
pygame.quit()