import pygame


pygame.init()

screen1=pygame.display.set_mode((1200,1000))
title=pygame.image.load("components/titlecopy.png")
title=pygame.transform.scale(title,(600,200))
bu1=pygame.image.load("components/play.jpeg").convert_alpha()
bu2=pygame.image.load("components/quit.jpeg").convert_alpha()
bu1=pygame.transform.scale(bu1,(450,200))
bu2=pygame.transform.scale(bu2,(450,200))

pygame.mixer.music.load("music/elevator.mp3")
pygame.mixer.music.play(loops=-1)

hitsound=pygame.mixer.Sound("music/vine.mp3")


class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)

s1=button(bu1,(600,350))
s2=button(bu2,(600,550))
slis=pygame.sprite.Group()

slis.add(s1)
slis.add(s2)
colour=(255,255,255)

gameactive = True
while gameactive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameactive = False
        elif event.type== pygame.MOUSEBUTTONDOWN:
             if event.button==1:
                  print("insert vinebooms here")
             elif event.button==3:
                gameactive= False
    
    
    screen1.fill(colour)
    screen1.blit(title,(350,100))
    slis.draw(screen1)
    pygame.display.update()
    pygame.time.Clock().tick(60)