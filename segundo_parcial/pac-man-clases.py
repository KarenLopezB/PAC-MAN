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
from Obstaculo import *
from Letras import *
from Bolita import *

bolitas = []

#fantasma3 = Fantasma3()
monito = Monito()
fantasma = Fantasmas()
fantasma2 = Fantasmas()
fantasma6 = Fantasma6()
fantasma4 = Fantasma4()
fantasma5 = Fantasma5()
fantasma3 = Fantasma3()
fantasma2 = Fantasma2()
letras = Letras()

obstaculos = []

def inicializarObstaculos():
    global obstaculos
    #
    #agregar todos los obstaculos con las posiciones debidas
    obstaculos.append(Obstaculo(-0.65,0.6))
    obstaculos.append(Obstaculo(-0.15,0.6))
    obstaculos.append(Obstaculo(0.45,0.6))
    obstaculos.append(Obstaculo(0.95,0.6))
    obstaculos.append(Obstaculo(-1.0,0.0))
    obstaculos.append(Obstaculo(-0.45,0.0))
    obstaculos.append(Obstaculo(0.4,0.0))
    obstaculos.append(Obstaculo(0.7,0.0))
    obstaculos.append(Obstaculo(-0.25,-0.6))
    obstaculos.append(Obstaculo(0.55,-0.6))
    obstaculos.append(Obstaculo(-0.9,-0.6))

def inicializarBolitas():
    global bolitas
    bolitas.append(Bolita(-0.88, 0.88))
    bolitas.append(Bolita(-0.68, 0.88))
    bolitas.append(Bolita(-0.48, 0.88))
    bolitas.append(Bolita(-0.28, 0.88))
    bolitas.append(Bolita(-0.08, 0.88))
    bolitas.append(Bolita(0.12, 0.88))
    bolitas.append(Bolita(0.32, 0.88))
    bolitas.append(Bolita(0.52, 0.88))
    bolitas.append(Bolita(0.72, 0.88))
    bolitas.append(Bolita(0.92, 0.88))
    bolitas.append(Bolita(-0.88, 0.30))
    bolitas.append(Bolita(-0.68, 0.30))
    bolitas.append(Bolita(-0.48, 0.30))
    bolitas.append(Bolita(-0.28, 0.30))
    bolitas.append(Bolita(-0.08, 0.30))
    bolitas.append(Bolita(0.12, 0.30))
    bolitas.append(Bolita(0.32, 0.30))
    bolitas.append(Bolita(0.52, 0.30))
    bolitas.append(Bolita(0.72, 0.30))
    bolitas.append(Bolita(0.92, 0.30))
    bolitas.append(Bolita(-0.88, -0.30))
    bolitas.append(Bolita(-0.68, -0.30))
    bolitas.append(Bolita(-0.48, -0.30))
    bolitas.append(Bolita(-0.28, -0.30))
    bolitas.append(Bolita(-0.08, -0.30))
    bolitas.append(Bolita(0.12, -0.30))
    bolitas.append(Bolita(0.32, -0.30))
    bolitas.append(Bolita(0.52, -0.30))
    bolitas.append(Bolita(0.72, -0.30))
    bolitas.append(Bolita(0.92, -0.30))
    bolitas.append(Bolita(-0.88, -0.87))
    bolitas.append(Bolita(-0.68, -0.87))
    bolitas.append(Bolita(0.48, -0.87))
    bolitas.append(Bolita(-0.28, -0.87))
    bolitas.append(Bolita(0.32, -0.87))
    bolitas.append(Bolita(0.52, -0.87))
    bolitas.append(Bolita(0.72, -0.87))
    bolitas.append(Bolita(0.92, -0.87))
    bolitas.append(Bolita(-0.89, 0.60))
    bolitas.append(Bolita(-0.39, 0.60))
    bolitas.append(Bolita(0.15, 0.60))
    bolitas.append(Bolita(0.70, 0.60))
    bolitas.append(Bolita(-0.72, 0.00))
    bolitas.append(Bolita(0.10, 0.00))
    bolitas.append(Bolita(-0.15, 0.00))
    bolitas.append(Bolita(0.93, 0.00))
    bolitas.append(Bolita(-0.58, -0.6))
    bolitas.append(Bolita(0.05, -0.6))
    bolitas.append(Bolita(0.25, -0.6))
    bolitas.append(Bolita(0.85, -0.6))

def actualizar(window):
    global monito
    global fantasma
    global obstaculos
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
    
    for obstaculo in obstaculos:
        monito.checar_colisiones_obstaculos(obstaculo)
        #exit()
        #monito.checar_colisiones(obstaculo)
          #  if monito.colisionando:
               # break
        
    for bolita in bolitas:
        monito.checar_colisiones_bolitas(bolitas)

def dibujar():
    global monito
    global fantasma
    global obstaculos
    #global fantasma3
    global fantasma6
    global fantasma4
    global fantasma5
    global fantasma3
    global fantasma2
    global letras
    global bolitas
    for bolita in bolitas:
        bolita.dibujar()
    letras.dibujar()
    for obstaculo in obstaculos:
        obstaculo.dibujar()
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
    window = glfw.create_window(700,700,"PacMan-Apocaliptico", None, None)

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

    inicializarObstaculos()

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
