import pygame

pygame.init()

screen1=pygame.display.set_mode((1200,1000))
title=pygame.image.load("componentschar/titlecopy.png")
title=pygame.transform.scale(title,(600,200))
bu1=pygame.image.load("componentschar/play.jpeg").convert_alpha()
bu2=pygame.image.load("componentschar/quit.jpeg").convert_alpha()

replace1=pygame.image.load("componentschar/petergriffin.png").convert()


bu1=pygame.transform.scale(bu1,(450,200))
bu2=pygame.transform.scale(bu2,(450,200))

pygame.mixer.music.load("music/elevator.mp3")
pygame.mixer.music.play(loops=-1)

hitsound=pygame.mixer.Sound("soundeff/vine.mp3")


class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)
    def swap(self,new_image):
        self.image=new_image

s1=button(bu1,(600,350))
s2=button(bu2,(600,550))
slis=pygame.sprite.Group()

slis.add(s1)
slis.add(s2)
colour=(255,255,255)



mice = (0,0)

gameactive = True
while gameactive:
    mice = (0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameactive = False
        elif event.type== pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                mice = event.pos 
                
    
    print(mice)
    if s1.rect.collidepoint(mice):
        hitsound.play()
        s1.swap(replace1)
        slis.draw(screen1)

        
    elif s2.rect.collidepoint(mice):
        gameactive=False
        
        
    screen1.fill(colour)
    screen1.blit(title,(350,100))
    slis.draw(screen1)
    pygame.display.update()
    pygame.time.Clock().tick(60)