from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math
WINDOW_SIZE=500
angle=270.0
FPS=60

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def draw():
	global angle
	glClear(GL_COLOR_BUFFER_BIT)
	x=0
	y=0
	x1=200*math.cos(math.pi*angle/180)
	y1=200*math.sin(math.pi*angle/180.0)
	glLineWidth(5.0)
	glBegin(GL_LINES)
	glColor3f(0.0,0.0,0.0)
	glVertex2f(x,y)
	glVertex2f(x1,y1)
	glEnd()
	x2=50*math.cos(math.pi*angle/180)+x1
	y2=50*math.sin(math.pi*angle/180)+y1
	x3=50*math.cos(math.pi*(angle+120)/180)+x1
	y3=50*math.sin(math.pi*(angle+120)/180)+y1
	x4=50*math.cos(math.pi*(angle+240)/180)+x1
	y4=50*math.sin(math.pi*(angle+240)/180)+y1
	glBegin(GL_TRIANGLES)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glVertex2f(x4,y4)
	glEnd()
	
	glutSwapBuffers()
def animate(temp):
	global angle
	angle=angle+1
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()
	


def main():
	glutInit(sys.argv)
	glutInitWindowPosition(0,0)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("Needle")
	glutDisplayFunc(draw)
	glutIdleFunc(draw)
	glutTimerFunc(0,animate,0)
	init()
	glutMainLoop()
main()
