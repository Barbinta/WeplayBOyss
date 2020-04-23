import random
import pygame
import math
from pygame.locals import *
pygame.init()

# Window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('BarBy')
icon = pygame.image.load('cookie.png')
pygame.display.set_icon(icon)
pygame.time.Clock().tick(60)

# Coordonate
player_1_x = 100 
player_1_y = 300

player_2_x = 500 
player_2_y = 300

glont_1_x = 110
glont_1_y = 400

glont_2_x = 510 
glont_2_y = 400

boss_x = 400
boss_y = 100

cursor_x = 400
cursor_y = 300

ammo_boss_x = boss_x
ammo_boss_y = boss_y

ammo_x = random.randint(32, 768)
ammo_y = random.randint(32, 568)

comoara_x = 365
comoara_y = 400


# Poze
player_1_image = pygame.image.load( 'fat.png' )
player_2_image = pygame.image.load( 'eat.png' )

glont_1_image = pygame.image.load( 'cookie.png' )
glont_2_image = pygame.image.load( 'pizza.png' )

boss_image = pygame.image.load( 'Boss.png' )

cursor_image = pygame.image.load ( 'click.png' )

ammo_image = pygame.image.load ( 'plate.png' )

comoara_image = pygame.image.load ( 'comoara.png' )

ammo_boss_image = pygame.image.load ( 'bossammo.png' )

Camera_2_background = pygame.image.load( 'camera1.png' )
Camera_3_background = pygame.image.load( 'camera23.png' )
Camera_4_background = pygame.image.load( 'Camera 4.png' )
Camera_5_background = pygame.image.load( 'defeat.jpg' )
Camera_6_background = pygame.image.load( 'Victory.png' )

# Camere
Camera_1 = True
Camera_2 = False
Camera_3 = False
Camera_4 = False
Camera_5 = False
Camera_6 = False

# Variabile ajutatoare
glont_folosit = 0
player_folosit = 0

miscare_x = 0
miscare_y = 0

miscare_boss_x = 2
miscare_boss_y = 2

miscare_glont_boss = 10

A = 0
#B = False

#munitie = 0

#font = pygame.font.Font('arialblack', 20 )

# Damage
damage = 0
damage_player = 0

# Status glont

glont_status = True

# Avatare
def player_1 ( x, y ):
    screen.blit( player_1_image, ( x, y )) 

def player_2 ( x, y ):
    screen.blit( player_2_image, ( x, y ))

# Gloante
def glont_1 ( x, y ):
    screen.blit ( glont_1_image, ( x, y ))

def glont_2 ( x, y ):
    screen.blit ( glont_2_image, ( x, y ))

miscare_glont_y = 2

# Boss
def boss ( x, y ):
    screen.blit ( boss_image, ( x, y ))

# Comoara
def comoara ( x, y ):
    screen.blit ( comoara_image, ( x, y ))  

# Cursor
def cursor( x, y ):
    screen.blit ( cursor_image, ( x, y ))

# Ammo
def ammo( x, y ):
    screen.blit( ammo_image, ( x, y ) )

# Boss Ammo
def boss_ammo( x, y ):
    screen.blit( ammo_boss_image, ( x, y ) )

# Coliziune
def coliziune ( x, y, x_1, y_1 ):
    distance = math.sqrt(( math.pow( x - x_1, 2 ) ) + math.pow( y - y_1, 2 ) )
    if distance < 36:
        return True

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if glont_folosit == 1 and glont_status == True and A != 0:
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    glont_1_x = player_1_x
                    glont_1_y = player_1_y
                    glont_status = False
                    glont_1( glont_1_x , glont_1_y )
                     
        if glont_folosit == 2 and glont_status == True and A != 0:
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    glont_2_x = player_2_x
                    glont_2_y = player_2_y
                    glont_status = False
                    glont_2( glont_2_x , glont_2_y )        

        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                miscare_x -= 0.35
            if event.key == K_d:
                miscare_x =+ 0.35
            if event.key == K_w:
                miscare_y -= 0.35
            if event.key == K_s:
                miscare_y += 0.35
        if event.type == pygame.KEYUP:
            if event.key == K_a or event.key == K_d:
                miscare_x = 0
            if event.key == K_w or event.key == K_s:
                miscare_y = 0         

    
