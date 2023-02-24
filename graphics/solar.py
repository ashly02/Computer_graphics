from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
import math
WINDOW_SIZE=800
FPS=10
angle=0
gx=0.0
gy=0.0
ga1=0
ga2=0
ga3=0

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)
def drawcirc(r,theta,r1,a,b,c):
	x=r*math.cos(math.pi*theta/180)
	y=r*math.sin(math.pi*theta/180)
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(a,b,c)
	glVertex2f(x,y)
	for i in range(0,361,1):
		glVertex2f(r1*math.cos(math.pi*i/180.0)+x,r1*math.sin(math.pi*i/180)+y)
	glEnd()

def draw():
	global angle,gx,gy,ga1,ga2,ga3
	glClear(GL_COLOR_BUFFER_BIT)
	glBegin(GL_TRIANGLE_FAN)
	glColor3f(1.0,1.0,0.0)
	glVertex2f(gx,gy)
	for i in range(0,361,1):
		glVertex2f(50*math.cos(math.pi*i/180.0)+gx,50*math.sin(math.pi*i/180)+gy)
	glEnd()
	drawcirc(100,ga1+60,25,1.0,0.0,0.0)
	drawcirc(200,ga2+270,35,2.0,0.0,2.0)
	drawcirc(300,ga3+180,25,0.0,1.0,0.0)
	glutSwapBuffers()
	
def animate(temp):
	global gx,gy,ga1,ga2,ga3
	ga1+=1
	ga2+=5
	ga3+=8
	glutTimerFunc(int(1000/FPS),animate,0)
	glutPostRedisplay()
	
def main():
	glutInit(sys.argv)
	glutInitWindowSize(0,0)
	glutInitWindowPosition(WINDOW_SIZE,WINDOW_SIZE)
	glutInitDisplayMode(GLUT_RGBA)
	glutCreateWindow("SOLAR")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glutIdleFunc(draw)
	init()
	glutMainLoop()
main()
