from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE=500
FPS=50
mode=1
angle=0
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawpend():
	global x,y,angle
	x=0
	y=0
	glClear(GL_COLOR_BUFFER_BIT)
	x1=300*math.cos(math.pi*angle/180.0)
	y1=300*math.sin(math.pi*angle/180.0)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glColor3f(0.0,0.0,0.0)
	glVertex2f(x,y)
	glVertex2f(x1,y1)
	glEnd()
	
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(0.0,0.0,0.0)
	glVertex(x1,y1)
	for i in range(0,361,1):
		glVertex(50*math.cos(math.pi*i/180.0)+x1,50*math.sin(math.pi*i/180.0)+y1)
	glEnd()
	glutSwapBuffers()
def animate(temp):
	global angle,mode
	if 0<=angle<90:
		angle+=1
	elif 90<=angle<180:
		angle+=2
	elif angle<360:
		angle+=3
	elif angle==360:
		angle=0		
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()
		
	

def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Pendulum")
	glutDisplayFunc(drawpend)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawpend)
	init()
	glutMainLoop()
main()
	
