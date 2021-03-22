from OpenGL.GL import *
from glew_wish import *
from math import* 
import glfw
 

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
    glVertex(-0.56, 0.78, 0.0)
    glVertex(-0.56, 0.54, 0.0)
    glVertex(-0.78, 0.54, 0.0)
    #RayaIzquierdaArriba
    glVertex(-0.36, 0.98, 0.0)
    glVertex(-0.34, 0.98, 0.0)
    glVertex(-0.34, 0.54, 0.0)
    glVertex(-0.36, 0.54, 0.0)
    #EsquinaDerechaArriba
    
    glVertex(0.76, 0.78, 0.0)
    glVertex(0.54, 0.78, 0.0)
    glVertex(0.54, 0.54, 0.0)
    glVertex(0.76, 0.54, 0.0)

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
    glVertex(-0.78, -0.34, 0.0)
    glVertex(-0.56, -0.34, 0.0)
    glVertex(-0.56, -0.56, 0.0)
    glVertex(-0.78, -0.56, 0.0)

    #RayaIzquierdaAbajo
    glVertex(-0.34, -0.34, 0.0)
    glVertex(-0.32, -0.34, 0.0)
    glVertex(-0.32, -0.76, 0.0)
    glVertex(-0.34, -0.76, 0.0)
    #EsquinaDerechaAbajo
    glVertex(0.56, -0.34, 0.0)
    glVertex(0.78, -0.34, 0.0)
    glVertex(0.78, -0.58, 0.0)
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
    glVertex(0.11, -0.56, 0.0)
    glVertex(-0.09, -0.56, 0.0)


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

    glVertex(-0.09, 0.78, 0.0)
    glVertex(0.11, 0.78, 0.0)
    glVertex(0.11, 0.54, 0.0)
    glVertex(-0.09, 0.54, 0.0)

    glEnd()

def bolitas():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 -0.88, sin(angulo) * 0.02 + 0.88, 0.0)

    glEnd()

def bolitas2():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 -0.68, sin(angulo) * 0.02 + 0.88, 0.0)

    glEnd()

def bolitas3():
    glColor3f(1.0,1.0,1.0)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos(angulo) * 0.02 -0.48, sin(angulo) * 0.02 + 0.88, 0.0)
    glEnd()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(700,700,"Mi ventana", None, None)

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
        glViewport(0,0,700,700)
        #Establece color de borrado
        glClearColor(0,0,0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        paredes()
        bolitas()
        bolitas2()
        bolitas3()

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