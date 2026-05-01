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
papy=pygame.image.load("componentschar/papyrus.png").convert()
papy=pygame.transform.scale(papy,(250,250))

pygame.mixer.music.load("music/snowy.mp3")
pygame.mixer.music.play(loops=-1)


class collidable(pygame.sprite.Sprite):
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

velocity=0
vx=0


character=pygame.sprite.Group()
dude1=player(guyd,(0,600))
character.add(dude1)
merchant1=collidable(papy,(250,250))
stores=pygame.sprite.Group()
stores.add(merchant1)

gameactive=True

while gameactive:
    
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
                gameactive = False
         elif event.type==pygame.MOUSEBUTTONDOWN:
             if event.button==1:
                 gameactive=False
         elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_w:
                print("up")
                velocity+=5
            elif event.key== pygame.K_s:
                print("down")
                velocity-=5
            elif event.key== pygame.K_a:
                print("left")
                vx-=5
            elif event.key==pygame.K_d:
                print("right")
                vx+=5
         elif event.type==pygame.KEYUP:
            if event.key== pygame.K_w:
                print("up")
                velocity-=5
            elif event.key== pygame.K_s:
                print("down")
                velocity+=5
            elif event.key== pygame.K_a:
                print("left")
                vx+=5
            elif event.key==pygame.K_d:
                print("right")
                vx-=5


    screen1.blit(store,(0,0))

    
    character.draw(screen1)
    if vx > 0 or vx< 0:
        dude1.rect.move_ip(vx,0)
    elif velocity<0 or velocity>0:
        dude1.rect.move_ip(0,velocity)

    stores.draw(screen1)
    pygame.display.update()
    pygame.time.Clock().tick(60)