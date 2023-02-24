from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math

ws=500
fps=60
mode=1
gy=0
gx=0
a1=180.0
a2=0.0
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-ws,ws,-ws,ws)
def draw():
	global gx,gy,a2,a1
	glClear(GL_COLOR_BUFFER_BIT)
	x1=200*math.cos(math.pi*120/180)+gx
	y1=200*math.sin(math.pi*120/180)+gy
	x2=200*math.cos(math.pi*60/180)+gx
	y2=200*math.sin(math.pi*60/180)+gy
	glBegin(GL_TRIANGLES)
	glColor3f(1.0,1.0,0.0)
	glVertex2f(gx,gy)
	glVertex2f(x1,y1)
	glVertex2f(x2,y2)
	glEnd()
	glLineWidth(5.0)
	glBegin(GL_LINES)
	glVertex2f(x2,y2)
	glVertex2f(120*math.cos(math.pi*a2/180)+x2,120*math.sin(math.pi*a2/180)+y2)
	glEnd()
	glLineWidth(5.0)
	glBegin(GL_LINES)
	glVertex2f(x1,y1)
	glVertex2f(120*math.cos(math.pi*a1/180)+x1,120*math.sin(math.pi*a1/180)+y1)
	glEnd()
	glutSwapBuffers()
def animate(temp):
	global a2,a1,mode,gy
	if mode==1:
		if (a2>=30 and a1<=150):
			mode=0
		else:
			a2=a2+2
			a1=a1-2
	elif mode==0:
		if(a2<=330 and a1>=210):
			mode=1
		else:
			a2=a2-2
			a1=a1+2
	gy=gy+1
	glutTimerFunc(int(1000/fps),animate,0)
	glutPostRedisplay()
	
	


def main():
	glutInit(sys.argv)
	glutInitWindowSize(ws,ws)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("bird")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	init()
	glutMainLoop()
main()
