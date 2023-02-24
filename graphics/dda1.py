from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

scale=50
x1=y1=0
x2=y2=10

def dda():
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1,0,0)
	glPointSize(5)
	dx,dy=x2-x1,y2-y1
	if abs(dx)>abs(dy):
		steps=abs(dx)
	else:
		steps=abs(dy)
	xinc,yinc=dx/steps,dy/steps
	glBegin(GL_POINTS)
	x,y=x1,y1
	glVertex2f(x/scale,y/scale)
	for i in range(int(steps)):
		x+=xinc
		y+=yinc
		glVertex2f(x/scale,y/scale)
	glEnd()
	glFlush()

def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB)
	glutInitWindowSize(500,500)
	glutInitWindowPosition(0,0)
	global x1,y1,x2,y2
	x1=int(input("Enter first x coordinate:"))
	y1=int(input("Enter first y coordinate:"))
	x2=int(input("Enter second x coordinate:"))
	y2=int(input("Enter second y coordinate:"))
	glutCreateWindow("dda")
	glutDisplayFunc(dda)
	glutMainLoop()
main()
	
		
	
