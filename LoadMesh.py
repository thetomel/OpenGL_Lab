from Mesh3D import *
from OpenGL.GL import *

class LoadMesh(Mesh3D):
    def __init__(self, draw_type, model_filename):
        self.vertices, self.triangles = self.load_drawing(model_filename)
        self.draw_type = draw_type

    def draw(self):
        for t in range(0, len(self.triangles), 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[t]])
            glVertex3fv(self.vertices[self.triangles[t + 1]])
            glVertex3fv(self.vertices[self.triangles[t + 2]])
            glEnd()
        glDisable(GL_TEXTURE_2D)

    def load_drawing(self, filename):
        vertices = []
        triangles = []
        
        with open(filename) as fp:
            line = fp.readline()
            while line:
                if line.startswith("v "):
                    parts = line.split()
                    vx = float(parts[1])
                    vy = float(parts[2])
                    vz = float(parts[3])
                    vertices.append((vx, vy, vz))
                if line.startswith("f "):
                    parts = line.split()
                    for i in range(1, 4):
                        vertex_index = int(parts[i].split('/')[0]) - 1
                        triangles.append(vertex_index)
                
                line = fp.readline()
        
        return vertices, triangles