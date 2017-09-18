import pygame, sys, time
from Scripts.UltraColor import *
from Scripts.Textures import *
from Scripts.globals import *
from Scripts.map_engine import *
pygame.init()

cSec = 0
cFrame = 0
FPS = 0

terrain = Map_Engine.load_map("maps\\el barmi.map")
        

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("graphics\\cielo.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky

#Metodo para mostrar los fps

def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.YellowGreen)
    window.blit(fps_overlay, (0,0))

def create_window():
    global window, window_altura, window_ancho, window_title
    window_ancho, window_altura = 800, 600
    window_title = "Nombre del juego"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_ancho, window_altura), pygame.HWSURFACE|pygame.DOUBLEBUF)


#Contador de FPS
    
def count_fps():
    global cSec, cFrame, FPS, deltatime

    if cSec == time.strftime("%S"):  #Segundo/Minuto/Hora en ese momento
        cFrame += 1
    else:
        FPS = cFrame
        cFrame = 0
        cSec = time.strftime("%S")
        if FPS > 0:
            deltatime = 1 / FPS
        

#Creacion de ventana principal (cambiar nombre desde window_title)


create_window()
  
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                Globals.camera_move = 1
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
            elif event.key == pygame.K_d:
                Globals.camera_move = 4

        elif event.type == pygame.KEYUP:
            Globals.camera_move == 0

        




    

    #Logic 
    if Globals.camera_move == 1:
        Globals.camera_y += 100 * deltatime
    elif Globals.camera_move == 2:
        Globals.camera_y -= 100 * deltatime
    elif Globals.camera_move == 3:
        Globals.camera_x += 100 * deltatime
    elif Globals.camera_move == 4:
        Globals.camera_x -= 100 * deltatime
        
        
            
          

    # Render graphics: Lo que hay dentro de la ventana

    window.blit(Sky, (0, 0))

    #Terreno

    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    show_fps()

    



    

    pygame.display.update()

    count_fps()


pygame.quit()
sys.exit()
