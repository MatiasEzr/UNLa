import pygame, sys, time
from Scripts.UltraColor import *
from Scripts.Textures import *

pygame.init()

cSec = 0
cFrame = 0
FPS = 0

title_size = 32

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

#Metodo para mostrar los fps

def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.YellowGreen)
    window.blit(fps_overlay, (0,0))

def create_window():
    global window, window_altura, window_ancho, window_title
    window_ancho, window_altura = 800, 600
    window_title = "Barmi"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_ancho, window_altura), pygame.HWSURFACE|pygame.DOUBLEBUF)


#Contador de FPS
    
def count_fps():
    global cSec, cFrame, FPS

    if cSec == time.strftime("%S"):  #Segundo/Minuto/Hora en ese momento
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        

#Creacion de ventana principal (cambiar nombre desde window_title)


create_window()
  
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    #Logic (supuestamente poniendo el metodo count_fps() repite todo el tiempo y va sumando los fps, pero no se que pasa que queda en 0
            count_fps()
          

    # Render graphics: Lo que hay dentro de la ventana

    window.fill(Color.Black)

    #Terreno
    for x in range (0, 640, title_size):
        for y in range (0,480, title_size):
            pygame.draw.rect(window, Color.White, (x, y, title_size +1, title_size +1),1)
    
    show_fps()

    



    

    pygame.display.update()



pygame.quit()
sys.exit()
