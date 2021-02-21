from OpenGL.GL import *
from glew_wish import *
import glfw

from math import* 
from random import randint
import random 


xObstaculo = 0.0
yObstaculo = 0.6

xPacman = 0.0
yPacman = -0.8

colisionando = False
direccion = 0

rotacion = 0
rotacionboca = 0
desfase = 5900

xFantasma = 0.0
yFantasma = 0.0

xFantasma1 = 0.5
yFantasma1 = 0.5

xFantasma2 = -0.5
yFantasma2 = 0.5

def checar_colisiones():
    global colisionando
    if xPacman + 0.05 > xObstaculo - 0.15 and xPacman - 0.05 < xObstaculo + 0.15 and yPacman + 0.05 > yObstaculo - 0.15 and yPacman - 0.05 < yObstaculo + 0.15:
        colisionando = True
    else:
        colisionando = False

def actualizar(window):
    global xPacman
    global yPacman
    global direccion
    global rotacion
    global desfase

    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)

    if estadoIzquierda == glfw.PRESS:
        direccion = 2
        rotacion = 180 - desfase
       
    if estadoDerecha == glfw.PRESS:
        direccion = 1
        rotacion = 0 - desfase
        
    if estadoAbajo == glfw.PRESS:
        direccion = 3
        rotacion = 270 - desfase
    if estadoArriba == glfw.PRESS:
        direccion = 0
        rotacion = 90 - desfase

    if direccion == 0:
        yPacman = yPacman + 0.001
    elif direccion == 1:
        xPacman = xPacman + 0.001
    elif direccion == 2:
        xPacman = xPacman - 0.001
    else:
        yPacman = yPacman - 0.001

    checar_colisiones()

