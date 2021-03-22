from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
from Monito import *
#from Fantasma3 import *
from Fantasmas import *
from Fantasma6 import *
from Fantasma4 import *
from Fantasma5 import *
from Fantasma3 import *
from Fantasma2 import *


#fantasma3 = Fantasma3()
monito = Monito()
fantasma = Fantasmas()
fantasma2 = Fantasmas()
fantasma6 = Fantasma6()
fantasma4 = Fantasma4()
fantasma5 = Fantasma5()
fantasma3 = Fantasma3()
fantasma2 = Fantasma2()



def actualizar(window):
    global monito
    global fantasma
    #global fantasma6
    #global fantasma3

    monito.actualizar(window)
    fantasma.actualizar(window)
    #fantasma2.actualizar(window)
    fantasma6.actualizar(window)
    fantasma4.actualizar(window)
    fantasma5.actualizar(window)
    fantasma3.actualizar(window)
    fantasma2.actualizar(window)
    monito.checar_colisiones(fantasma)
    monito.checar_colisiones6(fantasma6)
    monito.checar_colisiones4(fantasma4)
    monito.checar_colisiones5(fantasma5)
    monito.checar_colisiones3(fantasma3)
    monito.checar_colisiones2(fantasma2)
    #monito.colision5(fantasma5)

def dibujar():
    global monito
    global fantasma
    
    #global fantasma3
    global fantasma6
    global fantasma4
    global fantasma5
    global fantasma3
    global fantasma2
    fantasma6.dibujar()
    fantasma5.dibujar()
    fantasma4.dibujar()
    fantasma3.dibujar()
    fantasma2.dibujar()
    monito.dibujar()
    fantasma.dibujar()
    #fantasma2.dibujar()
    #fantasma3.dibujar()

def main():
    #inicia glfw
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(700,700,"PAC-MIN", None, None)

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
        glClearColor(0.0,0.0,0.0,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        actualizar(window)
        dibujar()
        #playsound.playsound('pacman-intermission.mp3', True)

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
