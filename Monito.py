from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import time



segundero=0


xObstaculo = 0.0
yObstaculo = 0.6

xPacman = 0.0
yPacman = -0.8

colisionando = False
direccion = 0

rotacion = 0
rotacionboca = 0
desfase = 5900


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


def boca():
 
    global colisionando
    global xPacman
    global yPacman

    
    glPushMatrix()
    glTranslate(xPacman, yPacman, 0.0)
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
    global time
    glPushMatrix()
    glTranslate(xPacman, yPacman, 0.0)
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