import pygame
pygame.init()


screen1=pygame.display.set_mode((1200,900))
store=pygame.image.load("componentstore/snowdin.png").convert()
store=pygame.transform.scale(store,(1550,950))
guyl=pygame.image.load("componentschar/char_left.png").convert()
guyr=pygame.image.load("componentschar/char_right.png").convert()
guyu=pygame.image.load("componentschar/char_behind.png").convert()
guyd=pygame.image.load("componentschar/char_front.png").convert()
surprise=pygame.image.load("componentschar/petergriffin.png").convert()
surprise=pygame.transform.scale(surprise,(250,250))
papy=pygame.image.load("componentschar/papyrus.png").convert()
papy=pygame.transform.scale(papy,(250,250))
pog=pygame.image.load("componentschar/horse.jpeg").convert()
chest=pygame.image.load("componentschar/chest.png").convert()


invis=pygame.image.load("componentstore/coconut.jpeg").convert()
backdrop1=pygame.image.load("componentstore/storescreenback.png").convert()
confirm=pygame.image.load("componentstore/confirm.png").convert()




pygame.mixer.music.load("music/snowy.mp3")
pygame.mixer.music.play(loops=-1)
confirms=pygame.mixer.Sound("soundeff/creeper.mp3")


class merchant(pygame.sprite.Sprite):
     def __init__(self,image,spawn):
          super().__init__()
          self.image=image
          self.spawn=spawn
          self.rect=self.image.get_rect(center=spawn)

class player(pygame.sprite.Sprite):
     def __init__(self,image,spot):
          super().__init__()
          self.image=image
          self.spot=spot
          self.rect=self.image.get_rect(center=spot)
     def swap(self,new_image):
          self.image=new_image

class inventory(pygame.sprite.Sprite):
    def __init__(self,image,spot,weapon=None,consumable=None):
          super().__init__()
          self.image=image
          self.spot=spot
          self.rect=self.image.get_rect(center=spot)
          self.weapon=weapon
          self.consumable=consumable
    def retrievew(self):
        with open("cache/storageweapons.txt","r") as f:
            self.weapon=(f.read())
            self.weapon=self.weapon.split(",")

class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)
    def swap(self,new_image):
        self.image=new_image

class hitbox(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)
    def setting(self,base):
        self.image=pygame.transform.scale(self.image,(((base.rect.x)*1.5),((base.rect.y)*1.5)))
        self.rect.center=base.rect.center
    




velocity=0
vx=0


character=pygame.sprite.Group()
dude1=player(guyd,(0,600))

character.add(dude1)
merchant1=merchant(papy,(250,250))
merchantreact=merchant(surprise,(250,250))
stores=pygame.sprite.Group()
stores.add(merchant1)

chester=inventory(chest,(600,450))
invent=pygame.sprite.Group()
invent.add(chester)

display=pygame.sprite.Group()
backing=button(backdrop1,(600,450))
confir=button(confirm,(1000,250))
display.add(backing)
display.add(confir)

boxmer=hitbox(invis,(200,200))
boxmer.setting(merchant1)
interact=pygame.sprite.Group()
interact.add(boxmer)



mice = (0,0)

gameactive=True

while gameactive:
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                gameactive = False
         elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_s:
                velocity+=5
            elif event.key== pygame.K_w:
                velocity-=5
            elif event.key== pygame.K_a:
                vx-=5
            elif event.key==pygame.K_d:
                vx+=5
            elif event.key== pygame.K_e:
                if dude1.rect.move(vx,velocity).colliderect(boxmer.rect):
                    display.draw(screen1)
                    if confir.rect.collidepoint(mice):
                        if event.type== pygame.MOUSEBUTTONDOWN:
                            if event.button==1:
                                confirms.play()
                                display.empty()
        
            elif event.key== pygame.K_TAB:
                display.draw(screen1)
         elif event.type==pygame.KEYUP:
            if event.key== pygame.K_s:
                velocity=0
            elif event.key== pygame.K_w:
                velocity=0
            elif event.key== pygame.K_a:
                vx=0
            elif event.key==pygame.K_d:
                vx=0
                
    if dude1.rect.move(vx,velocity).collidelist([x.rect for x in stores.sprites()]) != -1:
        stores.add(merchantreact)
        stores.draw(screen1)
        merchant1.kill()
        if vx>0 or vx<0:
            vx=0
        elif velocity>0 or velocity<0:
            velocity=0
    if vx>0:
        dude1.swap(guyr)
    elif vx<0:
        dude1.swap(guyl)
    elif velocity>0:
        dude1.swap(guyd)
    elif velocity<0:
        dude1.swap(guyu)
    
    

    screen1.blit(store,(0,0))
    
    character.draw(screen1)
    if vx > 0 or vx< 0:
        dude1.rect.move_ip(vx,0)
    elif velocity<0 or velocity>0:
        dude1.rect.move_ip(0,velocity)

    
    stores.draw(screen1)
    interact.draw(screen1)
    interact.update()
    
    pygame.display.update()
    pygame.time.Clock().tick(60)