import pygame
class Imagenes(object):
    def __init__(self):
        self.nombre="Unknown"
pygame.init()
pygame.display.set_mode((0,0))

attack=pygame.mixer.Sound("mundopict/atack.wav")
attack.set_volume(0.4)
hited=pygame.mixer.Sound("mundopict/hited.wav")
levelup=pygame.mixer.Sound("mundopict/Heavy Machine Gun.mp3")
gameoversound=pygame.mixer.Sound("mundopict/gameover.wav") 
disparosound=pygame.mixer.Sound("mundopict/disparo.wav")
disparosound.set_volume(0.6)



imagen1=pygame.image.load("mundopict/knightr1.png").convert_alpha()
imagen2=pygame.image.load("mundopict/knightr2.png").convert_alpha()
imagen1l=pygame.image.load("mundopict/knightl1.png").convert_alpha()
imagen2l=pygame.image.load("mundopict/knightl2.png").convert_alpha()    
imagen1t=pygame.image.load("mundopict/knightt1.png").convert_alpha()
imagen2t=pygame.image.load("mundopict/knightt2.png").convert_alpha()
imagen1b=pygame.image.load("mundopict/knightb1.png").convert_alpha()
imagen2b=pygame.image.load("mundopict/knightb2.png").convert_alpha()

ianciano= Imagenes()
ianciano.iancianor1=pygame.image.load("mundopict/ancianor1.png").convert_alpha()
ianciano.iancianor2=pygame.image.load("mundopict/ancianor2.png").convert_alpha()
ianciano.iancianol1=pygame.image.load("mundopict/ancianol1.png").convert_alpha()
ianciano.iancianol2=pygame.image.load("mundopict/ancianol2.png").convert_alpha()
ianciano.lista=[[ianciano.iancianor1,ianciano.iancianor2],[ianciano.iancianol1,ianciano.iancianol2],
                [],[]]

ivegeta= Imagenes()
ivegeta.ivegeta1=pygame.image.load("mundopict/vegeta1.png").convert_alpha()
ivegeta.ivegeta2=pygame.image.load("mundopict/vegeta2.png").convert_alpha()

ivegeta.lista=[[ivegeta.ivegeta1,ivegeta.ivegeta2],[ivegeta.ivegeta1,ivegeta.ivegeta2],
                [],[]]


iportal= Imagenes()
iportal.iportal1=pygame.image.load("mundopict/portal1.png").convert_alpha()
iportal.iportal2=pygame.image.load("mundopict/portal2.png").convert_alpha()

iportal.lista=[[iportal.iportal1,iportal.iportal2],[iportal.iportal1,iportal.iportal2],
                [],[]]

ientradaice= Imagenes()
ientradaice.ientradaice1=pygame.image.load("mundopict/entradaice.png").convert_alpha()
ientradaice.ientradaice2=pygame.image.load("mundopict/entradaice.png").convert_alpha()

ientradaice.lista=[[ientradaice.ientradaice1,ientradaice.ientradaice2],[ientradaice.ientradaice1,ientradaice.ientradaice2],
                [],[]]

iguardia= Imagenes()
iguardia.iguardiar1=pygame.image.load("mundopict/guardiar1.png").convert_alpha()
iguardia.iguardiar2=pygame.image.load("mundopict/guardiar2.png").convert_alpha()
iguardia.iguardial1=pygame.image.load("mundopict/guardial1.png").convert_alpha()
iguardia.iguardial2=pygame.image.load("mundopict/guardial2.png").convert_alpha()
iguardia.lista=[[iguardia.iguardiar1,iguardia.iguardiar2],[iguardia.iguardial1,iguardia.iguardial2],
                [],[]]    

imajor= Imagenes()
imajor.imajorr1=pygame.image.load("mundopict/majorr1.png").convert_alpha()
imajor.imajorr2=pygame.image.load("mundopict/majorr2.png").convert_alpha()
imajor.imajorl1=pygame.image.load("mundopict/majorl1.png").convert_alpha()
imajor.imajorl2=pygame.image.load("mundopict/majorl2.png").convert_alpha()
imajor.lista=[[imajor.imajorr1,imajor.imajorr2],[imajor.imajorl1,imajor.imajorl2],
                [],[]]   


