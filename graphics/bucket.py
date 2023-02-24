from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE=500
gy=0
FPS=20

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawbucket():
	x=0.0
	y=0.0
	global gy
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(x,y)
	glVertex2f(x,y+200)
	glEnd()
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(x-1,y)
	glVertex2f(x+200,y)
	glEnd()
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(x+200,y-1)
	glVertex2f(x+200,y+200)
	glEnd()
	
	glBegin(GL_QUADS)
	glColor3f(0.0,0.0,1.0)
	glVertex2f(x+1,y)
	glVertex2f(x+1,gy+1)
	glVertex2f(x+199,gy+1)
	glVertex2f(x+199,y)
	glEnd()
	glutSwapBuffers()
	
def animate(temp):
	global gy
	if gy<=188:
		gy=gy+2
	else:
		gy=0
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()
		
	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Bucket")
	glutDisplayFunc(drawbucket)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawbucket)
	init()
	glutMainLoop()
main()

