from OpenGL.GL import *
from glew_wish import *
import glfw
from math import* 
from random import randint
import random 
import playsound
from tkinter import *

rotacionC=0
xObstaculo = -0.65
yObstaculo = 0.6

xObstaculo2 = -0.15
yObstaculo2 = 0.6

xObstaculo3 = 0.45
yObstaculo3 = 0.6

xObstaculo4 = 0.95
yObstaculo4 = 0.6

xFantasma1 = 0.5
yFantasma1 = 0.5

xFantasma = 0.0
yFantasma = 0.0

xFantasma2 = -0.5
yFantasma2 = 0.5

xFantasma3 = 1.0
yFantasma3 = -0.2

xFantasma4 = -0.5
yFantasma4 = -0.5

xFantasma5 = 0.8
yFantasma5 = 0.5

xObstaculo5 = -1
yObstaculo5 = 0.0

xObstaculo6 = -0.45
yObstaculo6 = 0.0

xObstaculo7 =0.4
yObstaculo7 = 0.0

xObstaculo8 = 0.7
yObstaculo8 = 0.0

xObstaculo9 = -0.25
yObstaculo9 = -0.6

xObstaculo10 =0.55
yObstaculo10 = -0.6

xObstaculo11 = -0.9
yObstaculo11 = -0.6

xCarrito = 0.0
yCarrito = -0.8
rotacion=0
direccion = 0

colisionando = False


desfase = 5900

xbolitas1=-0.88
ybolitas1=0.88
obstaculoVivo1=True

xbolitas2=-0.68
ybolitas2=0.88
obstaculoVivo2=True

xbolitas3=-0.48
ybolitas3=0.88
obstaculoVivo3=True

xbolitas4=-0.28
ybolitas4=0.88
obstaculoVivo4=True

xbolitas5=-0.08
ybolitas5=0.88
obstaculoVivo5=True

xbolitas6=0.12
ybolitas6=0.88
obstaculoVivo6=True

xbolitas7=0.32
ybolitas7=0.88
obstaculoVivo7=True

xbolitas8=0.52
ybolitas8=0.88
obstaculoVivo8=True

xbolitas9=0.72
ybolitas9=0.88
obstaculoVivo9=True

xbolitas10=0.92
ybolitas10=0.88
obstaculoVivo10=True

xbolitas11=-0.88
ybolitas11=0.30
obstaculoVivo11=True

xbolitas12=-0.68
ybolitas12=0.30
obstaculoVivo12=True

xbolitas13=-0.48
ybolitas13=0.30
obstaculoVivo13=True

xbolitas14=-0.28
ybolitas14=0.30
obstaculoVivo14=True

xbolitas15=-0.08
ybolitas15=0.30
obstaculoVivo15=True

xbolitas16=0.12
ybolitas16=0.30
obstaculoVivo16=True

xbolitas17=0.32
ybolitas17=0.30
obstaculoVivo17=True

xbolitas18=0.52
ybolitas18=0.30
obstaculoVivo18=True

xbolitas19=0.72
ybolitas19=0.30
obstaculoVivo19=True

xbolitas20=0.92
ybolitas20=0.30
obstaculoVivo20=True

xbolitas21=-0.88
ybolitas21=-0.30
obstaculoVivo21=True

xbolitas22=-0.68
ybolitas22=-0.30
obstaculoVivo22=True

xbolitas23=-0.48
ybolitas23=-0.30
obstaculoVivo23=True

xbolitas24=-0.28
ybolitas24=-0.30
obstaculoVivo24=True

xbolitas25=-0.08
ybolitas25=-0.30
obstaculoVivo25=True

xbolitas26=0.12
ybolitas26=-0.30
obstaculoVivo26=True

xbolitas27=0.32
ybolitas27=-0.30
obstaculoVivo27=True

xbolitas28=0.52
ybolitas28=-0.30
obstaculoVivo28=True

xbolitas29=0.72
ybolitas29=-0.30
obstaculoVivo29=True

xbolitas30=0.92
ybolitas30=-0.30
obstaculoVivo30=True

xbolitas31=-0.88
ybolitas31=-0.87
obstaculoVivo31=True

xbolitas32=-0.68
ybolitas32=-0.87
obstaculoVivo32=True

xbolitas33=-0.48
ybolitas33=-0.87
obstaculoVivo33=True

xbolitas34=-0.28
ybolitas34=-0.87
obstaculoVivo34=True

xbolitas35=0.32
ybolitas35=-0.87
obstaculoVivo35=True

xbolitas36=0.52
ybolitas36=-0.87
obstaculoVivo36=True

xbolitas37=0.72
ybolitas37=-0.87
obstaculoVivo37=True

xbolitas38=0.92
ybolitas38=-0.87
obstaculoVivo38=True

xbolitas39=-0.89
ybolitas39=0.60
obstaculoVivo39=True

xbolitas40=-0.39
ybolitas40=0.60
obstaculoVivo40=True

xbolitas41=0.15
ybolitas41=0.60
obstaculoVivo41=True

xbolitas42=0.70
ybolitas42=0.60
obstaculoVivo42=True

xbolitas43=-0.72
ybolitas43=0.00
obstaculoVivo43=True

xbolitas44=0.10
ybolitas44=0.00
obstaculoVivo44=True

xbolitas45=-0.15
ybolitas45=0.00
obstaculoVivo45=True

xbolitas46=0.93
ybolitas46=0.00
obstaculoVivo46=True

xbolitas47=-0.58
ybolitas47=-0.6
obstaculoVivo47=True

xbolitas48=0.05
ybolitas48=-0.6
obstaculoVivo48=True

xbolitas49=0.25
ybolitas49=-0.6
obstaculoVivo49=True

xbolitas50=0.85
ybolitas50=-0.6
obstaculoVivo50=True

xBala = 0
yBala = 0
anguloBala=0


