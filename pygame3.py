import pygame
pygame.init()
game_active=True 
screen1=pygame.display.set_mode((1000,1000))
thingy=pygame.image.load('graphics/wojack.png').convert()
hehehe=pygame.image.load('graphics/pointing.jpeg').convert()
back=pygame.image.load("graphics/sky.jpeg").convert()
hehehe=pygame.transform.scale(hehehe,(50,50))



class char(pygame.sprite.Sprite):
    def __init__(self,name,image,location,x_velocity):
        super().__init__()
        self.name=name
        self.image=image
        self.rect=image.get_rect(center=location)
        self.x_velocity=x_velocity

    def update(self):
        print(self.x_velocity)
        self.rect.move_ip(self.x_velocity,0)
        if self.rect.right>0:
            self.x_velocity-=1
        elif self.rect.left<0:
            self.x_velocity+=1
        elif (self.rect.right>800 or self.rect.left<0):
            self.x_velocity*=-1

e1=char("ye",thingy,(90,100),1)
e2=char("yip",hehehe,(900,360),-1)

gr=pygame.sprite.Group()
gr.add(e1)
gr.add(e2)


while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False       
        
                


    screen1.blit(back,(0,0))
    gr.draw(screen1)
    gr.update()
   
    pygame.display.update()
    pygame.time.Clock().tick(60)