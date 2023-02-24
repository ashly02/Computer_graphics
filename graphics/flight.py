from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

ws=800
fps=60
gx=-550
gy=0
angle=0.0
x2=800
y2=660
x1=-100
y1=0
dx=x2-x1
dy=y2-y1
m=dy/dx

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-ws,ws,-ws,ws)
def draw():
	global gx,gy
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_POLYGON)
	glColor3f(0.0,0.0,1.0)
	glVertex2f(gx-150,gy+50)
	glVertex2f(gx+80,gy+50)
	glVertex2f(gx+150,gy-60)
	glVertex2f(gx-200,gy-60)
	glVertex2f(gx-200,gy+150)
	glEnd()
	glutSwapBuffers()
def animate(temp):
	global gx,gy
	if gx<=-400:
		gx=gx+2
	elif -400<gx<=-300:
		gx=gx+3
	elif -300<gx<-100:
		gx=gx+6
	if gx>=-100:

		gx=gx+1
		gy=gy+m
	glutTimerFunc(int(1000/fps),animate,0)
	glutPostRedisplay()
	

def main():
	glutInit(sys.argv)
	glutInitWindowSize(ws,ws)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("FLIGHT")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	init()
	glutMainLoop()
main()