def checar_colisiones():
    global colisionando
    global bolitas1
    global bolitas2
    global bolitas3
    global bolitas4
    global bolitas5
    global bolitas6
    global bolitas7
    global bolitas8
    global bolitas9
    global bolitas10
    global bolitas11
    global bolitas12
    global bolitas13
    global bolitas14
    global bolitas15
    global bolitas16
    global bolitas17
    global bolitas18
    global bolitas19
    global bolitas20
    global bolitas21
    global bolitas22
    global bolitas23
    global bolitas24
    global bolitas25
    global bolitas26
    global bolitas27
    global bolitas28
    global bolitas29
    global bolitas30
    global bolitas31
    global bolitas32
    global bolitas33
    global bolitas34
    global bolitas35
    global bolitas36
    global bolitas37
    global bolitas38
    global bolitas39
    global bolitas40
    global bolitas41
    global bolitas42
    global bolitas43
    global bolitas44
    global bolitas45
    global bolitas46
    global bolitas47
    global bolitas48
    global bolitas47
    global bolitas48
    global bolitas49
    global bolitas50
    global obstaculoVivo1
    global obstaculoVivo2
    global obstaculoVivo3
    global obstaculoVivo4
    global obstaculoVivo5
    global obstaculoVivo6
    global obstaculoVivo7
    global obstaculoVivo8
    global obstaculoVivo9
    global obstaculoVivo10
    global obstaculoVivo11
    global obstaculoVivo12
    global obstaculoVivo13
    global obstaculoVivo14
    global obstaculoVivo15
    global obstaculoVivo16
    global obstaculoVivo17
    global obstaculoVivo18
    global obstaculoVivo19
    global obstaculoVivo20
    global obstaculoVivo21
    global obstaculoVivo22
    global obstaculoVivo23
    global obstaculoVivo24
    global obstaculoVivo25
    global obstaculoVivo26
    global obstaculoVivo27
    global obstaculoVivo28
    global obstaculoVivo29
    global obstaculoVivo30
    global obstaculoVivo31
    global obstaculoVivo32
    global obstaculoVivo33
    global obstaculoVivo34
    global obstaculoVivo35
    global obstaculoVivo36
    global obstaculoVivo37
    global obstaculoVivo38
    global obstaculoVivo39
    global obstaculoVivo40
    global obstaculoVivo41
    global obstaculoVivo42
    global obstaculoVivo43
    global obstaculoVivo44
    global obstaculoVivo45
    global obstaculoVivo46
    global obstaculoVivo47
    global obstaculoVivo48
    global obstaculoVivo49
    global obstaculoVivo50
    global xFantasma
    global yFantasma
    global xFantasma1
    global yFantasma1
    global xFantasma2
    global yFantasma2
    global xFantasma3
    global yFantasma3
    global xFantasma4
    global yFantasma4
    global xFantasma5
    global yFantasma5
    
    #si extremaDerechaCarrito > extremaIquierdaCarrito
    if xCarrito + 0.05> xObstaculo2 - 0.15 and xCarrito - 0.05 < xObstaculo2 + 0.15 and yCarrito + 0.05 > yObstaculo2 - 0.15 and yCarrito - 0.05 < yObstaculo2 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
        #obstaculoVivo=False
    elif xCarrito + 0.05> xObstaculo - 0.15 and xCarrito - 0.05 < xObstaculo + 0.15 and yCarrito + 0.05 > yObstaculo - 0.15 and yCarrito - 0.05 < yObstaculo + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
        #obstaculoVivo=False
    elif xCarrito + 0.05> xObstaculo3 - 0.15 and xCarrito - 0.05 < xObstaculo3 + 0.15 and yCarrito + 0.05 > yObstaculo3 - 0.15 and yCarrito - 0.05 < yObstaculo3 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo4 - 0.15 and xCarrito - 0.05 < xObstaculo4 + 0.15 and yCarrito + 0.05 > yObstaculo4 - 0.15 and yCarrito - 0.05 < yObstaculo4 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo5 - 0.15 and xCarrito - 0.05 < xObstaculo5 + 0.15 and yCarrito + 0.05 > yObstaculo5 - 0.15 and yCarrito - 0.05 < yObstaculo5 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo6 - 0.15 and xCarrito - 0.05 < xObstaculo6 + 0.15 and yCarrito + 0.05 > yObstaculo6 - 0.15 and yCarrito - 0.05 < yObstaculo6 + 0.15:
        playsound.playsound('pacman-dies.mp3', True)
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo7 - 0.15 and xCarrito - 0.05 < xObstaculo7 + 0.15 and yCarrito + 0.05 > yObstaculo7 - 0.15 and yCarrito - 0.05 < yObstaculo7 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo8 - 0.15 and xCarrito - 0.05 < xObstaculo8 + 0.15 and yCarrito + 0.05 > yObstaculo8 - 0.15 and yCarrito - 0.05 < yObstaculo8 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo9 - 0.15 and xCarrito - 0.05 < xObstaculo9 + 0.15 and yCarrito + 0.05 > yObstaculo9 - 0.15 and yCarrito - 0.05 < yObstaculo9 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo10 - 0.15 and xCarrito - 0.05 < xObstaculo10 + 0.15 and yCarrito + 0.05 > yObstaculo10 - 0.15 and yCarrito - 0.05 < yObstaculo10 + 0.15:
        playsound.playsound('pacman-dies.mp3', True) 
        colisionando = True
        exit()
    elif xCarrito + 0.05> xObstaculo11 - 0.15 and xCarrito - 0.05 < xObstaculo11 + 0.15 and yCarrito + 0.05 > yObstaculo11 - 0.15 and yCarrito - 0.05 < yObstaculo11 + 0.15:
        playsound.playsound('pacman-dies.mp3', True)        
        colisionando = True
        exit()

    #fantasmas

    elif xCarrito + 0.05> xFantasma - 0.09 and xCarrito - 0.05 < xFantasma + 0.09 and yCarrito + 0.05 > yFantasma - 0.09 and yCarrito - 0.05 < yFantasma + 0.09:
        playsound.playsound('pacman-dies.mp3', True)        
        colisionando = True
        exit()

    elif xCarrito + 0.05> xFantasma1 - 0.09 and xCarrito - 0.05 < xFantasma1 + 0.09 and yCarrito + 0.05 > yFantasma1 - 0.09 and yCarrito - 0.05 < yFantasma1 + 0.09:
        playsound.playsound('pacman-dies.mp3', True)        
        colisionando = True
        exit()
    
    elif xCarrito + 0.05> xFantasma2 - 0.09 and xCarrito - 0.05 < xFantasma2 + 0.09 and yCarrito + 0.05 > yFantasma2 - 0.09 and yCarrito - 0.05 < yFantasma2 + 0.09:
        playsound.playsound('pacman-dies.mp3', True)        
        colisionando = True
        exit()
        
    elif xCarrito + 0.05> xFantasma3 - 0.09 and xCarrito - 0.05 < xFantasma3 + 0.09 and yCarrito + 0.05 > yFantasma3 - 0.09 and yCarrito - 0.05 < yFantasma3 + 0.09:
        playsound.playsound('pacman-dies.mp3', True)        
        colisionando = True
        exit()    

    elif xCarrito + 0.05> xFantasma4 - 0.09 and xCarrito - 0.05 < xFantasma4 + 0.09 and yCarrito + 0.05 > yFantasma4 - 0.09 and yCarrito - 0.05 < yFantasma4 + 0.09:
        playsound.playsound('pacman-dies.mp3', True)        
        colisionando = True
        exit() 

    elif xCarrito + 0.05> xFantasma5 - 0.09 and xCarrito - 0.05 < xFantasma5 + 0.09 and yCarrito + 0.05 > yFantasma5 - 0.09 and yCarrito - 0.05 < yFantasma5 + 0.09:
        playsound.playsound('pacman-dies.mp3', True)        
        colisionando = True
        exit()    
        #resetPosition()

        
    elif xCarrito + 0.05> xbolitas1 - 0.05 and xCarrito - 0.05 < xbolitas1 + 0.05 and yCarrito + 0.05 > ybolitas1 - 0.05 and yCarrito - 0.05 < ybolitas1 + 0.05:
        
        obstaculoVivo1=False

    elif xCarrito + 0.05> xbolitas2 - 0.05 and xCarrito - 0.05 < xbolitas2 + 0.05 and yCarrito + 0.05 > ybolitas2 - 0.05 and yCarrito - 0.05 < ybolitas2 + 0.05:
        obstaculoVivo2=False

    elif xCarrito + 0.05> xbolitas3 - 0.05 and xCarrito - 0.05 < xbolitas3 + 0.05 and yCarrito + 0.05 > ybolitas3 - 0.05 and yCarrito - 0.05 < ybolitas3 + 0.05:
        obstaculoVivo3=False

    elif xCarrito + 0.05> xbolitas4 - 0.05 and xCarrito - 0.05 < xbolitas4 + 0.05 and yCarrito + 0.05 > ybolitas4 - 0.05 and yCarrito - 0.05 < ybolitas4 + 0.05:
        obstaculoVivo4=False
    
    elif xCarrito + 0.05> xbolitas5 - 0.05 and xCarrito - 0.05 < xbolitas5 + 0.05 and yCarrito + 0.05 > ybolitas5 - 0.05 and yCarrito - 0.05 < ybolitas5 + 0.05:
        obstaculoVivo5=False

    elif xCarrito + 0.05> xbolitas6 - 0.05 and xCarrito - 0.05 < xbolitas6 + 0.05 and yCarrito + 0.05 > ybolitas6 - 0.05 and yCarrito - 0.05 < ybolitas6 + 0.05:
        obstaculoVivo6=False

    elif xCarrito + 0.05> xbolitas7 - 0.05 and xCarrito - 0.05 < xbolitas7 + 0.05 and yCarrito + 0.05 > ybolitas7 - 0.05 and yCarrito - 0.05 < ybolitas7 + 0.05:
        obstaculoVivo7=False

    elif xCarrito + 0.05> xbolitas8 - 0.05 and xCarrito - 0.05 < xbolitas8 + 0.05 and yCarrito + 0.05 > ybolitas8 - 0.05 and yCarrito - 0.05 < ybolitas8 + 0.05:
        obstaculoVivo8=False

    elif xCarrito + 0.05> xbolitas9 - 0.05 and xCarrito - 0.05 < xbolitas9 + 0.05 and yCarrito + 0.05 > ybolitas9 - 0.05 and yCarrito - 0.05 < ybolitas9 + 0.05:
        obstaculoVivo9=False

    elif xCarrito + 0.05> xbolitas10 - 0.05 and xCarrito - 0.05 < xbolitas10 + 0.05 and yCarrito + 0.05 > ybolitas10 - 0.05 and yCarrito - 0.05 < ybolitas10 + 0.05:
        obstaculoVivo10=False
    
    elif xCarrito + 0.05> xbolitas11 - 0.05 and xCarrito - 0.05 < xbolitas11 + 0.05 and yCarrito + 0.05 > ybolitas11 - 0.05 and yCarrito - 0.05 < ybolitas11 + 0.05:
        obstaculoVivo11=False

    elif xCarrito + 0.05> xbolitas12 - 0.05 and xCarrito - 0.05 < xbolitas12 + 0.05 and yCarrito + 0.05 > ybolitas12 - 0.05 and yCarrito - 0.05 < ybolitas12 + 0.05:
        obstaculoVivo12=False

    elif xCarrito + 0.05> xbolitas13 - 0.05 and xCarrito - 0.05 < xbolitas13 + 0.05 and yCarrito + 0.05 > ybolitas13 - 0.05 and yCarrito - 0.05 < ybolitas13 + 0.05:
        obstaculoVivo13=False

    elif xCarrito + 0.05> xbolitas14 - 0.05 and xCarrito - 0.05 < xbolitas14 + 0.05 and yCarrito + 0.05 > ybolitas14 - 0.05 and yCarrito - 0.05 < ybolitas14 + 0.05:
        obstaculoVivo14=False

    elif xCarrito + 0.05> xbolitas15 - 0.05 and xCarrito - 0.05 < xbolitas15 + 0.05 and yCarrito + 0.05 > ybolitas15 - 0.05 and yCarrito - 0.05 < ybolitas15 + 0.05:
        obstaculoVivo15=False

    elif xCarrito + 0.05> xbolitas16 - 0.05 and xCarrito - 0.05 < xbolitas16 + 0.05 and yCarrito + 0.05 > ybolitas16 - 0.05 and yCarrito - 0.05 < ybolitas16 + 0.05:
        obstaculoVivo16=False
    
    elif xCarrito + 0.05> xbolitas17 - 0.05 and xCarrito - 0.05 < xbolitas17 + 0.05 and yCarrito + 0.05 > ybolitas17 - 0.05 and yCarrito - 0.05 < ybolitas17 + 0.05:
        obstaculoVivo17=False

    elif xCarrito + 0.05> xbolitas18 - 0.05 and xCarrito - 0.05 < xbolitas18 + 0.05 and yCarrito + 0.05 > ybolitas18 - 0.05 and yCarrito - 0.05 < ybolitas18 + 0.05:
        obstaculoVivo18=False

    elif xCarrito + 0.05> xbolitas19 - 0.05 and xCarrito - 0.05 < xbolitas19 + 0.05 and yCarrito + 0.05 > ybolitas19 - 0.05 and yCarrito - 0.05 < ybolitas19 + 0.05:
        obstaculoVivo19=False

    elif xCarrito + 0.05> xbolitas20 - 0.05 and xCarrito - 0.05 < xbolitas20 + 0.05 and yCarrito + 0.05 > ybolitas20 - 0.05 and yCarrito - 0.05 < ybolitas20 + 0.05:
        obstaculoVivo20=False

    elif xCarrito + 0.05> xbolitas21 - 0.05 and xCarrito - 0.05 < xbolitas21 + 0.05 and yCarrito + 0.05 > ybolitas21 - 0.05 and yCarrito - 0.05 < ybolitas21 + 0.05:
        obstaculoVivo21=False

    elif xCarrito + 0.05> xbolitas22 - 0.05 and xCarrito - 0.05 < xbolitas22 + 0.05 and yCarrito + 0.05 > ybolitas22 - 0.05 and yCarrito - 0.05 < ybolitas22 + 0.05:
        obstaculoVivo22=False
    
    elif xCarrito + 0.05> xbolitas23 - 0.05 and xCarrito - 0.05 < xbolitas23 + 0.05 and yCarrito + 0.05 > ybolitas23 - 0.05 and yCarrito - 0.05 < ybolitas23 + 0.05:
        obstaculoVivo23=False

    elif xCarrito + 0.05> xbolitas24 - 0.05 and xCarrito - 0.05 < xbolitas24 + 0.05 and yCarrito + 0.05 > ybolitas24 - 0.05 and yCarrito - 0.05 < ybolitas24 + 0.05:
        obstaculoVivo24=False

    elif xCarrito + 0.05> xbolitas25 - 0.05 and xCarrito - 0.05 < xbolitas25 + 0.05 and yCarrito + 0.05 > ybolitas25 - 0.05 and yCarrito - 0.05 < ybolitas25 + 0.05:
        obstaculoVivo25=False

    elif xCarrito + 0.05> xbolitas26 - 0.05 and xCarrito - 0.05 < xbolitas26 + 0.05 and yCarrito + 0.05 > ybolitas26 - 0.05 and yCarrito - 0.05 < ybolitas26 + 0.05:
        obstaculoVivo26=False

    elif xCarrito + 0.05> xbolitas27 - 0.05 and xCarrito - 0.05 < xbolitas27 + 0.05 and yCarrito + 0.05 > ybolitas27 - 0.05 and yCarrito - 0.05 < ybolitas27 + 0.05:
        obstaculoVivo27=False

    elif xCarrito + 0.05> xbolitas28 - 0.05 and xCarrito - 0.05 < xbolitas28 + 0.05 and yCarrito + 0.05 > ybolitas28 - 0.05 and yCarrito - 0.05 < ybolitas28 + 0.05:
        obstaculoVivo28=False
    
    elif xCarrito + 0.05> xbolitas29 - 0.05 and xCarrito - 0.05 < xbolitas29 + 0.05 and yCarrito + 0.05 > ybolitas29 - 0.05 and yCarrito - 0.05 < ybolitas29 + 0.05:
        obstaculoVivo29=False

    elif xCarrito + 0.05> xbolitas30 - 0.05 and xCarrito - 0.05 < xbolitas30 + 0.05 and yCarrito + 0.05 > ybolitas30 - 0.05 and yCarrito - 0.05 < ybolitas30 + 0.05:
        obstaculoVivo30=False

    elif xCarrito + 0.05> xbolitas31 - 0.05 and xCarrito - 0.05 < xbolitas31 + 0.05 and yCarrito + 0.05 > ybolitas31 - 0.05 and yCarrito - 0.05 < ybolitas31 + 0.05:
        obstaculoVivo31=False

    elif xCarrito + 0.05> xbolitas32 - 0.05 and xCarrito - 0.05 < xbolitas32 + 0.05 and yCarrito + 0.05 > ybolitas32 - 0.05 and yCarrito - 0.05 < ybolitas32 + 0.05:
        obstaculoVivo32=False

    elif xCarrito + 0.05> xbolitas33 - 0.05 and xCarrito - 0.05 < xbolitas33 + 0.05 and yCarrito + 0.05 > ybolitas33 - 0.05 and yCarrito - 0.05 < ybolitas33 + 0.05:
        obstaculoVivo33=False

    elif xCarrito + 0.05> xbolitas34 - 0.05 and xCarrito - 0.05 < xbolitas34 + 0.05 and yCarrito + 0.05 > ybolitas34 - 0.05 and yCarrito - 0.05 < ybolitas34 + 0.05:
        obstaculoVivo34=False
    
    elif xCarrito + 0.05> xbolitas35 - 0.05 and xCarrito - 0.05 < xbolitas35 + 0.05 and yCarrito + 0.05 > ybolitas35 - 0.05 and yCarrito - 0.05 < ybolitas35 + 0.05:
        obstaculoVivo35=False

    elif xCarrito + 0.05> xbolitas36 - 0.05 and xCarrito - 0.05 < xbolitas36 + 0.05 and yCarrito + 0.05 > ybolitas36 - 0.05 and yCarrito - 0.05 < ybolitas36 + 0.05:
        obstaculoVivo36=False

    elif xCarrito + 0.05> xbolitas37 - 0.05 and xCarrito - 0.05 < xbolitas37 + 0.05 and yCarrito + 0.05 > ybolitas37 - 0.05 and yCarrito - 0.05 < ybolitas37 + 0.05:
        obstaculoVivo37=False

    elif xCarrito + 0.05> xbolitas38 - 0.05 and xCarrito - 0.05 < xbolitas38 + 0.05 and yCarrito + 0.05 > ybolitas38 - 0.05 and yCarrito - 0.05 < ybolitas38 + 0.05:
        obstaculoVivo38=False

    elif xCarrito + 0.05> xbolitas39 - 0.05 and xCarrito - 0.05 < xbolitas39 + 0.05 and yCarrito + 0.05 > ybolitas39 - 0.05 and yCarrito - 0.05 < ybolitas39 + 0.05:
        obstaculoVivo39=False

    elif xCarrito + 0.05> xbolitas40 - 0.05 and xCarrito - 0.05 < xbolitas40 + 0.05 and yCarrito + 0.05 > ybolitas40 - 0.05 and yCarrito - 0.05 < ybolitas40 + 0.05:
        obstaculoVivo40=False
    
    elif xCarrito + 0.05> xbolitas41 - 0.05 and xCarrito - 0.05 < xbolitas41 + 0.05 and yCarrito + 0.05 > ybolitas41 - 0.05 and yCarrito - 0.05 < ybolitas41 + 0.05:
        obstaculoVivo41=False

    elif xCarrito + 0.05> xbolitas42 - 0.05 and xCarrito - 0.05 < xbolitas42 + 0.05 and yCarrito + 0.05 > ybolitas42 - 0.05 and yCarrito - 0.05 < ybolitas42 + 0.05:
        obstaculoVivo42=False

    elif xCarrito + 0.05> xbolitas43 - 0.05 and xCarrito - 0.05 < xbolitas43 + 0.05 and yCarrito + 0.05 > ybolitas43 - 0.05 and yCarrito - 0.05 < ybolitas43 + 0.05:
        obstaculoVivo43=False

    elif xCarrito + 0.05> xbolitas44 - 0.05 and xCarrito - 0.05 < xbolitas44 + 0.05 and yCarrito + 0.05 > ybolitas44 - 0.05 and yCarrito - 0.05 < ybolitas44 + 0.05:
        obstaculoVivo44=False

    elif xCarrito + 0.05> xbolitas45 - 0.05 and xCarrito - 0.05 < xbolitas45 + 0.05 and yCarrito + 0.05 > ybolitas45 - 0.05 and yCarrito - 0.05 < ybolitas45 + 0.05:
        obstaculoVivo45=False

    elif xCarrito + 0.05> xbolitas46 - 0.05 and xCarrito - 0.05 < xbolitas46 + 0.05 and yCarrito + 0.05 > ybolitas46 - 0.05 and yCarrito - 0.05 < ybolitas46 + 0.05:
        obstaculoVivo46=False
    
    elif xCarrito + 0.05> xbolitas47 - 0.05 and xCarrito - 0.05 < xbolitas47 + 0.05 and yCarrito + 0.05 > ybolitas47 - 0.05 and yCarrito - 0.05 < ybolitas47 + 0.05:
        obstaculoVivo47=False

    elif xCarrito + 0.05> xbolitas48 - 0.05 and xCarrito - 0.05 < xbolitas48 + 0.05 and yCarrito + 0.05 > ybolitas48 - 0.05 and yCarrito - 0.05 < ybolitas48 + 0.05:
        obstaculoVivo48=False

    elif xCarrito + 0.05> xbolitas49 - 0.05 and xCarrito - 0.05 < xbolitas49 + 0.05 and yCarrito + 0.05 > ybolitas49 - 0.05 and yCarrito - 0.05 < ybolitas49 + 0.05:
        obstaculoVivo49=False

    elif xCarrito + 0.05> xbolitas50 - 0.05 and xCarrito - 0.05 < xbolitas50 + 0.05 and yCarrito + 0.05 > ybolitas50 - 0.05 and yCarrito - 0.05 < ybolitas50 + 0.05:
        #playsound.playsound('pacman-waka-waka.mp3', True) 
        obstaculoVivo50=False

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
    global rotacionC

    global xFantasma1
    global yFantasma1

    global xFantasma
    global yFantasma
    global xFantasma2
    global yFantasma2
    global xFantasma3
    global yFantasma3
    global xFantasma4
    global yFantasma4
    global xFantasma5
    global yFantasma5

    
    #playsound.playsound('pacman-intermission.mp3', True)
    estadoIzquierda = glfw.get_key(window, glfw.KEY_LEFT)
    estadoDerecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)
    estadoArriba = glfw.get_key(window, glfw.KEY_UP)
    
    if estadoIzquierda == glfw.PRESS and colisionando == False:
        xCarrito = xCarrito - 0.2
        direccion = 2
        rotacionC = 180 - desfase
        #playsound.playsound('pacman-waka-waka.mp3', False)
        #playsound.playsound('pacman-waka-waka.mp3', True)
        playsound.playsound('pacman-waka-waka.mp3', True) 
    if estadoDerecha == glfw.PRESS and colisionando == False:
        xCarrito = xCarrito + 0.2
        direccion = 1
        rotacionC = 0 - desfase
        playsound.playsound('pacman-waka-waka.mp3', True) 
        #playsound.playsound('pacman-waka-waka.mp3', True)
    if estadoAbajo == glfw.PRESS and colisionando == False:
        yCarrito = yCarrito - 0.2
        direccion = 3
        rotacionC = 270 - desfase
        playsound.playsound('pacman-waka-waka.mp3', True) 
        #playsound.playsound('pacman-waka-waka.mp3', True)
    if estadoArriba == glfw.PRESS and colisionando == False:
        yCarrito = yCarrito + 0.2
        direccion = 0
        rotacionC = 90 - desfase
        playsound.playsound('pacman-waka-waka.mp3', True) 
        #playsound.playsound('pacman-waka-waka.mp3', True)
        #playsound.playsound('pacman-waka-waka.mp3', True)
    
    yFantasmaR1 =sin(random.random())
    yFantasma1 = yFantasma1 -0.005 * yFantasmaR1
    xFantasmaR1 = cos(random.random())
    xFantasma1 = xFantasma1 -0.01 * xFantasmaR1

    yFantasmaR = sin(random.random())
    yFantasma = yFantasma1 +0.005 * yFantasmaR1
    xFantasmaR = cos(random.random())
    xFantasma = xFantasma +0.01 * xFantasmaR

    
    yFantasmaR2 = sin(60)#*random.random()
    yFantasma2 = yFantasma2 -0.005 * yFantasmaR2
    xFantasmaR2 = cos(90)#*random.random()
    xFantasma2 = xFantasma2 + 0.01 * xFantasmaR2

    yFantasmaR3 = random.random()
    yFantasma3 = yFantasma3 -0.005 * yFantasmaR3
    xFantasmaR3 = random.random()
    xFantasma3 = xFantasma3 * cos(xFantasmaR3)

    yFantasmaR4 = sin(30)*random.random()
    yFantasma4 = yFantasma4 -0.005 * yFantasmaR4
    xFantasmaR4 = cos(30)*random.random()
    xFantasma4 = xFantasma4 * cos(xFantasmaR4)

    yFantasmaR5 = random.random()
    yFantasma5 = yFantasma5 -0.005 * yFantasmaR5
    xFantasmaR5 = random.random()
    xFantasma5 = xFantasma5 * cos(xFantasmaR5)
    
    checar_colisiones()
    #playsound.playsound('pacman-waka-waka.mp3', True)
    #checar_bolitas()
    #playsound.playsound('pacman-intermission.mp3', True)