ialdeano= Imagenes()
ialdeano.ialdeanob1=pygame.image.load("mundopict/aldeanob1.png").convert_alpha()
ialdeano.ialdeanob2=pygame.image.load("mundopict/aldeanob2.png").convert_alpha()
ialdeano.ialdeanot1=pygame.image.load("mundopict/aldeanot1.png").convert_alpha()
ialdeano.ialdeanot2=pygame.image.load("mundopict/aldeanot2.png").convert_alpha()
ialdeano.lista=[[ialdeano.ialdeanob1,ialdeano.ialdeanob2],[],[ialdeano.ialdeanob1,ialdeano.ialdeanob2],[ialdeano.ialdeanot1,ialdeano.ialdeanot2]
                ]  

imarioperonista= Imagenes()
imarioperonista.imarioperonistab1=pygame.image.load("mundopict/marioperonistab1.png").convert_alpha()
imarioperonista.imarioperonistab2=pygame.image.load("mundopict/marioperonistab2.png").convert_alpha()
imarioperonista.imarioperonistat1=pygame.image.load("mundopict/marioperonistab1.png").convert_alpha()
imarioperonista.imarioperonistat2=pygame.image.load("mundopict/marioperonistab2.png").convert_alpha()
imarioperonista.lista=[[imarioperonista.imarioperonistab1,imarioperonista.imarioperonistab2],[],[imarioperonista.imarioperonistab1,imarioperonista.imarioperonistab2],[imarioperonista.imarioperonistat1,imarioperonista.imarioperonistat2]
                ]      

ianimacion=Imagenes()
ianimacion.ianimacionr1=pygame.image.load("mundopict/animacion1.png").convert_alpha()
ianimacion.ianimacionl1=pygame.image.load("mundopict/animacion1l.png").convert_alpha()
ianimacion.ianimacionb1=pygame.image.load("mundopict/animacion1b.png").convert_alpha()
ianimacion.ianimaciont1=pygame.image.load("mundopict/animacion1t.png").convert_alpha()    
ianimacion.ianimacionr2=pygame.image.load("mundopict/animacion2.png").convert_alpha()
ianimacion.ianimacionl2=pygame.image.load("mundopict/animacion2l.png").convert_alpha()
ianimacion.ianimacionb2=pygame.image.load("mundopict/animacion2b.png").convert_alpha()
ianimacion.ianimaciont2=pygame.image.load("mundopict/animacion2t.png").convert_alpha()   
ianimacion.lista=[[ianimacion.ianimacionr1,ianimacion.ianimacionr2],
                    [ianimacion.ianimacionl1,ianimacion.ianimacionl2],
                    [ianimacion.ianimacionb1,ianimacion.ianimacionb2],
                    [ ianimacion.ianimaciont1,ianimacion.ianimaciont2]]


iOrco=Imagenes()
iOrco.iOrcor1=pygame.image.load("mundopict/Orcor1.png").convert_alpha()
iOrco.iOrcol1=pygame.image.load("mundopict/Orcol1.png").convert_alpha()
iOrco.iOrcob1=pygame.image.load("mundopict/Orcob1.png").convert_alpha()
iOrco.iOrcot1=pygame.image.load("mundopict/Orcot1.png").convert_alpha()    
iOrco.iOrcor2=pygame.image.load("mundopict/Orcor2.png").convert_alpha()
iOrco.iOrcol2=pygame.image.load("mundopict/Orcol2.png").convert_alpha()
iOrco.iOrcob2=pygame.image.load("mundopict/Orcob2.png").convert_alpha()
iOrco.iOrcot2=pygame.image.load("mundopict/Orcot2.png").convert_alpha()   
iOrco.lista=[[iOrco.iOrcor1,iOrco.iOrcor2],
                    [iOrco.iOrcol1,iOrco.iOrcol2],
                    [iOrco.iOrcob1,iOrco.iOrcob2],
                    [ iOrco.iOrcot1,iOrco.iOrcot2]]





