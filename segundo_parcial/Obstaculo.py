from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import random 
import playsound
from tkinter import *

class Obstaculo:
    posicionX = 0.0
    posicionY = 0.0

    
    def __init__(self, x, y):
        self.posicionX = x
        self.posicionY = y

    def dibujar(self):
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY,0.0)
            
        glBegin(GL_QUADS)
            
        glColor3f(1.0,1.0,1.0)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()