def dibujarObstaculo():
    global xObstaculo
    global yObstaculo
    global xObstaculo2
    global yObstaculo2
    global xObstaculo9
    global yObstaculo9
    global xObstaculo10
    global yObstaculo10

    
    glPushMatrix()
    glTranslate(xObstaculo, yObstaculo,0.0)
  
    glBegin(GL_QUADS)
        
    glColor3f(0.1,0.7,0.6)
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
    glColor3f(0.2,0.3,0.7)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo4, yObstaculo4,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.5,0.9)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo5, yObstaculo5,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.4,0.2,0.8)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo6, yObstaculo6,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.8,0.2,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo7, yObstaculo7,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.3,0.8,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()

    glPopMatrix()
    glPushMatrix()
    glTranslate(xObstaculo8, yObstaculo8,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.3,0.8,0.6)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

   
    glPushMatrix()
    glTranslate(xObstaculo9, yObstaculo9,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.6,0.2)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslate(xObstaculo10, yObstaculo10,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.9,0.2,0.3)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xObstaculo11, yObstaculo11,0.0)
    glBegin(GL_QUADS)
    glColor3f(0.5,0.2,0.1)
    glVertex3f(-0.15,0.15,0.0)
    glVertex3f(0.15,0.15,0.0)
    glVertex3f(0.15,-0.15,0.0)
    glVertex3f(-0.15,-0.15,0.0)
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

