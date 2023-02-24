from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

WINDOW_SIZE=500
FPS=150
rad=0.0
angle=0.0
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawleaf(r1,r2,a1,a2):
	x1=r1*math.cos(math.pi*a1/180.0)
	y1=r1*math.sin(math.pi*a1/180.0)
	x2=r2*math.cos(math.pi*a2/180.0)
	y2=r2*math.sin(math.pi*a2/180.0)
	x3=r1*math.cos(math.pi*a2/180.0)
	y3=r1*math.sin(math.pi*a2/180.0)
	x4=r2*math.cos(math.pi*a1/180.0)
	y4=r2*math.sin(math.pi*a1/180.0)
	glBegin(GL_QUADS)
	glVertex2f(x1,y1)
	glVertex2f(x4,y4)
	glVertex2f(x2,y2)
	glVertex2f(x3,y3)
	glEnd()
	
def draw():
	global rad
	glClear(GL_COLOR_BUFFER_BIT)
	glLineWidth(10.0)
	glBegin(GL_LINES)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(0,0)
	glVertex2f(0,-500)
	glEnd()
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1.0,0.0,0.0)
	glVertex2f(0,0)
	for i in range(0,361,1):
		glVertex2f(100*math.cos(math.pi*i/180.0),100*math.sin(math.pi*i/180.0))
	glEnd()
	drawleaf(100,350,angle+70,angle+110)
	drawleaf(100,350,angle+205,angle+245)
	drawleaf(100,350,angle+295,angle+335)
	glutSwapBuffers()
def animate(temp):
	global angle
	angle+=1
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()
	

def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("fan")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	init()
	glutMainLoop()
main()

