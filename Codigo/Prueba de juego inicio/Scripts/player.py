import pygame
from Scripts.NPC import *

pygame.init()

class Player:

    def __init__(self, name): 
        self.name = name
        self.facing = "south"
        self.health = 100
        sprite = pygame.image.load("Graphics\\player.png")
        size = sprite.get_size() #Tamaño del Sprite
        self.width = size[0]          
        self.height = size[1]

        #Tomar los perfiles
        
        self.faces = get_faces(sprite) #llama al metodo que se encuentra
                                        #en NPC

    def render(self, surface, pos):
        surface.blit(self.faces[self.facing], pos)
        