def dibujarPacmanVerde2():
    

    global colisionando
    global xFantasma4
    global yFantasma4
    glPushMatrix()
    glTranslate(xFantasma4,yFantasma4, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
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
    glTranslate(xFantasma4,yFantasma4, 0.0)
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
    glTranslate(xFantasma4,yFantasma4, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 -0.03,sin(angulo)/60,0.0) 
     
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma4,yFantasma4, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 + 0.03,sin(angulo)/60,0.0) 
   
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma4,yFantasma4, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 + 0.04,sin(angulo)/110,0.0) 
    
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma4,yFantasma4, 0.0)
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
    
def dibujarPacmanAzul2():
    

    global colisionando
    global xFantasma3
    global yFantasma3
    glPushMatrix()
    glTranslate(xFantasma3,yFantasma3, 0.0)
    
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.5, 0.5, 0.5)
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
    glTranslate(xFantasma3,yFantasma3, 0.0)
 
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
    glTranslate(xFantasma3,yFantasma3, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
   
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 -0.03,sin(angulo)/60,0.0) 
     
    glEnd()
    glPopMatrix()



    glPushMatrix()
    glTranslate(xFantasma3,yFantasma3, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 + 0.03,sin(angulo)/60,0.0) 
    
   
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslate(xFantasma3,yFantasma3, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
 
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 + 0.04,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma3,yFantasma3, 0.0)

    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 -0.02,sin(angulo)/110,0.0)
   
    glEnd()
    glPopMatrix()   

