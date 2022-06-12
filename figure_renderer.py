from OpenGL.GL import *
from object_constant import *

def HouseDesign():
    glBegin(GL_QUADS)
    for face in base_faces:
        x = 0
        for vertex in face:
            x+=1
            glVertex3fv(base_verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in base_edges:
        for vertex in edge:
            glVertex3fv(base_verticies[vertex])
    glEnd()