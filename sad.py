import pygame
import math
from pygame.locals import*

height = 800
width = 600

x = 0
y = 0

C = True

player_1_x = 128 
player_1_y = 276

screen = pygame.display.set_mode(( height, width ))

player_1_image = pygame.image.load( 'pizza.png' )
def player_1 ( x, y ):
    screen.blit( player_1_image, ( x, y )) 

def coll(plx, ply, mnx, mny):
    distance = math.sqrt(( math.pow( plx - mnx, 2 ) ) + math.pow( ply - mny, 2 ) )
    if distance < 36:
        return True

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y  = pygame.mouse.get_pos()
            C= False
            
    if C:
        screen.fill((0,255,0))
    
    pygame.display.update()           