iskeletongreen=Imagenes()
iskeletongreen.iskeletonr1=pygame.image.load("mundopict/skeletongreenr1.png").convert_alpha()
iskeletongreen.iskeletonl1=pygame.image.load("mundopict/skeletongreenl1.png").convert_alpha()
iskeletongreen.iskeletonb1=pygame.image.load("mundopict/skeletongreenb1.png").convert_alpha()
iskeletongreen.iskeletont1=pygame.image.load("mundopict/skeletongreent1.png").convert_alpha()    
iskeletongreen.iskeletonr2=pygame.image.load("mundopict/skeletongreenr2.png").convert_alpha()
iskeletongreen.iskeletonl2=pygame.image.load("mundopict/skeletongreenl2.png").convert_alpha()
iskeletongreen.iskeletonb2=pygame.image.load("mundopict/skeletongreenb2.png").convert_alpha()
iskeletongreen.iskeletont2=pygame.image.load("mundopict/skeletongreent2.png").convert_alpha()   
iskeletongreen.lista=[[iskeletongreen.iskeletonr1,iskeletongreen.iskeletonr2],
					[iskeletongreen.iskeletonl1,iskeletongreen.iskeletonl2],
					[iskeletongreen.iskeletonb1,iskeletongreen.iskeletonb2],
					[ iskeletongreen.iskeletont1,iskeletongreen.iskeletont2]]




iskeletonred=Imagenes()
iskeletonred.iskeletonr1=pygame.image.load("mundopict/skeletonredr1.png").convert_alpha()
iskeletonred.iskeletonl1=pygame.image.load("mundopict/skeletonredl1.png").convert_alpha()
iskeletonred.iskeletonb1=pygame.image.load("mundopict/skeletonredb1.png").convert_alpha()
iskeletonred.iskeletont1=pygame.image.load("mundopict/skeletonredt1.png").convert_alpha()    
iskeletonred.iskeletonr2=pygame.image.load("mundopict/skeletonredr2.png").convert_alpha()
iskeletonred.iskeletonl2=pygame.image.load("mundopict/skeletonredl2.png").convert_alpha()
iskeletonred.iskeletonb2=pygame.image.load("mundopict/skeletonredb2.png").convert_alpha()
iskeletonred.iskeletont2=pygame.image.load("mundopict/skeletonredt2.png").convert_alpha()   
iskeletonred.lista=[[iskeletonred.iskeletonr1,iskeletonred.iskeletonr2],
                    [iskeletonred.iskeletonl1,iskeletonred.iskeletonl2],
                    [iskeletonred.iskeletonb1,iskeletonred.iskeletonb2],
                    [ iskeletonred.iskeletont1,iskeletonred.iskeletont2]]

iskeleton=Imagenes()
iskeleton.iskeletonr1=pygame.image.load("mundopict/skeletonr1.png").convert_alpha()
iskeleton.iskeletonl1=pygame.image.load("mundopict/skeletonl1.png").convert_alpha()
iskeleton.iskeletonb1=pygame.image.load("mundopict/skeletonb1.png").convert_alpha()
iskeleton.iskeletont1=pygame.image.load("mundopict/skeletont1.png").convert_alpha()    
iskeleton.iskeletonr2=pygame.image.load("mundopict/skeletonr2.png").convert_alpha()
iskeleton.iskeletonl2=pygame.image.load("mundopict/skeletonl2.png").convert_alpha()
iskeleton.iskeletonb2=pygame.image.load("mundopict/skeletonb2.png").convert_alpha()
iskeleton.iskeletont2=pygame.image.load("mundopict/skeletont2.png").convert_alpha()   
iskeleton.lista=[[iskeleton.iskeletonr1,iskeleton.iskeletonr2],
				[iskeleton.iskeletonl1,iskeleton.iskeletonl2],
				[iskeleton.iskeletonb1,iskeleton.iskeletonb2],
				[ iskeleton.iskeletont1,iskeleton.iskeletont2]]


