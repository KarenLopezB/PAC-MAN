from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import random 
import playsound
from tkinter import *
from Fantasma6 import *
from Fantasma5 import *
from Fantasma4 import *

fantasma6 = Fantasma6()
fantasma5 = Fantasma5()
fantasma4 = Fantasma4()

class Fantasmas:
  colisinando=False
  posicionX = 0.5
  posicionY=0.5
  rotacion = 0
  
  def dibujar(self):
    
    
    glPushMatrix()
    glTranslate(self.posicionX,self.posicionY, 0.0)
    glRotate(self.rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
  
    glVertex3f(-0.075,-0.08,0.0)
    glVertex3f(0.07,-0.08,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/16,sin(angulo)/16,0.0) 
    

    
    glEnd()
    glPopMatrix()


    
    glPushMatrix()
    glTranslate(self.posicionX,self.posicionY, 0.0)
    #glRotate(rotacion, 0.0, 0.0, 1.0)
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
    global fantasma5
    global fantasma6
    global fantasma4

    yFantasmaR = sin(30)*random.random()
    self.posicionY = self.posicionY -0.005 * yFantasmaR
    xFantasmaR = cos(30)*random.random()
    self.posicionX = self.posicionX * cos(xFantasmaR)

    


    

    
    






    