from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import random 

from tkinter import *

xObstaculo = -0.65
yObstaculo = 0.6
obstaculoVivo=True
obstaculoVivo1=True

xObstaculo2 = -0.15
yObstaculo2 = 0.6

xObstaculo3 = 0.45
yObstaculo3 = 0.6

xObstaculo4 = 0.95
yObstaculo4 = 0.6

xObstaculo5 = -1
yObstaculo5 = 0.0

xObstaculo6 = -0.45
yObstaculo6 = 0.0

xObstaculo7 =0.4
yObstaculo7 = 0.0

xObstaculo8 = 0.7
yObstaculo8 = 0.0

xObstaculo9 = -0.45
yObstaculo9 = -0.5

xObstaculo10 =0.4
yObstaculo10 = 0.0

xObstaculo11 = 0.7
yObstaculo11 = 0.0

xCarrito = 0.0
yCarrito = -0.8
rotacion=0
direccion = 0

colisionando = False


desfase = 5900


xbolitas=-0.88
ybolitas=0.88

xbolitas2=-0.48
ybolitas2=0.88

xbolitas3=-0.28
ybolitas3=0.88

xBala = 0
yBala = 0
anguloBala=0

def checar_colisiones():
    global colisionando
    global bolitas1
    global obstaculoVivo
    global obstaculoVivo1
    #si extremaDerechaCarrito > extremaIquierdaCarrito
    if xCarrito + 0.05> xObstaculo2 - 0.15 and xCarrito - 0.05 < xObstaculo2 + 0.15 and yCarrito + 0.05 > yObstaculo2 - 0.15 and yCarrito - 0.05 < yObstaculo2 + 0.15:
        colisionando = True
        #obstaculoVivo=False
    elif xCarrito + 0.05> xObstaculo - 0.15 and xCarrito - 0.05 < xObstaculo + 0.15 and yCarrito + 0.05 > yObstaculo - 0.15 and yCarrito - 0.05 < yObstaculo + 0.15:
        colisionando = True
        #obstaculoVivo=False
    elif xCarrito + 0.05> xObstaculo3 - 0.15 and xCarrito - 0.05 < xObstaculo3 + 0.15 and yCarrito + 0.05 > yObstaculo3 - 0.15 and yCarrito - 0.05 < yObstaculo3 + 0.15:
        colisionando = True
    elif xCarrito + 0.05> xObstaculo4 - 0.15 and xCarrito - 0.05 < xObstaculo4 + 0.15 and yCarrito + 0.05 > yObstaculo4 - 0.15 and yCarrito - 0.05 < yObstaculo4 + 0.15:
        colisionando = True
    elif xCarrito + 0.05> xObstaculo5 - 0.15 and xCarrito - 0.05 < xObstaculo5 + 0.15 and yCarrito + 0.05 > yObstaculo5 - 0.15 and yCarrito - 0.05 < yObstaculo5 + 0.15:
        colisionando = True
    elif xCarrito + 0.05> xObstaculo6 - 0.15 and xCarrito - 0.05 < xObstaculo6 + 0.15 and yCarrito + 0.05 > yObstaculo6 - 0.15 and yCarrito - 0.05 < yObstaculo6 + 0.15:
        colisionando = True
    elif xCarrito + 0.05> xObstaculo7 - 0.15 and xCarrito - 0.05 < xObstaculo7 + 0.15 and yCarrito + 0.05 > yObstaculo7 - 0.15 and yCarrito - 0.05 < yObstaculo7 + 0.15:
        colisionando = True
    elif xCarrito + 0.05> xObstaculo8 - 0.15 and xCarrito - 0.05 < xObstaculo8 + 0.15 and yCarrito + 0.05 > yObstaculo8 - 0.15 and yCarrito - 0.05 < yObstaculo8 + 0.15:
        colisionando = True
    
        
    elif xCarrito + 0.05> xbolitas - 0.05 and xCarrito - 0.05 < xbolitas + 0.05 and yCarrito + 0.05 > ybolitas - 0.05 and yCarrito - 0.05 < ybolitas + 0.05:
        obstaculoVivo=False

    elif xCarrito + 0.05> xbolitas2 - 0.05 and xCarrito - 0.05 < xbolitas2 + 0.05 and yCarrito + 0.05 > ybolitas2 - 0.05 and yCarrito - 0.05 < ybolitas2 + 0.05:
        obstaculoVivo1=False
    else:
        colisionando = False
        #obstaculoVivo=True



