from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import random 
import playsound
from tkinter import *

 

class Fantasma3:
    posicionX = -0.5
    posicionY = 0.5
    colisionando = False
    rotacion=0
    #monito = Monito()

    def dibujar(self):
        

        glPushMatrix()
        glTranslate(self.posicionX,self.posicionY, 0.0)
        glRotate(self.rotacion, 0.0, 0.0, 1.0)
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.5, 0.0)
        #glVertex3f(0.03,0.0,0.0)
        #glVertex3f(0.015,-0.05,0.0)
        #glVertex3f(0.06,0.0,0.0)
        glVertex3f(-0.075,-0.08,0.0)
        glVertex3f(0.07,-0.08,0.0)
        for a in range (360):
            angulo= (a*3.14159/180)
            glVertex3f(cos(angulo)/16,sin(angulo)/16,0.0) 
        

        
        glEnd()
        glPopMatrix()


        
        glPushMatrix()
        glTranslate(self.posicionX,self.posicionY, 0.0)
        #glRotate(self.rotacion, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
    


        glVertex3f(-0.072,-0.08,0.0)
        glVertex3f(-0.042,-0.08,0.0)
        glVertex3f(-0.057,-0.12,0.0)

        glVertex3f(-0.045,-0.08,0.0)
        glVertex3f(-0.015,-0.08,0.0)
        glVertex3f(-0.03,-0.12,0.0)

        glVertex3f(-0.015,-0.08,0.0)
        glVertex3f(0.015,-0.08,0.0)
        glVertex3f(0.0,-0.12,0.0)

        glVertex3f(0.015,-0.08,0.0)
        glVertex3f(0.045,-0.08,0.0)
        glVertex3f(0.0225,-0.12,0.0)

        glVertex3f(0.045,-0.08,0.0)
        glVertex3f(0.072,-0.08,0.0)
        glVertex3f(0.05,-0.12,0.0)
        
        glEnd()
        glPopMatrix()
    
        glPushMatrix()
        glTranslate(self.posicionX,self.posicionY, 0.0)
        glRotate(self.rotacion, 0.0, 0.0, 1.0)
        glBegin(GL_POLYGON)
        glColor3f(1.0,1.0,1.0)
        for a in range (360):
            angulo= (a*3.14159/180)
            glVertex3f(cos(angulo)/60 -0.03,sin(angulo)/60,0.0) 
        
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(self.posicionX,self.posicionY, 0.0)
        glRotate(self.rotacion, 0.0, 0.0, 1.0)
        glBegin(GL_POLYGON)
        glColor3f(1.0,1.0,1.0)
        for a in range (360):
            angulo= (a*3.14159/180)
            glVertex3f(cos(angulo)/60 + 0.03,sin(angulo)/60,0.0) 
    
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(self.posicionX,self.posicionY, 0.0)
        glRotate(self.rotacion, 0.0, 0.0, 1.0)
        glBegin(GL_POLYGON)
        glColor3f(0.0,0.0,0.0)
        for a in range (360):
            angulo= (a*3.14159/180)
            glVertex3f(cos(angulo)/110 + 0.04,sin(angulo)/110,0.0) 
        
        glEnd()
        glPopMatrix()

        glPushMatrix()
        glTranslate(self.posicionX,self.posicionY, 0.0)
        glRotate(self.rotacion, 0.0, 0.0, 1.0)
        glBegin(GL_POLYGON)
        glColor3f(0.0,0.0,0.0)
        for a in range (360):
            angulo= (a*3.14159/180)
            glVertex3f(cos(angulo)/110 -0.02,sin(angulo)/110,0.0) 
        
        glEnd()
        glPopMatrix()   

    

    
    def actualizar(self, window):
    
        yFantasmaR = sin(60)
        self.posicionY = self.posicionY -0.005 * yFantasmaR
        xFantasmaR = (cos(90))
        self.posicionX = self.posicionX +0.01 * xFantasmaR

    