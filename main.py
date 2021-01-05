from Engine.src.gl_imports import *
from Sandbox.src.Sanbox import *

w, h = 500, 500

def square():
    glBegin(GL_QUADS)
    glVertex2f(100,100)
    glVertex2f(200,100)
    glVertex2f(200,200)
    glVertex2f(100,200)
    glEnd()

def iterate():
    glViewport(0,0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, w, 0.0, h, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Remove everything from screen (i.e. displays all white)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 0.0, 3.0)
    square()
    glutSwapBuffers()

def Run():
    glutInit() # Initialize a glut instance which will allow us to customize our window
    glutInitDisplayMode(GLUT_RGBA) # Set the display mode to be colored
    glutInitWindowSize(w, h)   # Set the width and height of your window
    glutInitWindowPosition(0, 0)   # Set the position at which this windows should appear
    wind = glutCreateWindow("OpenGL Coding Practice") # Give your window a title
    glutDisplayFunc(showScreen)  # Tell OpenGL to call the showScreen method continuously
    glutIdleFunc(showScreen)     # Draw any graphics or shapes in the showScreen function at all times
    glutMainLoop()

if __name__ == "__main__":
    sb = SandBox()
    Run()
