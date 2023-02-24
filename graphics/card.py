from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys 
import math

WINDOW_SIZE=500
GLOBAL_X=0.0
GLOBAL_Y=0.0
GLOBAL_ANGLE=45

def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-WINDOW_SIZE,WINDOW_SIZE,-WINDOW_SIZE,WINDOW_SIZE)

def drawrect(x,y):
	glBegin(GL_POLYGON)
	glVertex2f(x-100,y+50)
	glVertex2f(x+100,y+50)
	glVertex2f(x+100,y-100)
	glVertex2f(x-150,y-100)
	glVertex2f(x-150,y-0)
	
	glEnd()

def drawcircle(x,y,s):
	i=0.0
	
	if s==0:
		y=y-100-35
		x=x-50
	else:
		y=y-100-35
		x=x+50
	glColor3f(0.0,0.0,0.0)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x,y)
	for i in range(0,361,1):
		glVertex2f(35*math.cos(math.pi*i/180.0)+x,35*math.sin(math.pi*i/180.0)+y)
	glEnd()

	x1=35*math.cos(math.pi*GLOBAL_ANGLE/180.0)+x
	y1=35*math.sin(math.pi*GLOBAL_ANGLE/180.0)+y
	glColor3f(1.0,1.0,1.0)
	glBegin(GL_LINES)
	glVertex2f(x,y)
	glVertex2f(x1,y1)
	glEnd()


def drawcar():
	global GLOBAL_X
	global GLOBAL_Y
	
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1.0,0.0,0.0)
	drawrect(GLOBAL_X,GLOBAL_Y)
	drawcircle(GLOBAL_X,GLOBAL_Y,0)
	drawcircle(GLOBAL_X,GLOBAL_Y,1)
	glutSwapBuffers()

def animate(value,key):
	global GLOBAL_X
	global GLOBAL_Y
	global GLOBAL_ANGLE
	if key=='a':
		if(GLOBAL_X-150>-WINDOW_SIZE):
			GLOBAL_X=GLOBAL_X-10
			if GLOBAL_ANGLE==360:
				GLOBAL_ANGLE=0
			else:
				GLOBAL_ANGLE=GLOBAL_ANGLE+10
		else:
			GLOBAL_X=400
	elif key=='d':
		if(GLOBAL_X+100<WINDOW_SIZE):
			GLOBAL_X=GLOBAL_X+value
			if GLOBAL_ANGLE==0:
				GLOBAL_ANGLE=360			
			else:
				GLOBAL_ANGLE=GLOBAL_ANGLE-10
		else:
			GLOBAL_X=-350
	glutPostRedisplay()	


def keyboard(key,x,y):
	key=key.decode()
	if key=='a':
		animate(-3,'a')
	elif key=='d':
		animate(3,'d')
	elif key=='z':
		glutLeaveMainLoop()
	elif key=='f':
		glutFullScreen()
			

def main():
	glutInit(sys.argv)
	glutInitWindowSize(WINDOW_SIZE,WINDOW_SIZE)
	glutInitWindowPosition(0,0)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("CAr moving")
	glutDisplayFunc(drawcar)
	glutKeyboardFunc(keyboard)
	init()
	glutMainLoop()
main()
	
