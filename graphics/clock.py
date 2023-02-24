from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE=500
x=0.0
y=0.0
m=90.0
s=90.0
FPS=60
def init():
	glClearColor(0.0,0.0,0.0,0.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawcircle():
	global m
	global s
	global x
	global y
	glClear(GL_COLOR_BUFFER_BIT)

	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1.0,1.0,1.0)
	glVertex2f(x,y)
	for i in range(0,361,1):
		glVertex2f(300*math.cos(math.pi*i/180.0)+x,300*math.sin(math.pi*i/180.0)+y)
	glEnd()
	glLineWidth(3.0)
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(x,y)
	glVertex2f(200*math.cos(math.pi*s/180.0)+x,200*math.sin(math.pi*s/180.0)+y)
	glEnd()
	
	glLineWidth(7.0)
	glBegin(GL_LINES)
	glColor3f(1.0,1.0,0.0)
	glVertex2f(x,y)
	glVertex2f(150*math.cos(math.pi*m/180.0)+x,150*math.sin(math.pi*m/180.0)+y)
	glEnd()
	glutSwapBuffers()

def animate(temp):
	global m,s
	m=m-1
	s=s-6
	glutTimerFunc(int(1000/50),animate,0)
	glutPostRedisplay()
	
	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("CLock")
	glutDisplayFunc(drawcircle)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawcircle)
	init()
	glutMainLoop()
main()