ibarbarian=Imagenes()
ibarbarian.barbarianr1=pygame.image.load("mundopict/barbarian8.png").convert_alpha()
ibarbarian.barbarianl1=pygame.image.load("mundopict/barbarian10.png").convert_alpha()
ibarbarian.barbarianb1=pygame.image.load("mundopict/barbarian2.png").convert_alpha()
ibarbarian.barbariant1=pygame.image.load("mundopict/barbarian5.png").convert_alpha()    
ibarbarian.barbarianr2=pygame.image.load("mundopict/barbarian9.png").convert_alpha()
ibarbarian.barbarianl2=pygame.image.load("mundopict/barbarian11.png").convert_alpha()
ibarbarian.barbarianb2=pygame.image.load("mundopict/barbarian3.png").convert_alpha()
ibarbarian.barbariant2=pygame.image.load("mundopict/barbarian6.png").convert_alpha()   
ibarbarian.lista=[[ibarbarian.barbarianr1,ibarbarian.barbarianr2],
                [ibarbarian.barbarianl1,ibarbarian.barbarianl2],
                [ibarbarian.barbarianb1,ibarbarian.barbarianb2],
                [ ibarbarian.barbariant1,ibarbarian.barbariant2]]

iespada=pygame.image.load("mundopict/espada.png").convert_alpha()
iespadal=pygame.image.load("mundopict/espadal.png").convert_alpha()
iespadat=pygame.image.load("mundopict/espadat.png").convert_alpha()
iespadab=pygame.image.load("mundopict/espadab.png").convert_alpha()

iespada2=pygame.image.load("mundopict/espada2.png").convert_alpha()
iespadal2=pygame.image.load("mundopict/espadal2.png").convert_alpha()
iespadat2=pygame.image.load("mundopict/espadat2.png").convert_alpha()
iespadab2=pygame.image.load("mundopict/espadab2.png").convert_alpha()


iespadaacrono=pygame.image.load("mundopict/espadaacrono.png").convert_alpha()
iespadaacronol=pygame.image.load("mundopict/espadaacronol.png").convert_alpha()
iespadaacronot=pygame.image.load("mundopict/espadaacronot.png").convert_alpha()
iespadaacronob=pygame.image.load("mundopict/espadaacronob.png").convert_alpha()

iespadaacrono2=pygame.image.load("mundopict/espadaacrono2.png").convert_alpha()
iespadaacronol2=pygame.image.load("mundopict/espadaacronol2.png").convert_alpha()
iespadaacronot2=pygame.image.load("mundopict/espadaacronot2.png").convert_alpha()
iespadaacronob2=pygame.image.load("mundopict/espadaacronob2.png").convert_alpha()

icastingr=pygame.image.load("mundopict/castingr.png").convert_alpha()
icastingl=pygame.image.load("mundopict/castingl.png").convert_alpha()
icastingb=pygame.image.load("mundopict/castingb.png").convert_alpha()
icastingt=pygame.image.load("mundopict/castingt.png").convert_alpha()


icastingacronor=pygame.image.load("mundopict/castingacronor.png").convert_alpha()
icastingacronol=pygame.image.load("mundopict/castingacronol.png").convert_alpha()
icastingacronob=pygame.image.load("mundopict/castingacronob.png").convert_alpha()
icastingacronot=pygame.image.load("mundopict/castingacronot.png").convert_alpha()

idisparor=pygame.image.load("mundopict/disparor.png").convert_alpha()
idisparol=pygame.image.load("mundopict/disparol.png").convert_alpha()
idisparot=pygame.image.load("mundopict/disparot.png").convert_alpha()
idisparob=pygame.image.load("mundopict/disparob.png").convert_alpha()
idisparor2=pygame.image.load("mundopict/disparor2.png").convert_alpha()
idisparol2=pygame.image.load("mundopict/disparol2.png").convert_alpha()
idisparot2=pygame.image.load("mundopict/disparot2.png").convert_alpha()
idisparob2=pygame.image.load("mundopict/disparob2.png").convert_alpha()

ipozo=pygame.image.load("mundopict/portall.png").convert_alpha()
ishop=pygame.image.load("mundopict/shop1.png").convert_alpha()
ishop2=pygame.image.load("mundopict/shop2.png").convert_alpha()
ishop3=pygame.image.load("mundopict/shop3.png").convert_alpha()
ishop4=pygame.image.load("mundopict/shop4.png").convert_alpha() 
ishop5=pygame.image.load("mundopict/shop5.png").convert_alpha() 
ishop6=pygame.image.load("mundopict/shop6.png").convert_alpha() 
igameover=pygame.image.load("mundopict/gameover.png").convert_alpha()                                                                      
