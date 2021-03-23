from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import random 
import playsound
from tkinter import *


class Letras:

    def dibujar(self):
        glPushMatrix()
        glBegin(GL_LINES)
        glColor3f(0.8, 0.5, 0.3)
        glVertex(-0.15, 0.15, 0.0)
        glVertex(-0.15, -0.15, 0.0)
        glVertex(0.05, 0.15, 0.0)
        glVertex(0.05, -0.0, 0.0)

        glVertex(-0.15, -0.0, 0.0)
        glVertex(0.05, -0.0, 0.0)

        glVertex(-0.15, 0.15, 0.0)
        glVertex(0.05, 0.15, 0.0)

        glVertex(0.05, 0.15, 0.0)
        glVertex(0.05, 0.0, 0.0)
        glEnd()
        glPopMatrix()


        glPushMatrix()
        glBegin(GL_LINE_STRIP)
        glColor3f(0.8, 0.5, 0.3)
        glVertex(-0.15, 0.15, 0.0)
        glVertex(-0.15, -0.15, 0.0)
        glVertex(0.05, 0.15, 0.0)
        glVertex(0.05, -0.0, 0.0)

        glVertex(0.05, -0.15, 0.0)
        glVertex(0.05, 0.15, 0.0)

        glVertex(0.05, -0.15, 0.0)
        glVertex(0.09, 0.15, 0.0)

        glVertex(0.09, 0.15, 0.0)
        glVertex(0.22, -0.15, 0.0)
            #glVertex(0.05, 0.15, 0.0)
    

        glEnd()
        glPopMatrix()

        glPushMatrix()
        #glTranslate(-1,-0.9,0.0)
        glBegin(GL_LINES)
        glColor3f(0.8, 0.5, 0.3)
        glVertex(-0.99, -0.97, 0.0)
        glVertex(0.99, -0.97, 0.0)
        #glVertex(0.9, -0.8, 0.0)
        #glVertex(0.05, -0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        #glTranslate(-1,-0.9,0.0)
        glBegin(GL_LINES)
        glColor3f(0.8, 0.5, 0.3)
        glVertex(-0.99, 0.96, 0.0)
        glVertex(0.99, 0.96, 0.0)
        #glVertex(0.9, -0.8, 0.0)
        #glVertex(0.05, -0.0, 0.0)
        glEnd()
        glPopMatrix()

        
        glPushMatrix()
        #glTranslate(-1,-0.9,0.0)
        glBegin(GL_LINES)
        glColor3f(0.8, 0.5, 0.3)
        glVertex(-0.99, -0.96, 0.0)
        glVertex(-0.99, 0.96, 0.0)
        #glVertex(0.9, -0.8, 0.0)
        #glVertex(0.05, -0.0, 0.0)
        glEnd()
        glPopMatrix()

        glPushMatrix()
        #glTranslate(-1,-0.9,0.0)
        glBegin(GL_LINES)
        glColor3f(0.8, 0.5, 0.3)
        glVertex(0.99, -0.96, 0.0)
        glVertex(0.99, 0.96, 0.0)
        #glVertex(0.9, -0.8, 0.0)
        #glVertex(0.05, -0.0, 0.0)
        glEnd()
        glPopMatrix()
