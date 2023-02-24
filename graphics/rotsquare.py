from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import sys
WINDOW_SIZE=500
angle=45

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawsquare():
	global angle
	glClear(GL_COLOR_BUFFER_BIT)
	x1=300*math.cos(math.pi*angle/180.0)
	y1=300*math.sin(math.pi*angle/180.0)
	x2=300*math.cos(math.pi*(angle+90)/180.0)
	y2=300*math.sin(math.pi*(angle+90)/180.0)
	x3=300*math.cos(math.pi*(angle+180)/180.0)
	y3=300*math.sin(math.pi*(angle+180)/180.0)
	x4=300*math.cos(math.pi*(angle+270)/180.0)
	y4=300*math.sin(math.pi*(angle+270)/180.0)
	glColor3f(1.0,0.0,1.0)
	glBegin(GL_QUADS)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glVertex2f(x4,y4)
	glEnd()
	glutSwapBuffers()
	
def animate(temp):
	global angle
	angle=angle-1
	glutTimerFunc(int(1000/50),animate,0)
	glutPostRedisplay()

	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(0,0)
	glutInitWindowPosition(WINDOW_SIZE,WINDOW_SIZE)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("SQUARE ROTATION")
	glutDisplayFunc(drawsquare)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawsquare)
	init()
	glutMainLoop()
main()