# Camera 1
    if Camera_1 == True:
        screen.fill((0, 255, 0))
        cursor( cursor_x, cursor_y )
        cursor_x += miscare_x
        cursor_y += miscare_y
        player_1 ( player_1_x, player_1_y )
        player_2 ( player_2_x , player_2_y )
        glont_1 ( glont_1_x, glont_1_y )
        glont_2 ( glont_2_x, glont_2_y )
        if coliziune( cursor_x, cursor_y, player_1_x, player_1_y ):
            player_folosit = 1
            glont_folosit = 1
            Camera_1 = False
            Camera_2 = True
            miscare_x = 0
            miscare_y = 0
            player_1_x = 400
            player_1_y = 300
        if coliziune( cursor_x, cursor_y, player_2_x, player_2_y ):
            player_folosit = 2
            glont_folosit = 2 
            Camera_1 = False
            Camera_2 = True
            miscare_x = 0
            miscare_y = 0
            player_2_x = 400
            player_2_y = 300   

# Camera 2
    if Camera_2:
        screen.blit(Camera_2_background, ( 0, 0 ))
        
        #if B:
            #text = font.render ( 'Ammo:' + str(munitie),1 ,(255, 255, 255) )
            #screen.blit( text , ( 20, 575 ) )

        if A != 2:
            ammo( ammo_x, ammo_y )

        if glont_folosit == 1 :
            if glont_status == False :
                glont_1( glont_1_x, glont_1_y )
                glont_1_y -= miscare_glont_y
                
                if coliziune(glont_1_x, glont_1_y, boss_x, boss_y):
                    glont_1_y = player_1_y
                    glont_status = True

                if glont_1_y <= 0:
                    glont_status = True
                    glont_1_y = player_1_y
 
        if glont_folosit == 2 :
            if glont_status == False :
                glont_2( glont_2_x, glont_2_y )
                glont_2_y -= miscare_glont_y
                 
                if coliziune(glont_2_x, glont_2_y, boss_x, boss_y):
                    glont_2_y = player_2_y
                    glont_status = True

                if glont_2_y <= 0:
                    glont_status = True
                    glont_2_y = player_2_y    
                            

        if player_folosit == 1:
            player_1 ( player_1_x, player_1_y )
            player_1_x += miscare_x*5
            player_1_y += miscare_y*5

            if coliziune ( player_1_x, player_1_y, ammo_x, ammo_y ) and A != 2:
                ammo_x = random.randint(32, 768)
                ammo_y = random.randint(32, 568)
                A += 1
                #munitie += 3
                #B = True

            if player_1_x <= 0:
                player_1_x = 0 
            elif player_1_x >= 736:
                player_1_x = 736
                Camera_2 = False
                Camera_3 = True      
            if player_1_y <= 0:
                player_1_y = 0 
            elif player_1_y >= 536:
                player_1_y = 536
                Camera_2 = False
                Camera_3 = True  

        if player_folosit == 2:
            player_2 ( player_2_x, player_2_y )
            player_2_x += miscare_x*5
            player_2_y += miscare_y*5

            if coliziune ( player_2_x, player_2_y, ammo_x, ammo_y ) and A != 2:
                ammo_x = random.randint(32, 768)
                ammo_y = random.randint(32, 568)
                A += 1
                #munitie += 3
                #B = True
            
            if player_2_x <= 0:
                player_2_x = 0 
            elif player_2_x >= 736:
                player_2_x = 0
                Camera_2 = False
                Camera_3 = True    
            if player_2_y <= 0:
                player_2_y = 0 
            elif player_2_y >= 536:
                player_2_y = 0
                Camera_2 = False
                Camera_3 = True
    
