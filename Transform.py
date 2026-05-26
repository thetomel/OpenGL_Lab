import pygame

class Transform:
    def move (self, amount: pygame.math.Vector3):
         self.position = pygame.math.Vector3(self.position.x + amount.x, self.position.y + amount.y, self.position.z + amount.z)
    def move_X(self, amount):
         self.position = pygame.math.Vector3 (self.position.x + amount, self.position.y, self.position.z)
    def move_Y(self, amount):
         self.position = pygame.math.Vector3 (self.position.x, self.position.y + amount, self.position.z)        
    def __init__(self, position):
         self.set_position(position)
    def get_position(self):
         return self.position
    def set_position(self, position):
         self.position = pygame.math.Vector3(position)