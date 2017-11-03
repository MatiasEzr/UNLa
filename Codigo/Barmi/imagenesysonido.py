import pygame
class Imagenes(object):
    def __init__(self):
        self.nombre="Barmi"
pygame.init()
pygame.display.set_mode((0,0))

attack=pygame.mixer.Sound("mundopict/atack.wav")
attack.set_volume(0.4)
hited=pygame.mixer.Sound("mundopict/hited.wav")
levelup=pygame.mixer.Sound("mundopict/heavymachinegun.wav")
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



ideadpool= Imagenes()
ideadpool.ideadpoolr1=pygame.image.load("mundopict/deadpoolr1.png").convert_alpha()
ideadpool.ideadpoolr2=pygame.image.load("mundopict/deadpoolr2.png").convert_alpha()
ideadpool.ideadpooll1=pygame.image.load("mundopict/deadpooll1.png").convert_alpha()
ideadpool.ideadpooll2=pygame.image.load("mundopict/deadpooll2.png").convert_alpha()
ideadpool.lista=[[ideadpool.ideadpoolr1,ideadpool.ideadpoolr2],[ideadpool.ideadpooll1,ideadpool.ideadpooll2],
                [],[]]   


izombie= Imagenes()
izombie.izombieb1=pygame.image.load("mundopict/zombieb1.png").convert_alpha()
izombie.izombieb2=pygame.image.load("mundopict/zombieb2.png").convert_alpha()
izombie.izombiet1=pygame.image.load("mundopict/zombiet1.png").convert_alpha()
izombie.izombiet2=pygame.image.load("mundopict/zombiet2.png").convert_alpha()
izombie.lista=[[izombie.izombieb1,izombie.izombieb2],[],[izombie.izombieb1,izombie.izombieb2],[izombie.izombiet1,izombie.izombiet2]
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


icaballeronegro=Imagenes()
icaballeronegro.icaballeronegror1=pygame.image.load("mundopict/caballeronegror1.png").convert_alpha()
icaballeronegro.icaballeronegrol1=pygame.image.load("mundopict/caballeronegrol1.png").convert_alpha()
icaballeronegro.icaballeronegrob1=pygame.image.load("mundopict/caballeronegrob1.png").convert_alpha()
icaballeronegro.icaballeronegrot1=pygame.image.load("mundopict/caballeronegrot1.png").convert_alpha()    
icaballeronegro.icaballeronegror2=pygame.image.load("mundopict/caballeronegror2.png").convert_alpha()
icaballeronegro.icaballeronegrol2=pygame.image.load("mundopict/caballeronegrol2.png").convert_alpha()
icaballeronegro.icaballeronegrob2=pygame.image.load("mundopict/caballeronegrob2.png").convert_alpha()
icaballeronegro.icaballeronegrot2=pygame.image.load("mundopict/caballeronegrot2.png").convert_alpha()   
icaballeronegro.lista=[[icaballeronegro.icaballeronegror1,icaballeronegro.icaballeronegror2],
                    [icaballeronegro.icaballeronegrol1,icaballeronegro.icaballeronegrol2],
                    [icaballeronegro.icaballeronegrob1,icaballeronegro.icaballeronegrob2],
                    [ icaballeronegro.icaballeronegrot1,icaballeronegro.icaballeronegrot2]]





isonic=Imagenes()
isonic.igokur1=pygame.image.load("mundopict/sonicr1.png").convert_alpha()
isonic.igokul1=pygame.image.load("mundopict/sonicl1.png").convert_alpha()
isonic.igokub1=pygame.image.load("mundopict/sonicb1.png").convert_alpha()
isonic.igokut1=pygame.image.load("mundopict/sonict1.png").convert_alpha()    
isonic.igokur2=pygame.image.load("mundopict/sonicr2.png").convert_alpha()
isonic.igokul2=pygame.image.load("mundopict/sonicl2.png").convert_alpha()
isonic.igokub2=pygame.image.load("mundopict/sonicb2.png").convert_alpha()
isonic.igokut2=pygame.image.load("mundopict/sonict2.png").convert_alpha()   
isonic.lista=[[isonic.igokur1,isonic.igokur2],
					[isonic.igokul1,isonic.igokul2],
					[isonic.igokub1,isonic.igokub2],
					[ isonic.igokut1,isonic.igokut2]]




ipikachuyellow=Imagenes()
ipikachuyellow.igokur1=pygame.image.load("mundopict/pikachuyellowr1.png").convert_alpha()
ipikachuyellow.igokul1=pygame.image.load("mundopict/pikachuyellowl1.png").convert_alpha()
ipikachuyellow.igokub1=pygame.image.load("mundopict/pikachuyellowb1.png").convert_alpha()
ipikachuyellow.igokut1=pygame.image.load("mundopict/pikachuyellowt1.png").convert_alpha()    
ipikachuyellow.igokur2=pygame.image.load("mundopict/pikachuyellowr2.png").convert_alpha()
ipikachuyellow.igokul2=pygame.image.load("mundopict/pikachuyellowl2.png").convert_alpha()
ipikachuyellow.igokub2=pygame.image.load("mundopict/pikachuyellowb2.png").convert_alpha()
ipikachuyellow.igokut2=pygame.image.load("mundopict/pikachuyellowt2.png").convert_alpha()   
ipikachuyellow.lista=[[ipikachuyellow.igokur1,ipikachuyellow.igokur2],
                    [ipikachuyellow.igokul1,ipikachuyellow.igokul2],
                    [ipikachuyellow.igokub1,ipikachuyellow.igokub2],
                    [ ipikachuyellow.igokut1,ipikachuyellow.igokut2]]

igoku=Imagenes()
igoku.igokur1=pygame.image.load("mundopict/gokur1.png").convert_alpha()
igoku.igokul1=pygame.image.load("mundopict/gokul1.png").convert_alpha()
igoku.igokub1=pygame.image.load("mundopict/gokub1.png").convert_alpha()
igoku.igokut1=pygame.image.load("mundopict/gokut1.png").convert_alpha()    
igoku.igokur2=pygame.image.load("mundopict/gokur2.png").convert_alpha()
igoku.igokul2=pygame.image.load("mundopict/gokul2.png").convert_alpha()
igoku.igokub2=pygame.image.load("mundopict/gokub2.png").convert_alpha()
igoku.igokut2=pygame.image.load("mundopict/gokut2.png").convert_alpha()   
igoku.lista=[[igoku.igokur1,igoku.igokur2],
				[igoku.igokul1,igoku.igokul2],
				[igoku.igokub1,igoku.igokub2],
				[ igoku.igokut1,igoku.igokut2]]


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

idisparandor=pygame.image.load("mundopict/disparandor.png").convert_alpha()
idisparandol=pygame.image.load("mundopict/disparandol.png").convert_alpha()
idisparandob=pygame.image.load("mundopict/disparandob.png").convert_alpha()
idisparandot=pygame.image.load("mundopict/disparandot.png").convert_alpha()


idisparandoacronor=pygame.image.load("mundopict/disparandoacronor.png").convert_alpha()
idisparandoacronol=pygame.image.load("mundopict/disparandoacronol.png").convert_alpha()
idisparandoacronob=pygame.image.load("mundopict/disparandoacronob.png").convert_alpha()
idisparandoacronot=pygame.image.load("mundopict/disparandoacronot.png").convert_alpha()

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
