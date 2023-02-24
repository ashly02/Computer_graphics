from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
FPS = 60
radius = 200
mode = 1

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawStar():
	global radius
	glClear(GL_COLOR_BUFFER_BIT)
	x1=radius*math.cos(math.pi*90/180.0)
	y1=radius*math.sin(math.pi*90/180.0)
	x2=radius*math.cos(math.pi*210/180.0)
	y2=radius*math.sin(math.pi*210/180.0)
	x3=radius*math.cos(math.pi*330/180.0)
	y3=radius*math.sin(math.pi*330/180.0)
	x4=radius*math.cos(math.pi*30/180.0)
	y4=radius*math.sin(math.pi*30/180.0)
	x5=radius*math.cos(math.pi*150/180.0)
	y5=radius*math.sin(math.pi*150/180.0)
	x6=radius*math.cos(math.pi*270/180.0)
	y6=radius*math.sin(math.pi*270/180.0)
	
	glColor3f(1.0,1.0,0.0)
	glBegin(GL_TRIANGLES)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glEnd()
	
	glBegin(GL_TRIANGLES)
	glVertex2f(x4,y4)
	glVertex2f(x5,y5)
	glVertex2f(x6,y6)
	glEnd()
	glutSwapBuffers()
	
def animate(temp):
	global radius,mode
	if mode==1:
		if radius==50:
			mode=0
		else:
			radius=radius-1
	if mode==0:
		if radius==220:
			mode=1
		else:
			radius=radius+1
	glutTimerFunc(int(1000/60),animate,0)
	glutPostRedisplay()

	
		
def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Star")
	glutDisplayFunc(drawStar)
	glutTimerFunc(0,animate,0)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawStar)
	init()
	glutMainLoop()
	
main()