def dibujarPacmanAzul3():
    

    global colisionando
    global xFantasma5
    global yFantasma5
    glPushMatrix()
    glTranslate(xFantasma5,yFantasma5, 0.0)
    
    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.6, 0.0, 0.7)
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
    glTranslate(xFantasma5,yFantasma5, 0.0)
 
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
    glTranslate(xFantasma5,yFantasma5, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
   
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 -0.03,sin(angulo)/60,0.0) 
     
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslate(xFantasma5,yFantasma5, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
    
    glBegin(GL_POLYGON)
    glColor3f(1.0,1.0,1.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/60 + 0.03,sin(angulo)/60,0.0) 
    
   
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glTranslate(xFantasma5,yFantasma5, 0.0)
    glRotate(rotacion, 0.0, 0.0, 1.0)
 
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 + 0.04,sin(angulo)/110,0.0) 
    
   
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslate(xFantasma5,yFantasma5, 0.0)

    glRotate(rotacion, 0.0, 0.0, 1.0)
    glBegin(GL_POLYGON)
    glColor3f(0.0,0.0,0.0)
    for a in range (360):
        angulo= (a*3.14159/180)
        glVertex3f(cos(angulo)/110 -0.02,sin(angulo)/110,0.0)
   
    glEnd()
    glPopMatrix()

