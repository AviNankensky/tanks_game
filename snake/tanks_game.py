from asyncio.windows_events import NULL

from turtle import update

import pygame 
from sys import exit
from random import choice ,randint 
from tkinter import *
from Class_of_game import *



win= Tk()
win.geometry("650x250")
width =  win.winfo_screenheight()
length = win.winfo_screenwidth() 
outcome_of_enemy_tanks=0
game_active=False
start_time=0
score=0
weapon_type = 'ball'
weapon_list=["ball","ice","tnt"]
weapon_index=0
num_enemy_tank=5
screen_2=False



def star_block():
    for enemy in enemy_tank:
        if enemy.rect.x>650 and enemy.rect.x<950 and  enemy.rect.y<150 :
            
            return False
    else:
        return True   
            
def oter_enemy_bomber(): 
    
    for enemy in enemy_tank:
        if  pygame.sprite.spritecollide(enemy,star,False):
            
            return True
    else:
        return False      
            
def ice_wall_bomber(): 
    for enemy in enemy_tank:
        if pygame.sprite.spritecollide(enemy,ice_wall,False):
            enemy.kill()
        
        
  
    
def flag_hit_from_ball(): 
    for ball in balls:
        if pygame.sprite.spritecollide(ball,door,False):
            
            return False
    else:
        return True
               
def reset_game(): 
    

    tank.sprite.key=True
    tank.sprite.rect.x=50
    tank.sprite.rect.y=50
    ice_wall.empty()
    trees_wall.empty()
    wood_wall.empty()
    stone_wall.empty()
    shield_ston.empty()
    enemy_tank.empty()
    balls.empty()
    heart.empty()
    
    
    pixels()
    door.add(Door(0,150))
    key.add(Key(150,150,True))

    #background
    background.add(Background((0,0)))
    background.add(Background((length+1,0)))
    background.add(Background((length*2+1,0)))

    
    
    #heart
    num_of_heart=3
    pos_of_heart=[(50,width-40),(100,width-40),(150,width-40)] 
    while num_of_heart>0:
        heart.add(Heart(pos_of_heart[num_of_heart-1]))
        num_of_heart-=1 

def pixels(): 
    

    

    pos_ston = [(50,100),(50,200),(100,100),(100,150),(100,200)]
    for i in range(len(pos_ston)):
        shield_ston.add(Shield_stone_wall(pos_ston[i]))
        
    for r in range(0,length*3,50):   # 800
        for c in range(0,width-50,50):   #400
            type_pixel =choice(['stone','wood',"empty",'trees','wood','wood',"empty","","",""])
            
            if c==0  or c>width-125 or r==0 and c!=150 or r >length*3-50:
                stone_wall.add(Stone_wall(r,c)) 
            elif r<=150 and c<=300 or r==750 and c==0 or c==150 or(r==0 and (c== 150 or c==200 or c==100) or r==50 and (c==100 or c==150 or c==200 ) )  :
                NULL
            
            else:
                if  type_pixel=="bounses":
                    bounses.add(Bounse("heart",r,c))
                    print("test")
                    
                if  type_pixel == "empty":
                    NULL
                
                if  type_pixel== 'stone':
                    stone_wall.add(Stone_wall(r,c)) 
            
                if  type_pixel=='trees':
                    trees_wall.add(Trees_wall(r,c))
            
                if  type_pixel =='wood':
                    wood_wall.add(Wood_wall(r,c)) 
  
def display_score():
    
    current_time = int(pygame.time.get_ticks() / 1000) -start_time
    score_surf = test_font.render(f'Score: {current_time}',False,( 0, 0, 0))
    score_rect = score_surf.get_rect(center = (length-150,width-40))
    screen.blit(score_surf,score_rect)
    return current_time


    
    


pygame.init()
screen = pygame.display.set_mode((0,0)) #, pygame.FULLSCREEN

clock = pygame.time.Clock()
pygame.display.set_caption('Tanks')
test_font = pygame.font.Font('font/OpenSans-Regular-webfont.woff', 50)
star_x=775

imags()

