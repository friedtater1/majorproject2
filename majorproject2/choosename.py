import pygame

pygame.init()



class button(pygame.sprite.Sprite):
    def __init__(self,image,spawn):
        super().__init__()
        self.image=image
        self.spawn=spawn
        self.rect=self.image.get_rect(center=spawn)

namestore=0
color=(255,255,255)


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
    screen1.blit(question,(350,100))
    slis.draw(screen1)
    pygame.display.update()
    pygame.time.Clock().tick(60)