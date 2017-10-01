import pygame
from Scripts.Textures import *

class Map_Engine:

    def add_tile(tile, pos, addTo):
        addTo.blit(tile, (pos[0] * Tiles.Size, pos[1] * Tiles.Size))
    
                   

        
    def load_map(file):
        with open(file, "r") as mapfile:
            map_data = mapfile.read()
        

        #leer azulejos

        map_data = map_data.split("-")   #divide en la lista de azulejos

        map_size = map_data[len(map_data) -1]  #trae las dimensiones del mapa
        map_data.remove(map_size)
        map_size = map_size.split(",")
        map_size[0] = int(map_size[0]) * Tiles.Size
        map_size[1] = int(map_size[1]) * Tiles.Size

        tiles = []

        for tile in range(len(map_data)):
            map_data[tile] = map_data[tile].replace("\n", "")
            tiles.append(map_data[tile].split(":"))  #separa la posicion de la textura

        for tile in tiles:
            tile[0] = tile[0].split(",")   #separa posicion en lista
            pos = tile[0]
            for p in pos:
                pos[pos.index(p)] = int(p)  #convierte a int

            tiles[tiles.index(tile)] = (pos, tile[1])  #guarda a lista de azulejos


        #algoritmo de optimizacion de fps

        #crear terreno

        terrain = pygame.Surface(map_size, pygame.HWSURFACE)

        for tile in tiles:
            if tile[1] in Tiles.Texture_Tags:
                Map_Engine.add_tile(Tiles.Texture_Tags[tile[1]], tile[0], terrain)

            if tile[1] in Tiles.Blocked_Types:
                Tiles.Blocked.append(tile[0])
        

        return terrain
        
        
