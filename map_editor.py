import pygame, sys, math
from Script.Color import *
from Script.texturas import *

def exportar_mapa(file):
	map_data = ""
	
	#Obtener dimensiones de mapa
	max_x = 0
	max_y = 0
	
	for t in tile_data:
		if t[0] > max_x:
			max_x = t[0]
		if t[1] > max_y:
			max_y = t[1]
			
	#Guardar mapa
	for tile in tile_data:
		map_data = map_data + str(int(tile[0] / Tiles.size)) + "," + str(int(tile[1] / Tiles.size)) + ":" + tile[2] + "-"
	
	
	#Guardar Dimensiones del mapa
	map_data = map_data + str(int(max_x / Tiles.size)) + "," + str(int(max_y / Tiles.size))
	
	#Escribir mapa
	with open (file, "w") as mapfile:
		mapfile.write(map_data)
	

window = pygame.display.set_mode ((1280, 720), pygame.HWSURFACE)
pygame.display.set_caption("Editor de Mapa")
clock = pygame.time.Clock()

txt_font = pygame.font.Font("C:\\Windows\\Fonts\\Verdana.ttf", 20)

mouse_pos = 0
mouse_x, mouse_y = 0, 0

map_ancho, map_alto = 100 * Tiles.size, 100 * Tiles.size

selector = pygame.Surface((Tiles.size, Tiles.size), pygame.HWSURFACE|pygame.SRCALPHA)
selector.fill(Color.WithAlpha(100, Color.CornflowerBlue))

tile_data = []

camera_x, camera_y = 0, 0
camera_mov = 0

brush = "1"		#Pasto

#iniciar mapa predeterminado
for x in range(0, map_ancho, Tiles.size):
	for y in range(0, map_alto, Tiles.size):
		tile_data.append([x, y, "1"])

isRunning = True

while isRunning:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		if event.type == pygame.KEYDOWN:
			
			if event.key == pygame.K_w:
				camera_mov = 1
			elif event.key == pygame.K_s:
				camera_mov = 2
			elif event.key == pygame.K_a:
				camera_mov = 3
			elif event.key == pygame.K_d:
				camera_mov = 4
				
			#Brushes
			if event.key == pygame.K_F4:
				brush = "r"
			elif event.key == pygame.K_F1:
				selection = input("Colocar: ")
				brush = selection
				
			#Guardar Mapa
			if event.key == pygame.K_F11:
				name = input("Nombre mapa: ")
				exportar_mapa(name + ".map")
				print("El mapa se ha guardado exitosamente!")
				
		elif event.type == pygame.KEYUP:
			camera_mov = 0
			
		if event.type == pygame.MOUSEMOTION:
			mouse_pos = pygame.mouse.get_pos()
			mouse_x = math.floor(mouse_pos[0] / Tiles.size) * Tiles.size
			mouse_y = math.floor(mouse_pos[1] / Tiles.size) * Tiles.size
			
		if event.type == pygame.MOUSEBUTTONDOWN:
			tile = [mouse_x - camera_x, mouse_y - camera_y, brush]	#Mantiene esto en la lista
			
			found = False
			for t in tile_data:
				if t[0] == tile[0] and t[1] == tile[1]:
					found = True
					break
					
			if not found:
				if not brush == "r":
					tile_data.append(tile)
			else:
				if brush == "r":
					#Eliminar titulo
					for t in tile_data:
						if t[0] == tile[0] and t[1] == tile[1]:
							tile_data.remove(t)
							print("Entidad eliminada!")
				else:
					print("Una entidad se ha generado!")
						
							
				
	#Logico
	if camera_mov == 1:
		camera_y += Tiles.size
	elif camera_mov == 2:
		camera_y -= Tiles.size
	elif camera_mov == 3:
		camera_x += Tiles.size
	elif camera_mov == 4:
		camera_x -= Tiles.size
		
	window.fill(Color.Blue)
	
	#Igualar mapa
	for tile in tile_data:
		try:
			window.blit(Tiles.Textura_Tags[tile[2]], (tile[0] + camera_x, tile[1] + camera_y))
		except:
			pass
	
	#Draw Tile Highlighter
	window.blit(selector, (mouse_x, mouse_y))
	
	
	pygame.display.update()
	
	clock.tick(60)
	
pygame.quit()
sys.exit()
