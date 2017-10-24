import pygame, sys, time
from Script.Color import *
from Script.texturas import *
from Script.globals import *
from Script.map_engine import*

pygame.init()

cSec = 0
cFrame = 0
FPS = 0

terrain = Mapa_Config.cargar_mapa("Mapas\\world.map")

fps_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

sky = pygame.image.load("Graficos\\sky.png")
cielo = pygame.Surface(sky.get_size(), pygame.HWSURFACE)
cielo.blit(sky, (0 ,0))

del sky

def show_fps():
	fps_overlay = fps_font.render(str(FPS), True, Color.YellowGreen)
	window.blit(fps_overlay, (0,0))
	
def create_window():
	global window, window_height, window_width, window_title
	window_width, window_height = 800, 600
	window_title = "Test"
	pygame.display.set_caption(window_title)
	window = pygame.display.set_mode((window_width, window_height), pygame.HWSURFACE|pygame.DOUBLEBUF)

def count_fps():
	global cSec, cFrame, FPS, deltatime
	
	if cSec == time.strftime("%S"):
		cFrame += 1
	else:
		FPS = cFrame
		cFrame = 0
		cSec = time.strftime("%S")
		if FPS > 0:
			deltatime = 1 / FPS

create_window()

isRunning = True

while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				Globales.camera_mov = 1
			elif event.key == pygame.K_s:
				Globales.camera_mov = 2
			elif event.key == pygame.K_a:
				Globales.camera_mov = 3
			elif event.key == pygame.K_d:
				Globales.camera_mov = 4
		
		elif event.type == pygame.KEYUP:
			Globales.camera_mov = 0
			

			
	# LOGIC
	if Globales.camera_mov == 1:
		Globales.camera_y += 100 * deltatime
	elif Globales.camera_mov == 2:
		Globales.camera_y -= 100 * deltatime
	elif Globales.camera_mov == 3:
		Globales.camera_x += 100 * deltatime
	elif Globales.camera_mov == 4:
		Globales.camera_x -= 100 * deltatime
			
	
	# Render Graphics
	window.blit(cielo, (0,0))
	
	window.blit(terrain, (Globales.camera_x, Globales.camera_y))
	
	show_fps()
	
	pygame.display.update()
	count_fps()
	# clock.tick(30)


pygame.quit()
sys.exit()
