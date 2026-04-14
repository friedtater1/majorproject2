import pygame
pygame.init()
game_active=True 
screen1=pygame.display.set_mode((1000,1000))
thingy=pygame.image.load('graphics/chara.jpeg').convert()
back=pygame.image.load("graphics/sky.jpeg").convert()
trap=pygame.image.load("graphics/map.jpeg").convert()
thingy_rect=thingy.get_rect(center=(400,400))
trap_rect=trap.get_rect(center=(200,200))
velocity=0
vx=0
while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
        elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_w:
                print("up")
                velocity+=10
            elif event.key== pygame.K_s:
                print("down")
                velocity-=10
            elif event.key== pygame.K_a:
                print("left")
                vx-=10
            elif event.key==pygame.K_d:
                print("right")
                vx+=10
        elif event.type==pygame.KEYUP:
            if event.key== pygame.K_w:
                print("up")
                velocity-=10
            elif event.key== pygame.K_s:
                print("down")
                velocity+=10
            elif event.key== pygame.K_a:
                print("left")
                vx+=10
            elif event.key==pygame.K_d:
                print("right")
                vx-=10
            
        elif thingy_rect.colliderect(trap_rect):
            print("STOP TOUCHING ME")

    screen1.blit(back,(0,0))
    screen1.blit(trap,(0,300))
    screen1.blit(thingy,thingy_rect)
    thingy_rect.move_ip(vx,velocity)
    pygame.display.update()
    pygame.time.Clock().tick(60)
