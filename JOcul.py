import random
import pygame
import math
from pygame.locals import *

A = 2
B = False
C = True

movepx = 0
movepy = 0

movebx = 0.2
moveby = 0.2

movegy = 0.5

damage_player = 0

px = 368
py = 400

gx = px
gy = py

mx = random.randint(32, 768) 
my = random.randint(32, 568)

bx = 400
by = 100

g2x = bx
g2y = by

damage = 0

screen = pygame.display.set_mode((800, 600))

bimg = pygame.image.load ( 'fat.png' )
pimg = pygame.image.load ( 'eat.png' )
ming = pygame.image.load ( 'cookie.png' )

def coll(plx, ply, mnx, mny):
    distance = math.sqrt(( math.pow( plx - mnx, 2 ) ) + math.pow( ply - mny, 2 ) )
    if distance < 36:
        return True
        
def boss(x, y):
    screen.blit(bimg, ( x, y ))

def player(x, y):
    screen.blit(pimg, ( x, y ))

def manc(x, y):
    screen.blit(ming, ( x, y ))

def shoot(x, y):
    global B 
    B = True
    screen.blit(ming, ( x+16, y ))

def shot( x, y ):
    screen.blit(ming, ( x, y ))

pygame.display.set_caption('BarBy')
icon = pygame.image.load('pizza.png')
pygame.display.set_icon(icon)
background = pygame.image.load('victory.png')
background1 = pygame.image.load('defeat.jpg')

running = True
while running:
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if A == 0 and B == False:
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    gx = px
                    gy = py
                    shoot( gx, gy )

        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                movepx -= 0.35
            if event.key == K_d:
                movepx =+ 0.35
            if event.key == K_w:
                movepy -= 0.35
            if event.key == K_s:
                movepy += 0.35
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_d:
                movepx = 0
            if event.key == K_w or event.key == K_s:
                movepy = 0
        
            
            
    px += movepx
    py += movepy 

    if A == 0:
        screen.fill((255, 255, 0))
        
        
        if B == True and damage != 5 :
            shoot( gx, gy )
            gy -= movegy
            if coll(gx, gy, bx, by):
                B = False
                gy = py
                damage += 1

            
            if gy <= 0:
                B = False
                gy = py
        
        if C :
            C = False
            px = 368
            py = 400     

        bx += movebx
        by += moveby

        
        shot( g2x, g2y )
        g2y += movegy
        if coll(g2x, g2y, px, py):
            g2x = bx
            g2y = by
            damage_player += 1
            
        if g2x <= 0:
            g2x = bx
            g2y = by 
        if px >= 736:
            g2x = bx
            g2y = by     
        if g2y <= 0:
            g2x = bx
            g2y = by 
        if g2y >= 536:
            g2x = bx
            g2y = by  
        
        boss( bx, by )
        player(px, py)
        #pygame.draw.rect(screen, (0, 0, 0),( bx + 10, by + 60, 55 , 15 ))
        pygame.draw.rect(screen, (255, 0, 0),( bx + 6 , by + 63, 53 - (10 * damage) , 10) )
        pygame.draw.rect(screen, (255, 0, 0),( px + 6 , py + 63, 53 - (25 * damage_player) , 10) )

        if bx <= 0 or bx >= 764:
            movebx *= -1
        if by <= 0 or by >= 168:
            moveby *= -1

        

    if px <= 0:
        px = 0 
    elif px >= 736:
        px = 736      
    if py <= 0:
        py = 0 
    elif py >= 536:
        py = 536        


    if A != 0:
        screen.fill((102, 153, 0))
        manc(mx, my)
        if coll(px, py, mx, my):
            mx = random.randint(32, 768) 
            my = random.randint(32, 568)
            A -= 1   
        player(px, py)


    
    if damage == 6:
        screen.blit(background,( 0, 0 ) )
         
    if damage_player == 2:
        screen.blit(background1,( 0, 0 ) )
    pygame.display.update()
       