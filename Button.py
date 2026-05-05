from OpenGL.GL import *
import pygame
from Utils import *
import Settings

class Button:
    def __init__(self, screen, position, width, height, color, o_color, p_color, on_click):
        self.screen = screen
        self.position = position
        self.on_click = on_click
        self.width = width
        self.height = height
        self.normal_color = color
        self.over_color = o_color
        self.pressed_color = p_color
        self.mouse_down = False
        self.mouse_down = False

    def draw(self, events):
        mouse_pos = pygame.mouse.get_pos()
        mx = map_value (0, Settings.SCREEN_WIDTH, 0, Settings.SCREEN_WIDTH, mouse_pos[0])
        my = map_value (0, Settings.SCREEN_HEIGHT, Settings.SCREEN_HEIGHT, 0, mouse_pos[1])
        glPushMatrix(),
        glLoadIdentity(),
        glColor3f(self.normal_color[0]/255,
              self.normal_color[1]/255,
              self.normal_color[2]/255)
        # Check is mouse over
        is_over = self.position [0] < mx < (self.position [0] + self.width) and \
           self.position [1] < my < (self.position [1] + self.height)
        
        if is_over:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mouse_down = True
                    self.on_click()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                   self.mouse_down = False
        else:
            self.mouse_down = False   
        if is_over:
            if self.mouse_down:
                color = self.pressed_color
            else:
                color = self.over_color
        else:
            color = self.normal_color   
        glColor3f(color[0]/255, color[1]/255, color[2]/255)
        color = self.normal_color   
        glColor3f(color[0]/255, color[1]/255, color[2]/255)
        glBegin (GL_POLYGON)
        glVertex2f(self.position[0], self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1])
        glVertex2f(self.position[0] + self.width, self.position[1] + self.height)
        glVertex2f(self.position[0], self.position[1] + self.height)
        glEnd()
        glPopMatrix()