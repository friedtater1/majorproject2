import pygame

pygame.init()


class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)

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


menu1=pygame.image.load("componentschar/actionmen.png").convert_alpha()
menu2=pygame.image.load("componentschar/healthtrack.png").convert_alpha()
menu3e=pygame.image.load("componentschar/actionmen.png").convert_alpha()

menu1=pygame.transform.scale(menu1,(400,300))
menu3e=pygame.transform.scale(menu3e,(400,300))
menu2=pygame.transform.scale(menu2,(800,300))

zombie1=pygame.image.load("componentschar/zombie.png").convert_alpha()
hitsound=pygame.mixer.Sound("soundeff/sword.mp3")

man=pygame.image.load("componentschar/char_left.png").convert()


pygame.mixer.music.load("music/dummy.mp3")
pygame.mixer.music.play(loops=-1)


pg=pygame.sprite.Group()
enemy=pygame.sprite.Group()
dude=player(man,(800,350))
erm=enemys(zombie1,(250,350))

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
    screen1.blit(menu1,(50,700))
    screen1.blit(menu2,(800,700))
    screen1.blit(menu3e,(450,700))
    pygame.display.update()
    pygame.time.Clock().tick(60)

