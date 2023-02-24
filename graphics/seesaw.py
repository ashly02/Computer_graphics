from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math


y=0
WS=500

DIR=1
FPS=60
angle1=0
angle2=180
x=300
def init():
    glClearColor(0,0,0,0)
    gluOrtho2D(-WS,WS,-WS,WS)
    

    
    
def tri():
    glColor3f(1,0,0)
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(-90,-100)
    glVertex(90,-100)
    glEnd()
    



def display():
    global x
    global y
    global angle1,angle2
    glClear(GL_COLOR_BUFFER_BIT)
    x1=x*math.cos(math.pi*angle1/180)
    y1=x*math.sin(math.pi*angle1/180)
    glColor3f(0,0,1)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x1,y1)
    glEnd()
    x2=x*math.cos(math.pi*angle2/180)
    y2=x*math.sin(math.pi*angle2/180)
    glColor3f(0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(x2,y2)
    glEnd()
    
    x3=100*math.cos(math.pi*(angle1+90)/180)+x1
    y3=100*math.sin(math.pi*(angle1+90)/180)+y1
    x4=140*math.cos(math.pi*(angle1+135)/180)+x1
    y4=140*math.sin(math.pi*(angle1+135)/180)+y1
    x5=100*math.cos(math.pi*(angle1+180)/180)+x1
    y5=100*math.sin(math.pi*(angle1+180)/180)+y1
    
    glBegin(GL_QUADS)
    glVertex2f(x1,y1)
    glVertex2f(x3,y3)
    glVertex2f(x4,y4)
    glVertex2f(x5,y5)
    glEnd()
    
    x6=100*math.cos(math.pi*(angle2-90)/180)+x2
    y6=100*math.sin(math.pi*(angle2-90)/180)+y2
    x7=(140)*math.cos(math.pi*(angle2-135)/180)+x2
    y7=(140)*math.sin(math.pi*(angle2-135)/180)+y2
    x8=100*math.cos(math.pi*(angle2-180)/180)+x2
    y8=100*math.sin(math.pi*(angle2-180)/180)+y2
    
    glBegin(GL_QUADS)
    glVertex2f(x2,y2)
    glVertex2f(x6,y6)
    glVertex2f(x7,y7)
    glVertex2f(x8,y8)
    glEnd()
    
    tri()
    glutSwapBuffers()

def animate(temp):
    
    global angle1,angle2,DIR
    if DIR==1:
        if(angle1>=40):
            DIR=0
        else:
            angle1=angle1+2
            angle2=angle2+2
    if DIR==0:
        if(angle2<=140):
            DIR=1
        else:
            angle1=angle1-2
            angle2=angle2-2
    glutTimerFunc(int(1000/FPS),animate,0)
    glutPostRedisplay()


    
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowPosition(0,0)
    glutInitWindowSize(WS,WS)
    glutCreateWindow("seesaw")
    glutDisplayFunc(display)
    glutTimerFunc(0,animate,0)
    glutIdleFunc(display)
    init()
    glutMainLoop()
main()