Background_start = pygame.transform.scale(pygame.image.load('graphics/Background of the beginning.jpg'),(length,width)).convert_alpha()  


Background_end = pygame.transform.scale(pygame.image.load('graphics/background_end.png'),(length,width)).convert_alpha()  

# background = pygame.transform.scale(pygame.image.load('graphics/background.jpg'),(length,width)).convert_alpha()  
# background2 = pygame.transform.scale(pygame.image.load('graphics/background.jpg'),(length,width)).convert_alpha()  
# background3 = background2
# background3_x = length*3
# background_x=0
# background2_x=length
    


background_line = pygame.transform.scale(pygame.image.load('graphics/background_line.jpg'),(length,70)).convert_alpha()  









#buttons
ball_image = pygame.transform.scale(pygame.image.load('graphics/weapons/ball_image.jpg'),(40,40)).convert_alpha()
ball_rect = ball_image.get_rect(center = (220,width-40))

ice_image = pygame.transform.scale(pygame.image.load('graphics/weapons/ice_wall.png'),(40,40)).convert_alpha()
ice_rect = ice_image.get_rect(center = (320,width-40))

tnt_image = pygame.transform.scale(pygame.image.load('graphics/weapons/tnt.jpg'),(40,40)).convert_alpha()
tnt_rect = tnt_image.get_rect(center = (420,width-40))


button_type="play"
play_image=pygame.image.load('graphics/buttons/play_2.png').convert_alpha()
play_rect = play_image.get_rect(center = (length/2,width/2-200))



exit_image=pygame.image.load('graphics/buttons/exit_1.png').convert_alpha()
exit_rect = exit_image.get_rect(center = (length/2,width/2-50))




#timers

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,3000)

#background



