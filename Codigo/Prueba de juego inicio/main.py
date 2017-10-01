import pygame, sys, time, math
from Scripts.UltraColor import *
from Scripts.Textures import *
from Scripts.globals import *
from Scripts.map_engine import *
from Scripts.NPC import *
from Scripts.player import *
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



player = Player("Barmi")
player_w, player_h = player.width, player.height
player_x = ((window_ancho / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
player_y = ((window_altura / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)


  
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w:
                Globals.camera_move = 1
                player.facing = "north"
            elif event.key == pygame.K_s:
                Globals.camera_move = 2
                player.facing = "south"
            elif event.key == pygame.K_a:
                Globals.camera_move = 3
                player.facing = "east"
            elif event.key == pygame.K_d:
                Globals.camera_move = 4
                player.facing = "west"

        elif event.type == pygame.KEYUP:
            Globals.camera_move == 0

        

    #Logic 
    if Globals.camera_move == 1:
        if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
            Globals.camera_y += 100 * deltatime
    elif Globals.camera_move == 2:
        if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
            Globals.camera_y -= 100 * deltatime
    elif Globals.camera_move == 3:
        if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
            Globals.camera_x += 100 * deltatime
    elif Globals.camera_move == 4:
        if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
            Globals.camera_x -= 100 * deltatime

    player_x = ((window_ancho / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
    player_y = ((window_altura / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)

        
        
            
          

    # Render graphics: Lo que hay dentro de la ventana

    window.blit(Sky, (0, 0))

    #Terreno

    window.blit(terrain, (Globals.camera_x, Globals.camera_y))

    player.render(window, (window_ancho / 2 - player_w / 2, window_altura / 2 - player_h / 2))

    show_fps()

    



    

    pygame.display.update()

    count_fps()


pygame.quit()
sys.exit()
