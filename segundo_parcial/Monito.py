from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import random 
import playsound
from tkinter import *
from Fantasmas import *
from Fantasma6 import *
from Fantasma5 import *
from Fantasma4 import *
from Fantasma3 import *
from Fantasma2 import *
from Bolita import *
#from Obstaculo import *

fantasma6 = Fantasma6()
fantasma5 = Fantasma5()
fantasma4 = Fantasma4()
fantasma3 = Fantasma3()
fantasma2 = Fantasma2()
fantasma = Fantasmas()
#bolita = Bolita()
#obstaculo = Obstaculo()

class Monito:
    posicionX = 0.0
    posicionY = -0.8
    colisionando = False
    rotacion= 0.0
    direccion= 0.0
    desfase = 590000
    angulo = 0 
    
    #angulo =0.0

    def boca(self):
        
        glPopMatrix()
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glRotate(self.rotacion + 90 ,0.0,0.0,1.0)
        glScale(0.5,0.5,0.5)
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(0.1,0.0,0.0)
        for a in range (360):
            self.angulo= (a*3.14159/180)/4
            glVertex3f(cos(self.angulo)/8,sin(self.angulo)/8,0.0)
            glVertex3f(0.0,0.1,0.0)
            glVertex3f(-0.01,0.0,0.0)
        glEnd()
        glPopMatrix()
    
    def dibujar(self):
       
        glPushMatrix()
        glTranslate(self.posicionX, self.posicionY, 0.0)
        glScale(0.5,0.5,0.5)
        glRotate(self.rotacion + 90 ,0.0,0.0,1.0)
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        #glBegin(GL_TRIANGLES)
        if self.colisionando == True:
            glColor3f(1.0, 1.0, 1.0)
            
        else:
            glColor3f(0.8,0.8,0.1)
    
        
        

        for a in range (360):
            angulo= a*3.14159/180
            glVertex3f(cos(angulo)/8,sin(angulo)/8,0.0)
        glEnd()
        self.boca()
       

    
    def actualizar(self,window):

        estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
        estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
        estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
        estadoArriba = glfw.get_key(window, glfw.KEY_UP)
    
        if estadoIzquierda == glfw.PRESS and self.colisionando == False:
            self.posicionX = self.posicionX - 0.2
            self.direccion = 2
            self.rotacion = 0 - self.desfase
            playsound.playsound('pacman-waka-waka.mp3', True) 
            #playsound.playsound('pacman-waka-waka.mp3', False)
            #playsound.playsound('pacman-waka-waka.mp3', True)
            #playsound.playsound('pacman-waka-waka.mp3', True) 
        if estadoDerecha == glfw.PRESS and self.colisionando == False:
            self.posicionX = self.posicionX + 0.2
            self.direccion = 1
            self.rotacion = 180 - self.desfase
            playsound.playsound('pacman-waka-waka.mp3', True) 
            #playsound.playsound('pacman-waka-waka.mp3', True) 
            #playsound.playsound('pacman-waka-waka.mp3', True)
        if estadoAbajo == glfw.PRESS and self.colisionando == False:
            self.posicionY = self.posicionY - 0.2
            self.direccion = 3
            self.rotacion = 90 - self.desfase
            playsound.playsound('pacman-waka-waka.mp3', True) 
            #playsound.playsound('pacman-waka-waka.mp3', True) 
            #playsound.playsound('pacman-waka-waka.mp3', True)
        if estadoArriba == glfw.PRESS and self.colisionando == False:
            self.posicionY = self.posicionY + 0.2
            self.direccion = 0
            self.rotacion = 270 - self.desfase
            playsound.playsound('pacman-waka-waka.mp3', True) 
            #playsound.playsound('pacman-waka-waka.mp3', True) 
            #playsound.playsound('pacman-waka-waka.mp3', True)
            #playsound.playsound('pacman-waka-waka.mp3', True)
    

    def checar_colisiones_obstaculos(self, obstaculo):
        if self.posicionX + 0.05 > obstaculo.posicionX - 0.15 and self.posicionX - 0.05 < obstaculo.posicionX + 0.15 and self.posicionY + 0.05 > obstaculo.posicionY - 0.15 and self.posicionY - 0.05 < obstaculo.posicionY + 0.15:
            self.colisionando = True
            playsound.playsound('pacman-dies.mp3', True)        
            exit()
        else:
            self.colisionando = False

    def checar_colisiones_bolitas(self,bolita):
        if self.posicionX + 0.05> bolita.posicionX - 0.05 and self.posicionX - 0.05 < bolita.posicionX + 0.05 and self.posicionY + 0.05 > bolita.posicionY - 0.05 and self.posicionY - 0.05 < bolita.posicionY + 0.05:
           bolita.vivo=False

        
        
       
        
       

    def checar_colisiones(self, fantasma):
        #global fantasma
        global fantasma6
        global fantasma5
        global fantasma4

        if self.posicionX + 0.05> fantasma.posicionX - 0.09 and self.posicionX - 0.05 < fantasma.posicionX + 0.09 and self.posicionY + 0.05 > fantasma.posicionY - 0.09 and self.posicionY - 0.05 < fantasma.posicionY + 0.09:
            #playsound.playsound('pacman-dies.mp3', True)        
            self.colisionando = True
            playsound.playsound('pacman-dies.mp3', True)        
            exit()

    def checar_colisiones6(self, fantasma6):
        #global fantasma
        #global fantasma6
        global fantasma5
        global fantasma4

        if self.posicionX + 0.05> fantasma6.posicionX - 0.09 and self.posicionX - 0.05 < fantasma6.posicionX + 0.09 and self.posicionY + 0.05 > fantasma6.posicionY - 0.09 and self.posicionY - 0.05 < fantasma6.posicionY + 0.09:
            #playsound.playsound('pacman-dies.mp3', True)        
            self.colisionando = True
            playsound.playsound('pacman-dies.mp3', True)        
            exit()
    def checar_colisiones4(self, fantasma4):
        #global fantasma
        #global fantasma6
        global fantasma5
       

        if self.posicionX + 0.05> fantasma4.posicionX - 0.09 and self.posicionX - 0.05 < fantasma4.posicionX + 0.09 and self.posicionY + 0.05 > fantasma4.posicionY - 0.09 and self.posicionY - 0.05 < fantasma4.posicionY + 0.09:
            #playsound.playsound('pacman-dies.mp3', True)        
            self.colisionando = True
            playsound.playsound('pacman-dies.mp3', True)        
            exit()
    
    def checar_colisiones5(self, fantasma5):
        #global fantasma
        #global fantasma6
       
       

        if self.posicionX + 0.05> fantasma5.posicionX - 0.09 and self.posicionX - 0.05 < fantasma5.posicionX + 0.09 and self.posicionY + 0.05 > fantasma5.posicionY - 0.09 and self.posicionY - 0.05 < fantasma5.posicionY + 0.09:
            #playsound.playsound('pacman-dies.mp3', True)        
            self.colisionando = True
            playsound.playsound('pacman-dies.mp3', True)        
            exit()
    
    def checar_colisiones3(self, fantasma3):
             

        if self.posicionX + 0.05> fantasma3.posicionX - 0.09 and self.posicionX - 0.05 < fantasma3.posicionX + 0.09 and self.posicionY + 0.05 > fantasma3.posicionY - 0.09 and self.posicionY - 0.05 < fantasma3.posicionY + 0.09:
            #playsound.playsound('pacman-dies.mp3', True)        
            self.colisionando = True
            playsound.playsound('pacman-dies.mp3', True)        
            exit()

    def checar_colisiones2(self, fantasma2):
             

        if self.posicionX + 0.05> fantasma2.posicionX - 0.09 and self.posicionX - 0.05 < fantasma2.posicionX + 0.09 and self.posicionY + 0.05 > fantasma2.posicionY - 0.09 and self.posicionY - 0.05 < fantasma2.posicionY + 0.09:
            #playsound.playsound('pacman-dies.mp3', True)        
            self.colisionando = True
            playsound.playsound('pacman-dies.mp3', True)        
            exit()
        else:
            self.colisionando=False

    
        
  
        
        
        

    