while True:
    
    #print(tank.sprite.activ)
    #ice_wall_bomber()
    oter_enemy_bomber() 
    
   
    if bollet_hit_enemy_tank():
        outcome_of_enemy_tanks+=1
       
    op=tnt_exploded()
    
    if op>0:
        
        outcome_of_enemy_tanks+=op
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            screen_2=False
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_1:
                    weapon_type=weapon_list[0]
                    weapon_index=-1
                
                if event.key == pygame.K_2:
                    weapon_type=weapon_list[1]
                    weapon_index=-1
                    
                if event.key == pygame.K_3:
                    weapon_type=weapon_list[2]
                    weapon_index=-1
                    
                if event.key == pygame.K_LALT:
                    if weapon_index==len(weapon_list)-1:
                        weapon_index=0  
                        weapon_type=weapon_list[weapon_index]
                    else:
                        weapon_index+=1
                        weapon_type=weapon_list[weapon_index]

                if event.key == pygame.K_SPACE  :
                    
                    if weapon_type == "ball" :
                            balls.add(Ball(tank.sprite.rect.center,tank.sprite.direction,"player_ball"))
                    
                    if weapon_type=='ice'  :
                        
                        if tank.sprite.direction =="right":
                            ice_wall.add(Ice_wall(tank.sprite.rect.x+50,tank.sprite.rect.y,"right"))
                        
                        if tank.sprite.direction =="left":
                            ice_wall.add(Ice_wall(tank.sprite.rect.x-50,tank.sprite.rect.y,"left"))
                        
                        if tank.sprite.direction =="down":
                            ice_wall.add(Ice_wall(tank.sprite.rect.x,tank.sprite.rect.y+50,"down"))
                        
                        if tank.sprite.direction =="up":
                            ice_wall.add(Ice_wall(tank.sprite.rect.x,tank.sprite.rect.y-50,"up"))

                    if weapon_type == "tnt"  :
                        if tank.sprite.direction =="right":
                            tnt.add(Tnt(tank.sprite.rect.x+50,tank.sprite.rect.y))
                        
                        if tank.sprite.direction =="left":
                            tnt.add(Tnt(tank.sprite.rect.x-50,tank.sprite.rect.y))
                        
                        if tank.sprite.direction =="down":
                            tnt.add(Tnt(tank.sprite.rect.x,tank.sprite.rect.y+50))
                        
                        if tank.sprite.direction =="up":
                            tnt.add(Tnt(tank.sprite.rect.x,tank.sprite.rect.y-50))


           
            if event.type == enemy_timer :
                if len(enemy_tank)< 5:
                
                    star.add(Star((star_x,175)))
                for enemy in enemy_tank:
                    enemy.direction=choice(["smart_move","smart_move","smart_move"])#"up","right","left",
                #if num_enemy_tank>0 :  #and star_block()
                
                
                    #num_enemy_tank-=1      
                
            
            
        else:
            if button_type=="screen 2":
                button_type="play"
            start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    #rect = pygame.draw.rect(screen,'black',exit_rect,40)
                    button_type="exit"
                    exit_image=pygame.image.load('graphics/buttons/exit_2.png').convert_alpha()
                    play_image=pygame.image.load('graphics/buttons/play_1.png').convert_alpha()
                    
                
                
                if event.key == pygame.K_UP:
                    button_type="play"
                    
                    exit_image=pygame.image.load('graphics/buttons/exit_1.png').convert_alpha()
                    play_image=pygame.image.load('graphics/buttons/play_2.png').convert_alpha()
                    
                if score > 0  and screen_2== False:
                    button_type ="screen 2"
                    
                if  event.key == pygame.K_SPACE  :
                    
                    if button_type =="screen 2":
                        screen_2 = True
                    

                    if button_type=="play":
                        
                        game_active=True
                        
                        outcome_of_enemy_tanks=0
                        num_enemy_tank=5
                        reset_game()
                        
                    if button_type=="exit":  
                        pygame.quit()
                        exit()
                
      

            
            
            
    if game_active:
         
       
        
        bounses.draw(screen)

        background.draw(screen)
        background.update()

        tank.draw(screen)
        tank.update()
    
   
        star.draw(screen)
        star.update()
    
        enemy_tank.draw(screen)
        enemy_tank.update()
        trees_wall.draw(screen)
        trees_wall.update()

        balls.draw(screen)
        balls.update()
        ball_animation.draw(screen)
        ball_animation.update()


        stone_wall.draw(screen)
        stone_wall.update()
    
        wood_wall.draw(screen)
        wood_wall.update()
        

        shield_ston.draw(screen)
        shield_ston.update()
        door.draw(screen)
        door.update()
        
        
        ice_wall.draw(screen)
        ice_wall.update()
        
        tnt.draw(screen)
        tnt.update()
        
        tnt_explosion.draw(screen)
        tnt_explosion.update()
        
        game_active=door_is_open() #flag_hit_from_ball()
        
        screen.blit(background_line,(0,width-70))
        key.draw(screen)
        key.update()
        screen.blit(ball_image,ball_rect)
        screen.blit(tnt_image,tnt_rect)
        screen.blit(ice_image,ice_rect)
        heart.draw(screen)
        score =display_score()
        if weapon_type=='ball'  :
            pygame.draw.rect(screen,(0,0,0),ball_rect,4)
        if weapon_type=='ice'  :
            pygame.draw.rect(screen,(0,0,0),ice_rect,4)
        if weapon_type=='tnt'  :
            pygame.draw.rect(screen,(0,0,0),tnt_rect,4)
        #screen.blit(Rect)
        if not heart:
            game_active=False
        
    
    else:
        background.empty()
        door.empty()
        key.empty()
        
        if score == 0 or screen_2 :
            screen.blit(Background_start,(0,0))

            screen.blit(play_image,play_rect)
        
            screen.blit(exit_image,exit_rect)
        else :
             screen.fill(( 0, 0, 0)) 
             screen.blit(Background_end,(50,20)) 
             outcome_of_enemy = test_font.render(f'Enemy tanks: {outcome_of_enemy_tanks}',False,(255,255,255))
             screen.blit(outcome_of_enemy,(length/2-200,width/2-50)) 
            
             enemy_tank_image = pygame.transform.scale(pygame.image.load('graphics/enemy_tank/enemy_tank.png'),(80,80)).convert_alpha()  
             
             screen.blit(enemy_tank_image,(length/2+200,width/2-50))
            
        
        
        

    pygame.display.update()
    clock.tick(60)