from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*

import sys
import math

WINDOW_SIZE=500
FPS=60
gx=0.0
gy=0.0
angle=40.0
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawrect(x,y):
	
	glBegin(GL_POLYGON)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(x-100,y+50)
	glVertex2f(x+100,y+50)
	glVertex2f(x+125,y-10)
	glVertex2f(x+125,y-100)
	glVertex2f(x-100,y-100)
	glEnd()
def drawcircle(x,y,s):
	global angle
	if s==0:
		y=y-100-35
		x=x-50
	else:
		y=y-100-35
		x=x+50
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(0.0,0.0,0.0)
	glVertex2f(x,y)
	for i in range(0,361,1):
		glVertex2f(35*math.cos(math.pi*i/180.0)+x,35*math.sin(math.pi*i/180.0)+y)
	glEnd()
	glLineWidth(2.0)
	glBegin(GL_LINES)
	glColor3f(0.0,1.0,1.0)
	glVertex2f(x,y)
	glVertex2f(35*math.cos(math.pi*angle/180.0)+x,35*math.sin(math.pi*angle/180.0)+y)
	glEnd()
def drawcar():
	global gx
	global gy
	glClear(GL_COLOR_BUFFER_BIT)
	drawrect(gx,gy)
	drawcircle(gx,gy,0)
	drawcircle(gx,gy,1)
	glutSwapBuffers()
	
def animate(temp):
	global gx,gy,WINDOW_SIZE,angle
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()
	if (gx+125<WINDOW_SIZE):
		gx=gx+3
		angle=angle-5
	else:
        	gx=-400
        
	
	
	

def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("Car")
	glutDisplayFunc(drawcar)
	glutIdleFunc(drawcar)
	glutTimerFunc(0,animate,0)
	init()
	glutMainLoop()
main()


