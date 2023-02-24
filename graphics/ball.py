from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE=500
gx=0.0
gy=0.0
mode=1
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
	
def drawball():
	glClear(GL_COLOR_BUFFER_BIT)
	global gx
	global gy
	x=0
	y=0
	glColor3f(1.0,0.0,0.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(gx,gy)
	for i in range(0,361,1):
		glVertex2f(100*math.cos(math.pi*i/180.0)+gx,100*math.sin(math.pi*i/180.0)+gy)
	glEnd()
	glutSwapBuffers()
	
	
def animate(temp):
	global gx,gy,mode
	if mode==1:
		gy=gy-1
		if gy==-50:
			mode=0
	elif mode==0:
		gy=gy+1
		if gy==50:
			mode=1
	glutTimerFunc(int(1000/50),animate,0)
	glutPostRedisplay()		
	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("BAll")
	glutDisplayFunc(drawball)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawball)
	init()
	glutMainLoop()
main()
