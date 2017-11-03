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



imagen1=pygame.image.load("mundopict/barmithr1.png").convert_alpha()
imagen2=pygame.image.load("mundopict/barmithr2.png").convert_alpha()
imagen1l=pygame.image.load("mundopict/barmithl1.png").convert_alpha()
imagen2l=pygame.image.load("mundopict/barmithl2.png").convert_alpha()    
imagen1t=pygame.image.load("mundopict/barmitht1.png").convert_alpha()
imagen2t=pygame.image.load("mundopict/barmitht2.png").convert_alpha()
imagen1b=pygame.image.load("mundopict/barmithb1.png").convert_alpha()
imagen2b=pygame.image.load("mundopict/barmithb2.png").convert_alpha()

imegaman= Imagenes()
imegaman.imegamanr1=pygame.image.load("mundopict/megamanr1.png").convert_alpha()
imegaman.imegamanr2=pygame.image.load("mundopict/megamanr2.png").convert_alpha()
imegaman.imegamanl1=pygame.image.load("mundopict/megamanl1.png").convert_alpha()
imegaman.imegamanl2=pygame.image.load("mundopict/megamanl2.png").convert_alpha()
imegaman.lista=[[imegaman.imegamanr1,imegaman.imegamanr2],[imegaman.imegamanl1,imegaman.imegamanl2],
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





isonic=Imagenes()
isonic.iskeletonr1=pygame.image.load("mundopict/sonicr1.png").convert_alpha()
isonic.iskeletonl1=pygame.image.load("mundopict/sonicl1.png").convert_alpha()
isonic.iskeletonb1=pygame.image.load("mundopict/sonicb1.png").convert_alpha()
isonic.iskeletont1=pygame.image.load("mundopict/sonict1.png").convert_alpha()    
isonic.iskeletonr2=pygame.image.load("mundopict/sonicr2.png").convert_alpha()
isonic.iskeletonl2=pygame.image.load("mundopict/sonicl2.png").convert_alpha()
isonic.iskeletonb2=pygame.image.load("mundopict/sonicb2.png").convert_alpha()
isonic.iskeletont2=pygame.image.load("mundopict/sonict2.png").convert_alpha()   
isonic.lista=[[isonic.iskeletonr1,isonic.iskeletonr2],
					[isonic.iskeletonl1,isonic.iskeletonl2],
					[isonic.iskeletonb1,isonic.iskeletonb2],
					[ isonic.iskeletont1,isonic.iskeletont2]]




ipikachuyellow=Imagenes()
ipikachuyellow.iskeletonr1=pygame.image.load("mundopict/pikachuyellowr1.png").convert_alpha()
ipikachuyellow.iskeletonl1=pygame.image.load("mundopict/pikachuyellowl1.png").convert_alpha()
ipikachuyellow.iskeletonb1=pygame.image.load("mundopict/pikachuyellowb1.png").convert_alpha()
ipikachuyellow.iskeletont1=pygame.image.load("mundopict/pikachuyellowt1.png").convert_alpha()    
ipikachuyellow.iskeletonr2=pygame.image.load("mundopict/pikachuyellowr2.png").convert_alpha()
ipikachuyellow.iskeletonl2=pygame.image.load("mundopict/pikachuyellowl2.png").convert_alpha()
ipikachuyellow.iskeletonb2=pygame.image.load("mundopict/pikachuyellowb2.png").convert_alpha()
ipikachuyellow.iskeletont2=pygame.image.load("mundopict/pikachuyellowt2.png").convert_alpha()   
ipikachuyellow.lista=[[ipikachuyellow.iskeletonr1,ipikachuyellow.iskeletonr2],
                    [ipikachuyellow.iskeletonl1,ipikachuyellow.iskeletonl2],
                    [ipikachuyellow.iskeletonb1,ipikachuyellow.iskeletonb2],
                    [ ipikachuyellow.iskeletont1,ipikachuyellow.iskeletont2]]

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


ilink=Imagenes()
ilink.linkr1=pygame.image.load("mundopict/link8.png").convert_alpha()
ilink.linkl1=pygame.image.load("mundopict/link10.png").convert_alpha()
ilink.linkb1=pygame.image.load("mundopict/link2.png").convert_alpha()
ilink.linkt1=pygame.image.load("mundopict/link5.png").convert_alpha()    
ilink.linkr2=pygame.image.load("mundopict/link9.png").convert_alpha()
ilink.linkl2=pygame.image.load("mundopict/link11.png").convert_alpha()
ilink.linkb2=pygame.image.load("mundopict/link3.png").convert_alpha()
ilink.linkt2=pygame.image.load("mundopict/link6.png").convert_alpha()   
ilink.lista=[[ilink.linkr1,ilink.linkr2],
                [ilink.linkl1,ilink.linkl2],
                [ilink.linkb1,ilink.linkb2],
                [ ilink.linkt1,ilink.linkt2]]

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