# Camera 3
    if Camera_3:
        screen.blit(Camera_3_background, ( 0, 0 ))

        comoara( comoara_x, comoara_y )

        if player_folosit == 1:
            if coliziune( player_1_x, player_1_y, comoara_x, comoara_y ):
                Camera_3 = False
                Camera_4 = True

        if player_folosit == 2:
            if coliziune( player_2_x, player_2_y, comoara_x, comoara_y ):
                Camera_3 = False
                Camera_4 = True        

        if glont_folosit == 1 :
            if glont_status == False :
                glont_1( glont_1_x, glont_1_y )
                glont_1_y -= miscare_glont_y

                if glont_1_y <= 0:
                    glont_status = True
                    glont_1_y = player_1_y
 
        if glont_folosit == 2 :
            if glont_status == False :
                glont_2( glont_2_x, glont_2_y )
                glont_2_y -= miscare_glont_y

                if glont_2_y <= 0:
                    glont_status = True
                    glont_2_y = player_2_y    
                            

        if player_folosit == 1:
            player_1 ( player_1_x, player_1_y )
            player_1_x += miscare_x*5
            player_1_y += miscare_y*5

            if player_1_x <= 0:
                player_1_x = 0 
            elif player_1_x >= 736:
                player_1_x = 736      
            if player_1_y <= 0:
                player_1_y = 0 
            elif player_1_y >= 536:
                player_1_y = 536
        
        if player_folosit == 2:
            player_2 ( player_2_x, player_2_y )
            player_2_x += miscare_x*5
            player_2_y += miscare_y*5

            if player_2_x <= 0:
                player_2_x = 0 
            elif player_2_x >= 736:
                player_2_x = 736       
            if player_2_y <= 0:
                player_2_y = 0 
            elif player_2_y >= 536:
                player_2_y = 536

# Camera 4           
    if Camera_4:
        screen.blit(Camera_4_background, ( 0, 0 ))

        boss( boss_x, boss_y )
        

        boss_x += miscare_boss_x
        boss_y += miscare_boss_y

        if boss_x <= 0 or boss_x >= 764:
            miscare_boss_x *= -1
        if boss_y <= 0 or boss_y >= 168:
            miscare_boss_y *= -1


        boss_ammo(ammo_boss_x, ammo_boss_y)

        ammo_boss_y += miscare_glont_boss       

        if player_folosit == 1:
            if coliziune( player_1_x, player_1_y, ammo_boss_x, ammo_boss_y ):
                ammo_boss_x = boss_x
                ammo_boss_y = boss_y

        if player_folosit == 2:
            if coliziune( player_2_x, player_2_y, ammo_boss_x, ammo_boss_y ):
                ammo_boss_x = boss_x
                ammo_boss_y = boss_y

        if ammo_boss_y <= 599:
            ammo_boss_x = boss_x
            ammo_boss_y = boss_y

        pygame.draw.rect(screen, (255, 0, 0),( boss_x + 6 , boss_y + 63, 53 - (10 * damage) , 10) )
        
        if player_folosit == 1:
            pygame.draw.rect(screen, (255, 0, 0),( player_1_x + 6 , player_1_y + 63, 53 - (27 * damage_player) , 10) )

        if player_folosit == 2:
            pygame.draw.rect(screen, (255, 0, 0),( player_2_x + 6 , player_2_y + 63, 53 - (25 * damage_player) , 10) )    
                


#Repet        
        if glont_folosit == 1 :
            if glont_status == False :
                glont_1( glont_1_x, glont_1_y )
                glont_1_y -= miscare_glont_y
                
                if coliziune(glont_1_x, glont_1_y, boss_x, boss_y):
                    glont_1_y = player_1_y
                    glont_status = True
                    damage += 1

                if glont_1_y <= 0:
                    glont_status = True
                    glont_1_y = player_1_y
 
        if glont_folosit == 2 :
            if glont_status == False :
                glont_2( glont_2_x, glont_2_y )
                glont_2_y -= miscare_glont_y
                 
                if coliziune(glont_2_x, glont_2_y, boss_x, boss_y):
                    glont_2_y = player_2_y
                    glont_status = True
                    damage += 1

                if glont_2_y <= 0:
                    glont_status = True
                    glont_2_y = player_2_y    
                            

        if player_folosit == 1:
            player_1 ( player_1_x, player_1_y )
            player_1_x += miscare_x*5
            player_1_y += miscare_y*5

            if player_1_x <= 0:
                player_1_x = 0 
            elif player_1_x >= 736:
                player_1_x = 736      
            if player_1_y <= 0:
                player_1_y = 0 
            elif player_1_y >= 536:
                player_1_y = 536
        
        if player_folosit == 2:
            player_2 ( player_2_x, player_2_y )
            player_2_x += miscare_x*5
            player_2_y += miscare_y*5

            if player_2_x <= 0:
                player_2_x = 0 
            elif player_2_x >= 736:
                player_2_x = 736       
            if player_2_y <= 0:
                player_2_y = 0 
            elif player_2_y >= 536:
                player_2_y = 536
                    

   
    pygame.display.update()
