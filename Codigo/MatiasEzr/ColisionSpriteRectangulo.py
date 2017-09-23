import pygame

pygame.init()
pantalla=pygame.display.set_mode((1000,500)) #resolucion pantalla

salir=False
reloj1= pygame.time.Clock() #definir reloj
imagen1= pygame.image.load("Chabon.png") #cambiar por imagenQueQuieran
vx=0 #valor inicial
vy=0  				
								#si aumentas y va para abajo
r1=pygame.Rect(500,200,50,300) #(pos x,posa y,ancho,largo)
r2=pygame.Rect(100,200,50,300) #se puede agregar x cantidad de r
sprite1=pygame.sprite.Sprite()#crear sprite
sprite1.image=imagen1 #coloca una imagen al sprite
sprite1.rect=imagen1.get_rect() #devuelve ancho y alto de la imagen1(top,left)
sprite1.rect.top=250 #iguala el sprite a la posición del rectangulo
sprite1.rect.left=200 #o sea moves el sprite en que pos aparece de la ven
while salir!=True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			salir=True
		if event.type==pygame.KEYDOWN: #Movimiento con teclado
			if event.key==pygame.K_LEFT:
					vx-=10  #Al modificarse x u y el sprite se mueve
			if event.key==pygame.K_RIGHT :
					vx+=10
			if event.key==pygame.K_UP :
					vy-=10 	
			if event.key==pygame.K_DOWN:
					vy+=10 			
		if event.type==pygame.KEYUP: #al soltar la tecla
			if event.key==pygame.K_LEFT: #el movimiento vuelve 0 
					vx=0				#(se detiene)
			if event.key==pygame.K_RIGHT:
					vx=0
			if event.key==pygame.K_UP:
					vy=0	
			if event.key==pygame.K_DOWN:
					vy=0					
	reloj1.tick(60) #definir los fps
	oldx=sprite1.rect.left #contiene la posicion antes de colisionar
	oldy=sprite1.rect.top #pos de y antes de colision
	sprite1.rect.move_ip(vx,vy) #movimiento al sprite
	if sprite1.rect.colliderect(r1): #comprobar si colisiona
		sprite1.rect.left=oldx  #vuelve a su viejo x
		sprite1.rect.top=oldy	#vuelve a su viejo y
	if sprite1.rect.colliderect(r2): #Idem anterior
		sprite1.rect.left=oldx  
		sprite1.rect.top=oldy
	pantalla.fill((100,100,200))#color de pantalla
	pygame.draw.rect(pantalla,(0,0,0),(r1))#mostrar los rectangulos
	pygame.draw.rect(pantalla,(100,0,0),(r2))
	pantalla.blit(sprite1.image,sprite1.rect) #Superficie de pantalla
											#en este caso muestra el sprite
	pygame.display.update()

pygame.quit()			
