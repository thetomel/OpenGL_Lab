from Object import *
from Cube import *
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Button import *
import Settings

pygame.init()
screen_width = Settings.SCREEN_WIDTH
screen_height = Settings.SCREEN_HEIGHT
pygame.display.set_caption('OpenGL in Python')
screen = pygame.display.set_mode((screen_width,
                                  screen_height),
                                 DOUBLEBUF | OPENGL)
done = False
white = pygame.Color(255, 255, 255)
green = (0,255,0)
blue = (0,0,255)
objects_3d = []
objects_2d = []
def button_click():
    print("Hello Button")
def set_2d():
    glDisable(GL_DEPTH_TEST)
    glDisable(GL_TEXTURE_2D)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, screen.get_width(), 0, screen.get_height())
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())

def set_3d():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)

cube = Object("Cube")
cube.add_component(Transform((0, 0, -5)))
cube.add_component(Cube(GL_POLYGON, "./texture.png")) #ToDo - change to Vars, pathlib
objects_3d.append(cube)

clock = pygame.time.Clock()
fps = 600


button1 = Object("Button")
button1.add_component(Button(screen, (0,0), 100,50, white, green, blue, button_click))
objects_2d.append(button1)

while not done:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    set_3d()
    for o in objects_3d:
        o.update(events)
    set_2d()
    for o in objects_2d:
        o.update(events)

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()