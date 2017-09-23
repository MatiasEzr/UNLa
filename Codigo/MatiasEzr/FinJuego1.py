import pygame
import random
pygame.init()
sonido1=pygame.mixer.Sound("MetalSlug.wav")#Crear sonido

pantalla=pygame.display.set_mode((480,500))#Ventana
fuente1=pygame.font.SysFont("Arial",20,True,False) #Fuente
info=fuente1.render("Tenes 10 segundos",0,(255,255,255))#Texto
salir=False
reloj1= pygame.time.Clock()
listarec=[]#Lista rectangulos
segundosint=0
termino=False
r1= pygame.Rect(0,0,10,10)#Posicion de rectangulo r1
rotos=0
for x in range(35):
	w=random.randrange(5,30)
	h=random.randrange(5,25)
	x=random.randrange(450)
	y=random.randrange(450)
	listarec.append(pygame.Rect(x,y,w,h))#crea lista rectangulos y almacena
						  #x=posicion entre 0 y 450 y=idem w y h =tamaño
while salir!=True:
	for event in pygame.event.get(): #Recorrer evento de pygame
		if event.type == pygame.QUIT: #if para salir del programa
			salir=True
			
		if event.type==pygame.MOUSEBUTTONDOWN: #agregarColision
			for recs in listarec:
				if termino==False: #Si no termino el tiempo sigue destruyendo
					if r1.colliderect(recs): #(destruye los rectangulos)
						sonido1.play() #se escucha el sonido
						recs.width=0 #los rectangulos se achican
						recs.height=0
						rotos+=1
	reloj1.tick(20)	#Controlar fps
	(r1.left,r1.top)=pygame.mouse.get_pos()#Controlar r1 por mouse
	r1.left-=r1.width/2 #acomodar mouse en el centro
	r1.top-=r1.height/2
	pantalla.fill((0,0,0)) #Fill es color de pantalla
	
	
	for recs in listarec:
		pygame.draw.rect(pantalla,(250,0,0),recs) #mostrar rectangulos
	pygame.draw.rect(pantalla,(0,0,250),r1)	#mostrar rectangulo
	pantalla.blit(info,(5,5))#poner texto
	if segundosint>=10: #Si los segundosint==10 fin del juego
		termino=True
	if termino==False:
		segundosint= pygame.time.get_ticks()/1000 #crear cronometro
		segundos= str(segundosint) #Convertir los segundos a cadena
		contador=fuente1.render(segundos,0,(0,250,0))#crear cronometro
	else:
		contador=fuente1.render("Usted rompio "+str(rotos),0,(0,250,0))
	pantalla.blit(contador,(290,10))#mostrar cronometro
	pygame.display.update()	

pygame.quit()