def paredes():
    #rutinas de dibujo
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.4, 1.0)
    #ParedIzquierda
    glVertex(-1, 1, 0.0)
    glVertex(-0.98, 1, 0.0)
    glVertex(-0.98, -1, 0.0)
    glVertex(-1, -1, 0.0)
    #ParedDerecha
    glVertex(0.98, 1, 0.0)
    glVertex(1, 1, 0.0)
    glVertex(1, -1, 0.0)
    glVertex(0.98, -1, 0.0)
    #ParedArriba
    glVertex(-0.98, 1, 0.0)
    glVertex(0.98, 1, 0.0)
    glVertex(0.98, 0.98, 0.0)
    glVertex(-0.98, 0.98, 0.0)
    #ParedAbajo
    glVertex(-0.98, -0.98, 0.0)
    glVertex(0.98, -0.98, 0.0)
    glVertex(0.98, -1, 0.0)
    glVertex(-0.98, -1, 0.0)
    #EsquinaIzquierdaArriba
    glVertex(-0.78, 0.78, 0.0)
    glVertex(-0.58, 0.78, 0.0)
    glVertex(-0.58, 0.76, 0.0)
    glVertex(-0.78, 0.76, 0.0)

    glVertex(-0.78, 0.56, 0.0)
    glVertex(-0.58, 0.56, 0.0)
    glVertex(-0.58, 0.54, 0.0)
    glVertex(-0.78, 0.54, 0.0)

    glVertex(-0.58, 0.78, 0.0)
    glVertex(-0.56, 0.78, 0.0)
    glVertex(-0.56, 0.54, 0.0)
    glVertex(-0.58, 0.54, 0.0)
    #RayaIzquierdaArriba
    glVertex(-0.36, 0.98, 0.0)
    glVertex(-0.34, 0.98, 0.0)
    glVertex(-0.34, 0.54, 0.0)
    glVertex(-0.36, 0.54, 0.0)
    #EsquinaDerechaArriba
    glVertex(0.76, 0.78, 0.0)
    glVertex(0.78, 0.78, 0.0)
    glVertex(0.78, 0.58, 0.0)
    glVertex(0.76, 0.58, 0.0)

    glVertex(0.54, 0.58, 0.0)
    glVertex(0.78, 0.58, 0.0)
    glVertex(0.78, 0.56, 0.0)
    glVertex(0.54, 0.56, 0.0)

    glVertex(0.54, 0.78, 0.0)
    glVertex(0.56, 0.78, 0.0)
    glVertex(0.56, 0.58, 0.0)
    glVertex(0.54, 0.58, 0.0)
    #RayaDerechaArriba
    glVertex(0.32, 0.98, 0.0)
    glVertex(0.34, 0.98, 0.0)
    glVertex(0.34, 0.56, 0.0)
    glVertex(0.32, 0.56, 0.0)
    #RayaArribadeScore
    glVertex(-0.98, -0.76, 0.0)
    glVertex(0.98, -0.76, 0.0)
    glVertex(0.98, -0.78, 0.0)
    glVertex(-0.98, -0.78, 0.0)
    #EsquinaIzquierdaAbajo
    glVertex(-0.78, -0.36, 0.0)
    glVertex(-0.76, -0.36, 0.0)
    glVertex(-0.76, -0.56, 0.0)
    glVertex(-0.78, -0.56, 0.0)

    glVertex(-0.78, -0.34, 0.0)
    glVertex(-0.56, -0.34, 0.0)
    glVertex(-0.56, -0.36, 0.0)
    glVertex(-0.78, -0.36, 0.0)
    
    glVertex(-0.56, -0.34, 0.0)
    glVertex(-0.54, -0.34, 0.0)
    glVertex(-0.54, -0.56, 0.0)
    glVertex(-0.56, -0.56, 0.0)
    #RayaIzquierdaAbajo
    glVertex(-0.34, -0.34, 0.0)
    glVertex(-0.32, -0.34, 0.0)
    glVertex(-0.32, -0.76, 0.0)
    glVertex(-0.34, -0.76, 0.0)
    #EsquinaDerechaAbajo
    glVertex(0.58, -0.34, 0.0)
    glVertex(0.78, -0.34, 0.0)
    glVertex(0.78, -0.36, 0.0)
    glVertex(0.58, -0.36, 0.0)

    glVertex(0.58, -0.56, 0.0)
    glVertex(0.78, -0.56, 0.0)
    glVertex(0.78, -0.58, 0.0)
    glVertex(0.58, -0.58, 0.0)

    glVertex(0.56, -0.34, 0.0)
    glVertex(0.58, -0.34, 0.0)
    glVertex(0.58, -0.58, 0.0)
    glVertex(0.56, -0.58, 0.0)
    #RayaDerechaAbajo
    glVertex(0.34, -0.34, 0.0)
    glVertex(0.36, -0.34, 0.0)
    glVertex(0.36, -0.76, 0.0)
    glVertex(0.34, -0.76, 0.0)

    #LineasAbajoCentro
    glVertex(-0.98, -0.14, 0.0)
    glVertex(-0.56, -0.14, 0.0)
    glVertex(-0.56, -0.12, 0.0)
    glVertex(-0.98, -0.12, 0.0)

    glVertex(-0.36, -0.14, 0.0)
    glVertex(-0.09, -0.14, 0.0)
    glVertex(-0.09, -0.12, 0.0)
    glVertex(-0.36, -0.12, 0.0)

    glVertex(0.54, -0.14, 0.0)
    glVertex(0.98, -0.14, 0.0)
    glVertex(0.98, -0.12, 0.0)
    glVertex(0.54, -0.12, 0.0)

    glVertex(0.11, -0.14, 0.0)
    glVertex(0.34, -0.14, 0.0)
    glVertex(0.34, -0.12, 0.0)
    glVertex(0.11, -0.12, 0.0)

    glVertex(-0.09, -0.34, 0.0)
    glVertex(0.11, -0.34, 0.0)
    glVertex(0.11, -0.32, 0.0)
    glVertex(-0.09, -0.32, 0.0)

    glVertex(-0.34, -0.54, 0.0)
    glVertex(-0.09, -0.54, 0.0)
    glVertex(-0.09, -0.56, 0.0)
    glVertex(-0.34, -0.56, 0.0)

    glVertex(0.11, -0.54, 0.0)
    glVertex(0.36, -0.54, 0.0)
    glVertex(0.36, -0.56, 0.0)
    glVertex(0.11, -0.56, 0.0)

    #CasitaFantasmasPacman
    glVertex(-0.34, 0.34, 0.0)
    glVertex(-0.09, 0.34, 0.0)
    glVertex(-0.09, 0.32, 0.0)
    glVertex(-0.34, 0.32, 0.0)

    glVertex(0.11, 0.34, 0.0)
    glVertex(0.34, 0.34, 0.0)
    glVertex(0.34, 0.32, 0.0)
    glVertex(0.11, 0.32, 0.0)

    glVertex(-0.34, 0.12, 0.0)
    glVertex(0.34, 0.12, 0.0)
    glVertex(0.34, 0.10, 0.0)
    glVertex(-0.34, 0.10, 0.0)

    glVertex(-0.36, 0.34, 0.0)
    glVertex(-0.34, 0.34, 0.0)
    glVertex(-0.34, 0.10, 0.0)
    glVertex(-0.36, 0.10, 0.0)

    glVertex(0.32, 0.34, 0.0)
    glVertex(0.34, 0.34, 0.0)
    glVertex(0.34, 0.10, 0.0)
    glVertex(0.32, 0.10, 0.0)

    #RayasLadoIzquierdo
    glVertex(-0.98, 0.34, 0.0)
    glVertex(-0.56, 0.34, 0.0)
    glVertex(-0.56, 0.32, 0.0)
    glVertex(-0.98, 0.32, 0.0)

    glVertex(-0.78, 0.12, 0.0)
    glVertex(-0.56, 0.12, 0.0)
    glVertex(-0.56, 0.10, 0.0)
    glVertex(-0.78, 0.10, 0.0)

    #RayasLadoDerecho
    glVertex(0.54, 0.34, 0.0)
    glVertex(0.98, 0.34, 0.0)
    glVertex(0.98, 0.32, 0.0)
    glVertex(0.54, 0.32, 0.0)

    glVertex(0.54, 0.12, 0.0)
    glVertex(0.78, 0.12, 0.0)
    glVertex(0.78, 0.10, 0.0)
    glVertex(0.54, 0.10, 0.0)

    #RayasArribaCentro
    glVertex(-0.34, 0.78, 0.0)
    glVertex(-0.09, 0.78, 0.0)
    glVertex(-0.09, 0.76, 0.0)
    glVertex(-0.34, 0.76, 0.0)

    glVertex(0.11, 0.78, 0.0)
    glVertex(0.34, 0.78, 0.0)
    glVertex(0.34, 0.76, 0.0)
    glVertex(0.11, 0.76, 0.0)

    glVertex(-0.09, 0.56, 0.0)
    glVertex(0.11, 0.56, 0.0)
    glVertex(0.11, 0.54, 0.0)
    glVertex(-0.09, 0.54, 0.0)

    glEnd()

def boca():
 
    global colisionando
    global xPacman
    global yPacman

    
    glPushMatrix()
    glTranslate(xPacman, yPacman, 0.0)
    glScale(0.5,0.5,0.0)
    glRotate(rotacion + 90 ,0.0,0.0,1.0)
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




def dibujarPacman():

    global colisionando
    global xPacman
    global yPacman
    #global time
    glPushMatrix()
    glTranslate(xPacman, yPacman, 0.0)
    glScale(0.5,0.5,0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    if colisionando == True:
        glColor3f(1.0, 1.0, 1.0)
    else:
        glColor3f(1.0, 0.0, 0.0)
    for a in range (360):
        angulo= a*3.14159/180
        glVertex3f(cos(angulo)/8,sin(angulo)/8,0.0)
    
    glEnd()
    glPopMatrix()
    boca()



def dibujar():
    # rutinas de dibujo
    #dibujarObstaculo()
   
     dibujarPacman()
     paredes()


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
        glClearColor(0,0,0,1)
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