import pygame
pygame.init()
game_active=True 
screen1=pygame.display.set_mode((600,600))
thingy=pygame.image.load('graphics/wojack.png').convert()
hehehe=pygame.image.load('graphics/momskindahomeless.jpeg').convert()
li=[thingy,hehehe]
while game_active:
    for event in pygame.event.get():
        x=0
        if event.type==pygame.QUIT:
           game_active=False
        elif event.type==pygame.MOUSEMOTION:
            if event.rel[0]>0:
                print("mouse is moving right")
            elif event.rel[1]>0:
                print("mouse is moving down")
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                print("clicky")
                screen1.blit(li[x],(0,0))
                x+=1
                if x>1:
                    x=0


    
    pygame.display.update()
    pygame.time.Clock().tick(60)