def bolitas1():
    global xbolitas1
    global ybolitas1
    global obstaculoVivo1
    if obstaculoVivo1:
        glPushMatrix()
        glTranslate(xbolitas1, ybolitas1,0.0)
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
    global obstaculoVivo2
    if obstaculoVivo2:
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
    global obstaculoVivo3
    if obstaculoVivo3:
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

def bolitas4():
    global xbolitas4
    global ybolitas4
    global obstaculoVivo4
    if obstaculoVivo4:
        glPushMatrix()
        glTranslate(xbolitas4, ybolitas4,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas5():
    global xbolitas5
    global ybolitas5
    global obstaculoVivo5
    if obstaculoVivo5:
        glPushMatrix()
        glTranslate(xbolitas5, ybolitas5,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas6():
    global xbolitas6
    global ybolitas6
    global obstaculoVivo6
    if obstaculoVivo6:
        glPushMatrix()
        glTranslate(xbolitas6, ybolitas6,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas7():
    global xbolitas7
    global ybolitas7
    global obstaculoVivo7
    if obstaculoVivo7:
        glPushMatrix()
        glTranslate(xbolitas7, ybolitas7,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas8():
    global xbolitas8
    global ybolitas8
    global obstaculoVivo8
    if obstaculoVivo8:
        glPushMatrix()
        glTranslate(xbolitas8, ybolitas8,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas9():
    global xbolitas9
    global ybolitas9
    global obstaculoVivo9
    if obstaculoVivo9:
        glPushMatrix()
        glTranslate(xbolitas9, ybolitas9,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas10():
    global xbolitas10
    global ybolitas10
    global obstaculoVivo10
    if obstaculoVivo10:
        glPushMatrix()
        glTranslate(xbolitas10, ybolitas10,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas11():
    global xbolitas11
    global ybolitas11
    global obstaculoVivo11
    if obstaculoVivo11:
        glPushMatrix()
        glTranslate(xbolitas11, ybolitas11,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas12():
    global xbolitas12
    global ybolitas12
    global obstaculoVivo12
    if obstaculoVivo12:
        glPushMatrix()
        glTranslate(xbolitas12, ybolitas12,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas13():
    global xbolitas13
    global ybolitas13
    global obstaculoVivo13
    if obstaculoVivo13:
        glPushMatrix()
        glTranslate(xbolitas13, ybolitas13,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas14():
    global xbolitas14
    global ybolitas14
    global obstaculoVivo14
    if obstaculoVivo14:
        glPushMatrix()
        glTranslate(xbolitas14, ybolitas14,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas15():
    global xbolitas15
    global ybolitas15
    global obstaculoVivo15
    if obstaculoVivo15:
        glPushMatrix()
        glTranslate(xbolitas15, ybolitas15,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas16():
    global xbolitas16
    global ybolitas16
    global obstaculoVivo16
    if obstaculoVivo16:
        glPushMatrix()
        glTranslate(xbolitas16, ybolitas16,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas17():
    global xbolitas17
    global ybolitas17
    global obstaculoVivo17
    if obstaculoVivo17:
        glPushMatrix()
        glTranslate(xbolitas17, ybolitas17,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas18():
    global xbolitas18
    global ybolitas18
    global obstaculoVivo18
    if obstaculoVivo18:
        glPushMatrix()
        glTranslate(xbolitas18, ybolitas18,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas19():
    global xbolitas19
    global ybolitas19
    global obstaculoVivo19
    if obstaculoVivo19:
        glPushMatrix()
        glTranslate(xbolitas19, ybolitas19,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas20():
    global xbolitas20
    global ybolitas20
    global obstaculoVivo20
    if obstaculoVivo20:
        glPushMatrix()
        glTranslate(xbolitas20, ybolitas20,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas21():
    global xbolitas21
    global ybolitas21
    global obstaculoVivo21
    if obstaculoVivo21:
        glPushMatrix()
        glTranslate(xbolitas21, ybolitas21,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas22():
    global xbolitas22
    global ybolitas22
    global obstaculoVivo22
    if obstaculoVivo22:
        glPushMatrix()
        glTranslate(xbolitas22, ybolitas22,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas23():
    global xbolitas23
    global ybolitas23
    global obstaculoVivo23
    if obstaculoVivo23:
        glPushMatrix()
        glTranslate(xbolitas23, ybolitas23,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas24():
    global xbolitas24
    global ybolitas24
    global obstaculoVivo24
    if obstaculoVivo24:
        glPushMatrix()
        glTranslate(xbolitas24, ybolitas24,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas25():
    global xbolitas25
    global ybolitas25
    global obstaculoVivo25
    if obstaculoVivo25:
        glPushMatrix()
        glTranslate(xbolitas25, ybolitas25,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas26():
    global xbolitas26
    global ybolitas26
    global obstaculoVivo26
    if obstaculoVivo26:
        glPushMatrix()
        glTranslate(xbolitas26, ybolitas26,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas27():
    global xbolitas27
    global ybolitas27
    global obstaculoVivo27
    if obstaculoVivo27:
        glPushMatrix()
        glTranslate(xbolitas27, ybolitas27,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas28():
    global xbolitas28
    global ybolitas28
    global obstaculoVivo28
    if obstaculoVivo28:
        glPushMatrix()
        glTranslate(xbolitas28, ybolitas28,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas29():
    global xbolitas29
    global ybolitas29
    global obstaculoVivo29
    if obstaculoVivo29:
        glPushMatrix()
        glTranslate(xbolitas29, ybolitas29,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas30():
    global xbolitas30
    global ybolitas30
    global obstaculoVivo30
    if obstaculoVivo30:
        glPushMatrix()
        glTranslate(xbolitas30, ybolitas30,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas31():
    global xbolitas31
    global ybolitas31
    global obstaculoVivo31
    if obstaculoVivo31:
        glPushMatrix()
        glTranslate(xbolitas31, ybolitas31,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas32():
    global xbolitas32
    global ybolitas32
    global obstaculoVivo32
    if obstaculoVivo32:
        glPushMatrix()
        glTranslate(xbolitas32, ybolitas32,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas33():
    global xbolitas33
    global ybolitas33
    global obstaculoVivo33
    if obstaculoVivo33:
        glPushMatrix()
        glTranslate(xbolitas33, ybolitas33,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas34():
    global xbolitas34
    global ybolitas34
    global obstaculoVivo34
    if obstaculoVivo34:
        glPushMatrix()
        glTranslate(xbolitas34, ybolitas34,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas35():
    global xbolitas35
    global ybolitas35
    global obstaculoVivo35
    if obstaculoVivo35:
        glPushMatrix()
        glTranslate(xbolitas35, ybolitas35,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas36():
    global xbolitas36
    global ybolitas36
    global obstaculoVivo36
    if obstaculoVivo36:
        glPushMatrix()
        glTranslate(xbolitas36, ybolitas36,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas37():
    global xbolitas37
    global ybolitas37
    global obstaculoVivo37
    if obstaculoVivo37:
        glPushMatrix()
        glTranslate(xbolitas37, ybolitas37,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas38():
    global xbolitas38
    global ybolitas38
    global obstaculoVivo38
    if obstaculoVivo38:
        glPushMatrix()
        glTranslate(xbolitas38, ybolitas38,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas39():
    global xbolitas39
    global ybolitas39
    global obstaculoVivo39
    if obstaculoVivo39:
        glPushMatrix()
        glTranslate(xbolitas39, ybolitas39,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas40():
    global xbolitas40
    global ybolitas40
    global obstaculoVivo40
    if obstaculoVivo40:
        glPushMatrix()
        glTranslate(xbolitas40, ybolitas40,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas41():
    global xbolitas41
    global ybolitas41
    global obstaculoVivo41
    if obstaculoVivo41:
        glPushMatrix()
        glTranslate(xbolitas41, ybolitas41,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas42():
    global xbolitas42
    global ybolitas42
    global obstaculoVivo42
    if obstaculoVivo42:
        glPushMatrix()
        glTranslate(xbolitas42, ybolitas42,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas43():
    global xbolitas43
    global ybolitas43
    global obstaculoVivo43
    if obstaculoVivo43:
        glPushMatrix()
        glTranslate(xbolitas43, ybolitas43,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas44():
    global xbolitas44
    global ybolitas44
    global obstaculoVivo44
    if obstaculoVivo44:
        glPushMatrix()
        glTranslate(xbolitas44, ybolitas44,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas45():
    global xbolitas45
    global ybolitas45
    global obstaculoVivo45
    if obstaculoVivo45:
        glPushMatrix()
        glTranslate(xbolitas45, ybolitas45,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas46():
    global xbolitas46
    global ybolitas46
    global obstaculoVivo46
    if obstaculoVivo46:
        glPushMatrix()
        glTranslate(xbolitas46, ybolitas46,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas47():
    global xbolitas47
    global ybolitas47
    global obstaculoVivo47
    if obstaculoVivo47:
        glPushMatrix()
        glTranslate(xbolitas47, ybolitas47,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas48():
    global xbolitas48
    global ybolitas48
    global obstaculoVivo48
    if obstaculoVivo48:
        glPushMatrix()
        glTranslate(xbolitas48, ybolitas48,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas49():
    global xbolitas49
    global ybolitas49
    global obstaculoVivo49
    if obstaculoVivo49:
        glPushMatrix()
        glTranslate(xbolitas49, ybolitas49,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()

def bolitas50():
    global xbolitas50
    global ybolitas50
    global obstaculoVivo50
    if obstaculoVivo50:
        glPushMatrix()
        glTranslate(xbolitas50, ybolitas50,0.0)
        glScale(0.2,0.2,0.2)
        glBegin(GL_QUADS)
        glColor3f(1.0,1.0,1.6)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.15,0.15,0.0)
        glVertex3f(0.15,-0.15,0.0)
        glVertex3f(-0.15,-0.15,0.0)
        glEnd()
        glPopMatrix()



def letras():
    glPushMatrix()
    glBegin(GL_LINES)
    glColor3f(0.8, 0.5, 0.3)
    glVertex(-0.15, 0.15, 0.0)
    glVertex(-0.15, -0.15, 0.0)
    glVertex(0.05, 0.15, 0.0)
    glVertex(0.05, -0.0, 0.0)

    glVertex(-0.15, -0.0, 0.0)
    glVertex(0.05, -0.0, 0.0)

    glVertex(-0.15, 0.15, 0.0)
    glVertex(0.05, 0.15, 0.0)

    glVertex(0.05, 0.15, 0.0)
    glVertex(0.05, 0.0, 0.0)
    glEnd()
    glPopMatrix()


    glPushMatrix()
    glBegin(GL_LINE_STRIP)
    glColor3f(0.8, 0.5, 0.3)
    glVertex(-0.15, 0.15, 0.0)
    glVertex(-0.15, -0.15, 0.0)
    glVertex(0.05, 0.15, 0.0)
    glVertex(0.05, -0.0, 0.0)

    glVertex(0.05, -0.15, 0.0)
    glVertex(0.05, 0.15, 0.0)

    glVertex(0.05, -0.15, 0.0)
    glVertex(0.09, 0.15, 0.0)

    glVertex(0.09, 0.15, 0.0)
    glVertex(0.22, -0.15, 0.0)
        #glVertex(0.05, 0.15, 0.0)
   

    glEnd()
    glPopMatrix()

    glPushMatrix()
    #glTranslate(-1,-0.9,0.0)
    glBegin(GL_LINES)
    glColor3f(0.8, 0.5, 0.3)
    glVertex(-0.99, -0.97, 0.0)
    glVertex(0.99, -0.97, 0.0)
    #glVertex(0.9, -0.8, 0.0)
    #glVertex(0.05, -0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    #glTranslate(-1,-0.9,0.0)
    glBegin(GL_LINES)
    glColor3f(0.8, 0.5, 0.3)
    glVertex(-0.99, 0.96, 0.0)
    glVertex(0.99, 0.96, 0.0)
    #glVertex(0.9, -0.8, 0.0)
    #glVertex(0.05, -0.0, 0.0)
    glEnd()
    glPopMatrix()

    
    glPushMatrix()
    #glTranslate(-1,-0.9,0.0)
    glBegin(GL_LINES)
    glColor3f(0.8, 0.5, 0.3)
    glVertex(-0.99, -0.96, 0.0)
    glVertex(-0.99, 0.96, 0.0)
    #glVertex(0.9, -0.8, 0.0)
    #glVertex(0.05, -0.0, 0.0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    #glTranslate(-1,-0.9,0.0)
    glBegin(GL_LINES)
    glColor3f(0.8, 0.5, 0.3)
    glVertex(0.99, -0.96, 0.0)
    glVertex(0.99, 0.96, 0.0)
    #glVertex(0.9, -0.8, 0.0)
    #glVertex(0.05, -0.0, 0.0)
    glEnd()
    glPopMatrix()

    

def dibujar():
    #rutinas de dibujo
    letras()
    bolitas1()
    bolitas2()
    bolitas3()
    bolitas4()
    bolitas5()
    bolitas6()
    bolitas7()
    bolitas8()
    bolitas9()
    bolitas10()
    bolitas11()
    bolitas12()
    bolitas13()
    bolitas14()
    bolitas15()
    bolitas16()
    bolitas17()
    bolitas18()
    bolitas19()
    bolitas20()
    bolitas21()
    bolitas22()
    bolitas23()
    bolitas24()
    bolitas25()
    bolitas26()
    bolitas27()
    bolitas28()
    bolitas29()
    bolitas30()
    bolitas31()
    bolitas32()
    bolitas33()
    bolitas34()
    bolitas35()
    bolitas36()
    bolitas37()
    bolitas38()
    bolitas39()
    bolitas40()
    bolitas41()
    bolitas42()
    bolitas43()
    bolitas44()
    bolitas45()
    bolitas46()
    bolitas47()
    bolitas48()
    bolitas49()
    bolitas50()
    dibujarObstaculo()
    dibujarCarrito()
    dibujarPacmanVerde()
    dibujarPacman()
    dibujarPacmanAzul()
    dibujarPacmanAzul2()
    dibujarPacmanVerde()
    dibujarPacman()
    dibujarPacmanAzul()
    dibujarPacmanAzul2()
    dibujarPacmanVerde2()
    dibujarPacmanAzul3()
    #playsound.playsound('pacman-intermission.mp3', True)


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