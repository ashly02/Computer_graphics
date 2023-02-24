from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
WINDOW_SIZE=500
FPS=10
gx1=50
gx2=160
mode=0
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawgun():
	global gx1,gx2
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	glColor3f(1.0,0.0,1.0)
	glVertex2f(50,70)
	glVertex2f(50,0)
	glVertex2f(0,0)
	glVertex2f(0,150)
	glVertex2f(180,150)
	glVertex2f(180,70)
	glEnd()	
	
	
	glBegin(GL_QUADS)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(gx1,25)
	glVertex2f(gx1,70)
	glVertex2f(gx1+25,70)
	glVertex2f(gx1+25,25)
	glEnd()
	glBegin(GL_POLYGON)
	glColor3f(0.0,0.0,1.0)
	glVertex2f(gx2,90)
	glVertex2f(gx2,120)
	glVertex2f(gx2+20,120)
	glVertex2f(gx2+30,105)
	glVertex2f(gx2+20,90)
	glEnd()
	
	glutSwapBuffers()
def animate(temp):
	global gx1,gx2,mode
	if mode==0:
		if gx1<=30:
			gx1=50
			mode=1
		else:
			gx1-=3
	if mode==1:
		if gx2>=500:
			gx2=180
			mode=0
		else:
			gx2+=20
	
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()
def main():
	glutInit(sys.argv)
	glutInitWindowSize(0,0)
	glutInitWindowPosition(WINDOW_SIZE,WINDOW_SIZE)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("GUN")
	glutDisplayFunc(drawgun)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(drawgun)
	init()
	glutMainLoop()
main()
