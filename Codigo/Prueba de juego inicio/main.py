import pygame, sys, time, math
from Scripts.Textures import *
from Scripts.globals import *
from Scripts.map_engine import *
from Scripts.NPC import *
from Scripts.player import *
from Scripts.meloonatic_gui import *
from Scripts.UltraColor import *
from Timer import *
pygame.init()

cSec = 0
cFrame = 0
FPS = 0

terrain = Map_Engine.load_map("maps\\Test1.map")
        

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("graphics\\cielo.png")
Sky = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
Sky.blit(sky, (0, 0))
del sky

logo_img_temp =pygame.image.load("graphics\\logo.png")
logo_img_temp= pygame.transform.scale(logo_img_temp,(200,200))
logo_img= pygame.Surface(logo_img_temp.get_size(),pygame.HWSURFACE)
logo_img.blit(logo_img_temp,(0,0))
del logo_img_temp


#Metodo para mostrar los fps

def show_fps():
    fps_overlay = fps_font.render(str(FPS), True, Color.YellowGreen)
    window.blit(fps_overlay, (0,0))

def create_window():
    global window, window_altura, window_ancho, window_title,clock
    window_ancho, window_altura = 800, 600
    window_title = "Nombre del juego"
    pygame.display.set_caption(window_title)
    window = pygame.display.set_mode((window_ancho, window_altura), pygame.HWSURFACE|pygame.DOUBLEBUF)
    clock=pygame.time.Clock()

#Contador de FPS
    
def count_fps():
    global FPS
    
    FPS= clock.get_fps()
    if FPS > 0:
        Globals.deltatime = 1 / FPS
        
        

#Creacion de ventana principal (cambiar nombre desde window_title)


create_window()



player = Player("Barmi")
player_w, player_h = player.width, player.height
player_x = ((window_ancho / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
player_y = ((window_altura / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)



man1= Male1(name="Andres", pos=(200,300))

#Inicializar GUI

def Play():
    Globals.scene="game"
def Exit():
    global isRunning
    isRunning =False

btnPlay= Menu.Button(text="Jugar",rect=(0,0,300,60),
                     tag= ("menu",None))
btnPlay.Left= window_ancho / 2 - btnPlay.Width /  2
btnPlay.Top= window_altura / 2 - btnPlay.Height /  2
btnPlay.Command= Play

btnExit=Menu.Button(text= "Salir", rect= (0,0,300,60),
                    tag= ("menu",None))

btnExit.Left=btnPlay.Left
btnExit.Top= btnPlay.Top+btnExit.Height+3
btnExit.Command=Exit


menuTitle= Menu.Text(text="Apocalipsis Minecraft",color= Color.Cyan,
                     font= Font.Large)
menuTitle.Left,menuTitle.Top=window_ancho/2 - menuTitle.Width / 2,0

logo= Menu.Image(bitmap=logo_img)
logo.Left= window_ancho/2 - logo.Height/2
logo.Top= menuTitle.Top + menuTitle.Height +3
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
            Globals.camera_move = 0

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #click izquierdo
                # Evento manejado boton click
                for btn in Menu.Button.All:
                    if btn.Tag[0]== Globals.scene and btn.Rolling:
                        if btn.Command!=None:
                            btn.Command()  #Do button event
                        btn.Rolling=False
                        break   #salir loop
                            
     
    #Render scene
    if Globals.scene=="game" :   

    
        #Logic 
        if Globals.camera_move == 1:
            if not Tiles.Blocked_At((round(player_x), math.floor(player_y))):
                Globals.camera_y += 100 * Globals.deltatime
        elif Globals.camera_move == 2:
            if not Tiles.Blocked_At((round(player_x), math.ceil(player_y))):
                Globals.camera_y -= 100 * Globals.deltatime
        elif Globals.camera_move == 3:
            if not Tiles.Blocked_At((math.floor(player_x), round(player_y))):
                Globals.camera_x += 100 * Globals.deltatime
        elif Globals.camera_move == 4:
            if not Tiles.Blocked_At((math.ceil(player_x), round(player_y))):
                Globals.camera_x -= 100 * Globals.deltatime

        player_x = ((window_ancho / 2 - player_w / 2 - Globals.camera_x) / Tiles.Size)
        player_y = ((window_altura / 2 - player_h / 2 - Globals.camera_y) / Tiles.Size)

            
            
                
              

        # Render graphics: Lo que hay dentro de la ventana

        window.blit(Sky, (0, 0))

        #Terreno

        window.blit(terrain, (Globals.camera_x, Globals.camera_y))

        for npc in NPC.AllNPCs:
            npc.Render(window)

        player.render(window, (window_ancho / 2 - player_w / 2, window_altura / 2 - player_h / 2))

    #Process menu
    elif Globals.scene=="menu":
        window.fill(Color.Fog)

        logo.Render(window)
        menuTitle.Render(window)
        for btn in Menu.Button.All:
           if btn.Tag[0]=="menu":
               btn.Render(window)
    
    show_fps()

    
    pygame.display.update()
    clock.tick(60)
    count_fps()


pygame.quit()
sys.exit()
