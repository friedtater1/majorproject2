import pygame
pygame.init()

screen1=pygame.display.set_mode((1200,1200))
backing=pygame.image.load("components/backdrop.jpeg").convert()
title=pygame.image.load("components/titlecopy.png").convert()
title=pygame.transform.scale(title,(200,200))
backing=pygame.transform.scale(backing,(1000,1000))

class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)



gameactive = True
while gameactive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                gameactive = False
        elif event.type== pygame.MOUSEBUTTONDOWN:
             if event.button==1:
                  print("its working")
             elif event.button==2:
                gameactive = False
                  
    screen1.blit(title,(200,200))
    screen1.blit(backing,(0,0))
    pygame.display.update()
    pygame.time.Clock().tick(60)