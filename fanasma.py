from OpenGL.GL import *
from glew_wish import *
import glfw

from math import* 
from random import randint
import random 


xObstaculo = 0.0
yObstaculo = 0.6

xFantasma = 0.0
yFantasma = 0.0

xFantasma1 = 0.5
yFantasma1 = 0.5

xFantasma2 = -0.5
yFantasma2 = 0.5

colisionando = False
direccion = 0

rotacion = 0
rotacionboca = 0
desfase = 5900

def chocando(x1, y1, w1, h1, x2, y2, w2, h2):
    # w1 es la mitad del ancho del primer objeto
    # h1 es la mitad del alto del primer objeto
    # w2 es la mitad del ancho del segundo objeto
    # h2 es la mitad del alto del segundo objeto
    if x1 + w1 > x2 - w2 and x1 - w1 < x2 + w2 and y1 + h1 > y2 - h2 and y1 - h1 < y2 + h2:
        return True
    return False

def checar_colisiones():
    #cambiar a xpacman ypacman
    global colisionando
    if xFantasma + 0.05 > xObstaculo - 0.15 and xFantasma - 0.05 < xObstaculo + 0.15 and yFantasma + 0.05 > yObstaculo - 0.15 and yFantasma - 0.05 < yObstaculo + 0.15:
        colisionando = True
    else:
        colisionando = False


def actualizar(window):
    global xFantasma
    global yFantasma

    global xFantasma1
    global yFantasma1

    global xFantasma2
    global yFantasma2
    global direccion
    global rotacion
    global desfase

    
    
    yFantasmaR = random.random()/2
    yFantasma = yFantasma +0.005 * yFantasmaR
    xFantasmaR = random.random()/2
    xFantasma = xFantasma +0.01 * xFantasmaR


    yFantasmaR1 = random.random()/2
    yFantasma1 = yFantasma1 -0.005 * yFantasmaR1
    xFantasmaR1 = random.random()/2
    xFantasma1 = xFantasma1 -0.01 * xFantasmaR1

    yFantasmaR2 = random.random()/2
    yFantasma2 = yFantasma2 -0.005 * yFantasmaR2
    xFantasmaR2 = random.random()/2
    xFantasma2 = xFantasma2 * xFantasmaR2
    
    if not chocando(xFantasma, yFantasma + 0.01,0.05,0.05, xObstaculo, yObstaculo, 0.15,0.15):
        yFantasma = yFantasma + 0.01
    #checar_colisiones()
    
def dibujarObstaculo():
    global xObstaculo
    global yObstaculo

    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo, 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex(-0.15, 0.15, 0.0)
    glVertex(0.15, 0.15, 0.0)
    glVertex(0.15, -0.15, 0.0)
    glVertex(-0.15, -0.15, 0.0)
    glEnd()
    glPopMatrix()





def dibujarPacman():

    global colisionando
    global xFantasma
    global yFantasma
    glPushMatrix()
    glTranslate(xFantasma,yFantasma, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    if colisionando == True:
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
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
    glTranslate(xFantasma,yFantasma, 0.0)
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
    glTranslate(xFantasma,yFantasma, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 -0.03,sin(angulo)/60,0.0) 
    
   
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma,yFantasma, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 + 0.03,sin(angulo)/60,0.0) 
    
   
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslate(xFantasma,yFantasma, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 + 0.04,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma,yFantasma, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 -0.02,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()



def dibujarPacmanVerde():
    

    global colisionando
    global xFantasma1
    global yFantasma1
    glPushMatrix()
    glTranslate(xFantasma1,yFantasma1, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 1.0, 0.0)
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
    glTranslate(xFantasma1,yFantasma1, 0.0)
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
    glTranslate(xFantasma1,yFantasma1, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 -0.03,sin(angulo)/60,0.0) 
     
    glEnd()
    glPopMatrix()



    glPushMatrix()
    glTranslate(xFantasma1,yFantasma1, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 + 0.03,sin(angulo)/60,0.0) 
    
   
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslate(xFantasma1,yFantasma1, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 + 0.04,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma1,yFantasma1, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 -0.02,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()   
    
    
    


def dibujarPacmanAzul():
    

    global colisionando
    global xFantasma2
    global yFantasma2
    glPushMatrix()
    glTranslate(xFantasma2,yFantasma2, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0, 0.0, 2.0)
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
    glTranslate(xFantasma2,yFantasma2, 0.0)
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
    glTranslate(xFantasma2,yFantasma2, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 -0.03,sin(angulo)/60,0.0) 
     
    glEnd()
    glPopMatrix()



    glPushMatrix()
    glTranslate(xFantasma2,yFantasma2, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 + 0.03,sin(angulo)/60,0.0) 
    
   
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslate(xFantasma2,yFantasma2, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 + 0.04,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma2,yFantasma2, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 -0.02,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()   
    
    

    


def dibujar():
    # rutinas de dibujo
    
    glPushMatrix()
    
    dibujarPacman()
    dibujarPacmanVerde()
    dibujarPacmanAzul()
    glEnd()
    glPopMatrix()   
    
    
   
    

    
    


def main():
    # inicia glfw
    if not glfw.init():
        return

    # crea la ventana,
    # independientemente del SO que usemos
    window = glfw.create_window(800, 800, "Mi ventana", None, None)

    # Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    # Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    # Establecemos el contexto
    glfw.make_context_current(window)

    # Activamos la validación de
    # funciones modernas de OpenGL
    glewExperimental = True

    # Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    # Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        # Establece regiond e dibujo
        glViewport(0, 0, 800, 800)
        # Establece color de borrado
        glClearColor(0.4, 0.8, 0.1, 1)
        # Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Dibujar
        actualizar(window)
        dibujar()

        # Preguntar si hubo entradas de perifericos
        # (Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        # Intercambia los buffers
        glfw.swap_buffers(window)

    # Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    # Termina los procesos que inició glfw.init
    glfw.terminate()


if __name__ == "__main__":
    main()