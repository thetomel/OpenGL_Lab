from Mesh3D import *
class Cube(Mesh3D):
    def __init__(self, draw_type, filename):
        self.vertices= [ #Points in 3Dplane
            (-0.5, -0.5,  0.5), ( 0.5, -0.5,  0.5), ( 0.5,  0.5,  0.5), (-0.5,  0.5,  0.5),
            (-0.5, -0.5, -0.5), (-0.5,  0.5, -0.5), ( 0.5,  0.5, -0.5), ( 0.5, -0.5, -0.5),
            (-0.5,  0.5, -0.5), (-0.5,  0.5,  0.5), ( 0.5,  0.5,  0.5), ( 0.5,  0.5, -0.5),
            (-0.5, -0.5, -0.5), ( 0.5, -0.5, -0.5), ( 0.5, -0.5,  0.5), (-0.5, -0.5,  0.5),
            ( 0.5, -0.5, -0.5), ( 0.5,  0.5, -0.5), ( 0.5,  0.5,  0.5), ( 0.5, -0.5,  0.5),
            (-0.5, -0.5, -0.5), (-0.5, -0.5,  0.5), (-0.5,  0.5,  0.5), (-0.5,  0.5, -0.5)]
        self.uvs = [ #Mapping TExture
            (0,0), (1,0), (1,1), (0,1),
            (1,0), (1,1), (0,1), (0,0),
            (0,1), (0,0), (1,0), (1,1),
            (1,1), (0,1), (0,0), (1,0),
            (1,0), (1,1), (0,1), (0,0), 
            (0,0), (1,0), (1,1), (0,1) ]

        self.triangles = [] #index to points, easy connect
        for i in range(0, 24, 4):
            self.triangles.extend([i, i+1, i+2, i, i+2, i+3])

        self.texture = pygame.image.load(filename)
        self.draw_type = draw_type
        self.init_texture()

        Mesh3D.texture = pygame.image.load(filename)
        Mesh3D.draw_type = draw_type
        Mesh3D.init_texture(self)
