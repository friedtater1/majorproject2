import pygame

pygame.init()


class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)
    def swap(self,new_image):
        self.image=new_image
    def scale(self,base):
        self.image=pygame.transform.scale(self.image,(((base.rect.x)*1.5),((base.rect.y)*1.5)))

class enemys(pygame.sprite.Sprite):
     def __init__(self,image,spot):
        super().__init__()
        self.image=image
        self.spot=spot
        self.rect=self.image.get_rect(center=spot)


class player(pygame.sprite.Sprite):
     def __init__(self,image,spot):
          super().__init__()
          self.image=image
          self.spot=spot
          self.rect=self.image.get_rect(center=spot)

        
                       



screen1=pygame.display.set_mode((1200,1000))
backing=pygame.image.load("componentschar/grass.jpeg").convert()
backing=pygame.transform.scale(backing,(1200,1000))





zombie1=pygame.image.load("componentschar/zombie.png").convert_alpha()
hitsound=pygame.mixer.Sound("soundeff/sword.mp3")

man=pygame.image.load("componentschar/char_left.png").convert()
actionmenu=pygame.image.load("componentscomb/actionmenu.png").convert()
healthtrack=pygame.image.load("componentscomb/healthtrackmenu.png").convert()

pygame.mixer.music.load("music/dummy.mp3")
pygame.mixer.music.play(loops=-1)


pg=pygame.sprite.Group()
enemy=pygame.sprite.Group()
dude=player(man,(800,350))
erm=enemys(zombie1,(250,350))

menu=pygame.sprite.Group()
actionm=button(actionmenu,(300,500))
healthm=button(healthtrack,(600,500))
menu.add(actionm)
menu.add(healthm)

enemy.add(erm)
pg.add(dude)



gameactive = True
while gameactive:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameactive = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                hitsound.play()
            elif event.button==3:
                gameactive = False


    screen1.blit(backing,(0,0))
    pg.draw(screen1)
    enemy.draw(screen1)
    menu.draw(screen1)
    
    pygame.display.update()
    pygame.time.Clock().tick(60)

