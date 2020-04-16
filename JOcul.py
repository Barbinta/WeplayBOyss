import pygame

movex = 0
movey = 0
px = 480
py = 200

screen = pygame.display.set_mode((800, 600))

pimg = pygame.image.load ('eat.png')

def player(x, y):
    screen.blit(pimg, ( x, y ))

pygame.display.set_caption('BarBy')
icon = pygame.image.load('pizza.png')
pygame.display.set_icon(icon)


running = True
while running:
    screen.fill((102, 153, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                movex -= 0.3
            if event.key == K_RIGHT:
                movex =+ 0.3
            if event.key == K_UP:
                movey -= 0.3
            if event.key == K_DOWN:
                movey += 0.3
        if event.type == pygame.KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                movex = 0
            if event.key == K_UP or event.key == K_DOWN:
                movey = 0   
         
    px += movex
    py += movey   

    if px <= 0:
        px = 0 
    elif px >= 736:
        px = 736      
    if py <= 0:
        py = 0 
    elif py >= 536:
        py = 536        

    player(px, py)  
    pygame.display.update()     