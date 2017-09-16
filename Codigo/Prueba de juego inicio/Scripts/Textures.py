import pygame

pygame.init()

class Tiles:  #Azulejos (cuadrados)

    Size = 32

    def Load_Texture(file, Size):
        bitmap = pygame.image.load(file)
        bitmap = pygame.transform.scale(bitmap, (Size, Size))
        surface = pygame.Surface((Size, Size), pygame.HWSURFACE|pygame.SRCALPHA)
        surface.blit(bitmap, (0, 0))
        return surface


    Pasto = Load_Texture("graphics\\pasto.png", Size)

    Piedras = Load_Texture("graphics\\piedras.png", Size)

    Agua = Load_Texture("graphics\\agua.png", Size)

    Texture_Tags = {"1" : Pasto, "2" : Piedras, "3" : Agua}

    
    