def actualizar(window):
    global xCarrito
    global yCarrito
    global colisionando
    global direccion
    global desfase
    global rotacion
    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)

    if estadoIzquierda == glfw.PRESS and colisionando == False:
        xCarrito = xCarrito - 0.003
        direccion = 2
        rotacion = 180 - desfase
    if estadoDerecha == glfw.PRESS and colisionando == False:
        xCarrito = xCarrito + 0.003
        direccion = 1
        rotacion = 0 - desfase
    if estadoAbajo == glfw.PRESS and colisionando == False:
        yCarrito = yCarrito - 0.003
        direccion = 3
        rotacion = 270 - desfase
    if estadoArriba == glfw.PRESS and colisionando == False:
        yCarrito = yCarrito + 0.003 
        direccion = 0
        rotacion = 90 - desfase

    
  
       
  
        
    
    

    
    checar_colisiones()
    #checar_bolitas()


def dibujarObstaculo():
    global xObstaculo
    global yObstaculo
    global xObstaculo2
    global yObstaculo2
    global xObstaculo9
    global yObstaculo9

    
    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo,0.0)
  
    glBegin(GL_QUADS)
        
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo2, yObstaculo2,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo3, yObstaculo3,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo4, yObstaculo4,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo5, yObstaculo5,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo6, yObstaculo6,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo7, yObstaculo7,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()

    glPopMatrix()
    glPushMatrix()
    glTranslate(xObstaculo8, yObstaculo8,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0,0.5,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    


   

def bolitas1():
    global xbolitas
    global ybolitas
    global obstaculoVivo
    if obstaculoVivo:
        glPushMatrix()
        glTranslate(xbolitas, ybolitas,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()
    

def bolitas2():
    global xbolitas2
    global ybolitas2
    global obstaculoVivo1
    if obstaculoVivo1:
        glPushMatrix()
        glTranslate(xbolitas2, ybolitas2,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas3():
    global xbolitas3
    global ybolitas3
    global obstaculoVivo
    if obstaculoVivo:
        glPushMatrix()
        glTranslate(xbolitas3, ybolitas3,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def boca():
 
    global colisionando
    global xCarrito
    global yCarrito

    
    glPushMatrix()
    glTranslate(xCarrito, yCarrito, 0.0)
    glRotate(rotacion + 90 ,0.0,0.0,1.0)
    glScale(0.5,0.5,0.5)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(0.1,0.0,0.0)
    for a in range (360):
       angulo= (a*3.14159/180)/4
       glVertex3f(cos(angulo)/8,sin(angulo)/8,0.0)
    glVertex3f(0.0,0.1,0.0)
    glVertex3f(-0.01,0.0,0.0)
    glEnd()
    glPopMatrix()

def dibujarCarrito():
    global xCarrito
    global yCarrito
    global colisionando
    global rotacion

    glPushMatrix()
    glTranslate(xCarrito, yCarrito, 0.0)
    glScale(0.5,0.5,0.5)
    glRotate(rotacion + 90 ,0.0,0.0,1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 0.0)
    #glBegin(GL_TRIANGLES)
    if colisionando == True:
        glColor3f(1.0, 1.0, 1.0)
        
    else:
        glColor3f(0.8,0.8,0.1)
   
    
    

    for a in range (360):
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/8,sin(angulo)/8,0.0)
    glEnd()
    glPopMatrix()
    boca()



def dibujar():
    #rutinas de dibujo
    
    bolitas1()
    bolitas2()
    bolitas3()
    dibujarObstaculo()
    dibujarCarrito()


def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(800,800,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0,800,800)
        #Establece color de borrado
        glClearColor(0.0,0.0,0.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        actualizar(window)
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()