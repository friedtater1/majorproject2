import pygame
pygame.init()
game_active=True
screen1=pygame.display.set_mode((800,1000))
sky_surface=pygame.image.load('graphics/zep61g96ak1g1.png').convert()

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
    screen1.blit(sky_surface,(0,0))
    pygame.display.update()
    pygame.time.Clock().tick(60)