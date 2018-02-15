from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import  *
import OpenGL.GLUT

def draw ():
    #elbta3a bta3et el 7la2a aw bta3t super man
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)

    glVertex(.1, .3)
    glVertex(-.1, .3)
    glVertex(-.2, -.4)
    glVertex(.2, -.4)
    glEnd()
    glFlush()

    #main body
    glColor(.4,.5,.8)
    glBegin(GL_POLYGON)
    glVertex(.1,.3)
    glVertex(.1,-.3)
    glVertex(-.1,-.3)
    glVertex(-.1,.3)
    glEnd()
    glFlush()
    # neck
    glColor(.4, .5, .8)
    glBegin(GL_POLYGON)
    glVertex(.05, .38)
    glVertex(.05, .3)
    glVertex(-.05, .3)
    glVertex(-.05, .38)
    glEnd()
    glFlush()
    # head
    glColor(.4, .5, .8)
    glBegin(GL_POLYGON)
    glVertex(.2, .58)
    glVertex(.2, .38)
    glVertex(-.2, .38)
    glVertex(-.2, .58)
    glEnd()
    glFlush()
    #right leg
    glColor(.4, .5, .8)
    glBegin(GL_POLYGON)
    glVertex(.1, -.5)
    glVertex(.1, -.3)
    glVertex(.03,-.3)
    glVertex(.03,-.5 )
    glEnd()
    glFlush()
    # left leg
    glColor(.4, .5, .8)
    glBegin(GL_POLYGON)
    glVertex(-.1, -.5)
    glVertex(-.1, -.3)
    glVertex(-.03, -.3)
    glVertex(-.03, -.5)
    glEnd()
    glFlush()
    #right eyes
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(.17,.55)
    glVertex(.17, .50)
    glVertex(.13, .50)
    glVertex(.13,.53)
    glEnd()
    glFlush()
    #right eyes
    glColor(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex(.14,.52)
    glVertex(.14, .50)
    glVertex(.16, .50)
    glVertex(.16,.52)
    glEnd()
    glFlush()
    #left eyes
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(-.17,.55)
    glVertex(-.17, .50)
    glVertex(-.13, .50)
    glVertex(-.13,.53)
    glEnd()
    glFlush()
    glColor(0, 0, 1)
    glBegin(GL_POLYGON)
    glVertex(-.14, .52)
    glVertex(-.14, .50)
    glVertex(-.16, .50)
    glVertex(-.16, .52)
    glEnd()
    glFlush()
    # mouth
    glColor(1, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(.09, .43)
    glVertex(.09, .46)
    glVertex(-.09, .46)
    glVertex(-.09, .43)
    glEnd()
    glFlush()
    # nose
    glColor(0, 1, 1)
    glBegin(GL_POLYGON)
    glVertex(0, .48)
    glVertex(.02, .50)
    glVertex(-.02, .50)
    glEnd()
    glFlush()
    #hand
    glColor(.4, .5, .8)
    glBegin(GL_POLYGON)
    glVertex(.35, .3)
    glVertex(.1, .3)
    glVertex(.1, .25)
    glVertex(.35, .25)
    glEnd()
    glFlush()
    glColor(.4, .5, .8)
    glBegin(GL_POLYGON)
    glVertex(-.35, .3)
    glVertex(-.1, .3)
    glVertex(-.1, .25)
    glVertex(-.35, .25)
    glEnd()
    glFlush()
    # cloth
    glColor(.45, 1, .485)
    glBegin(GL_POLYGON)

    glVertex(0, .08)
    glVertex(.08, .2)
    glVertex(-.08, .2)
    glEnd()
    glFlush()
    #crown
    glColor(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(.2, .58)
    glVertex(.125, .58)
    glVertex(.2, .63)
    glEnd()
    glFlush()
    glColor(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(-.2, .58)
    glVertex(-.125, .58)
    glVertex(-.2, .63)
    glEnd()
    glFlush()
    glColor(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(.120, .58)
    glVertex(-.025, .58)
    glVertex(.050, .63)
    glEnd()
    glFlush()
    glColor(1, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(-.125, .58)
    glVertex(.025, .58)
    glVertex(-.050, .63)
    glEnd()
    glFlush()
    glColor(1, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(.2, .58)
    glVertex(.2,.57)
    glVertex(-.2, .57)
    glVertex2d(-.2,.58)
    glEnd()
    glFlush()


















glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"project")
glutDisplayFunc(draw)

glutMainLoop()






