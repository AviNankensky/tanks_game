
from tkinter import *
from asyncio.windows_events import NULL
from random import choice 
import pygame

from pygame.sprite import spritecollide 


screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
win= Tk()
win.geometry("650x250")
width =  win.winfo_screenheight()
length = win.winfo_screenwidth() 



class Background(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.background = pygame.transform.scale(pygame.image.load('graphics/background.jpg'),(length,width)).convert_alpha()  
        self.pos=pos
        
        self.image=self.background
        self.rect=self.background.get_rect(topleft = (self.pos))
        
    def update(self):
        camera(self,"background")
        
class Tank(pygame.sprite.Sprite):
    
    def __init__( self): 
        super().__init__()
        # self.image = pygame.Surface((60, 60))
        # self.image.fill((255,0,0))
        # self.rect = self.image.get_rect()
        # self.rect.topleft = (40, 40) 
        
        
        
        self.tank_image = pygame.image.load('graphics/tank/tank.png').convert_alpha()
        
        self.image = self.tank_image
        self.rect = self.image.get_rect(center = (37,37))
        self.direction=""
        self.activ=False
        
        
        self.tank_speed =1
        
    def input(self):
        
        self.keys = pygame.key.get_pressed()
        if stone_block() or enemy_back():
            self.activ=False
            if self.direction=="left":
                self.rect.x+=2
                
            if self.direction=="right":
                self.rect.x-=2
                
            if self.direction=="up":
                self.rect.y+=2
                
            if self.direction=="down":
                self.rect.y-=2
                
          
        if  self.keys[pygame.K_LEFT]:
            self.direction="left"
            self.activ=True
            self.image = pygame.transform.rotate(self.tank_image,90)
            self.rect.x -= self.tank_speed
            if self.rect.x< 0:
                    
                self.rect.x = 0
            
                
        elif self.keys[pygame.K_RIGHT]:
            self.direction="right"
            self.activ=True
            self.image = pygame.transform.rotate(self.tank_image,270)
            self.rect.x += self.tank_speed
            if self.rect.x >length-45:
                self.rect.x=length-45
            
        elif self.keys[pygame.K_UP]:
            self.direction="up"
            self.activ=True
            self.image = pygame.transform.rotate(self.tank_image,0)
            self.rect.y -= self.tank_speed
            if self.rect.y <0:
                self.rect.y = 0
            
        elif self.keys[pygame.K_DOWN]:
            self.direction="down"
            self.activ=True
            self.image = pygame.transform.rotate(self.tank_image,180)
            self.rect.y += self.tank_speed
            if self.rect.y>width-110:
                self.rect.y = width-110
        else:
            self.activ=False
                
    
    def reset_game(self):
        if bollet_hit_player():
            self.rect.x=37
            self.rect.y=37
            
            
    def update(self):
        self.reset_game()
        self.input()      
            
class Ball(pygame.sprite.Sprite):
    def __init__(self, pos ,direction,self_type):
        super().__init__()  
        self.ball = pygame.image.load('graphics/weapons/ball.png').convert_alpha()
        
        self.type=self_type
        self.rect = self.ball.get_rect(center = pos)
        self.image = self.ball
        self.direction = direction
        self.ball_speed=10
        
    def ball_movement(self):
        
        if self.direction == "smart_move" :
            self.kill()
        
        if self.direction == "right":
            self.rect.x += self.ball_speed
            
        if self.direction == "left":
            self.rect.x -= self.ball_speed
            
        if self.direction == "up":
            self.rect.y -= self.ball_speed
            
        if self.direction == "down":
            self.rect.y += self.ball_speed
   
    
        
   
        if self.rect.x > length or self.rect.x < 0 or self.rect.y > width-50 or self.rect.y < 0 or stone_wall_block_ball():
            ball_animation.add(Ball_animation((self.rect.x,self.rect.y)))
            self.kill()
        
            
    def update(self):
        self.ball_movement()
 
class Tnt_explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        explosion_1 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_1.png'),(200,200)).convert_alpha()
        explosion_2 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_2.png'),(200,200)).convert_alpha()
        explosion_3 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_3.png'),(200,200)).convert_alpha()
        explosion_4 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_4.png'),(200,200)).convert_alpha()
        explosion_5 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_5.png'),(200,200)).convert_alpha()
        explosion_6 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_6.png'),(200,200)).convert_alpha()
        explosion_7 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_7.png'),(200,200)).convert_alpha()
        explosion_8 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_8.png'),(200,200)).convert_alpha()
        self.explosion_image_list=[explosion_1, explosion_2, explosion_3, explosion_4, explosion_5, explosion_6, explosion_7, explosion_8]
        
        self.image = self.explosion_image_list[0]
        self.rect = self.image.get_rect(center = (x+20,y))
        
        # self.rect.y-=75
        # self.rect.x-=75
        self.index=0

    def animation(self):
        self.index +=0.2
        self.image=self.explosion_image_list[int(self.index)]
        if self.index>len(self.explosion_image_list)-0.5:
            self.kill()

    def update(self):
        self.animation()
        camera(self,"")
        #tnt_exploded()
       
class Tnt(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.tnt = pygame.transform.scale(pygame.image.load('graphics/weapons/tnt.jpg'),(50,50)).convert_alpha()
        

        # explosion_1 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_1.png'),(200,200)).convert_alpha()
        # explosion_2 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_2.png'),(200,200)).convert_alpha()
        # explosion_3 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_3.png'),(200,200)).convert_alpha()
        # explosion_4 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_4.png'),(200,200)).convert_alpha()
        # explosion_5 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_5.png'),(200,200)).convert_alpha()
        # explosion_6 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_6.png'),(200,200)).convert_alpha()
        # explosion_7 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_7.png'),(200,200)).convert_alpha()
        # explosion_8 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_8.png'),(200,200)).convert_alpha()
        # self.explosion_image_list=[explosion_1, explosion_2, explosion_3, explosion_4, explosion_5, explosion_6, explosion_7, explosion_8]
        self.rect = self.tnt.get_rect(center = (x,y))
        
        self.rect.x=x
        self.rect.y=y
        self.image=self.tnt
        self.index=0
        self.time_for_explos=20
        self.explosion_pos=0
        #self.type_of_tnt = ""
        
        
    def animation(self):
        
        self.time_for_explos-=0.2
        if self.time_for_explos<0:
            if self.explosion_pos<1:
                #self.type_of_tnt="explosion"
                
                # self.rect.y-=75
                # self.rect.x-=75
                self.explosion_pos+=1
                tnt_explosion.add(Tnt_explosion(self.rect.x,self.rect.y))
                self.kill()
                
            #self.index+=0.1
            
            # self.image=self.explosion_image_list[int(self.index)]
            # #self.rect.y-=0.7
            # if self.index>len(self.explosion_image_list)-0.5:
            #     self.kill()
        
        
    
        
    def update(self):
        camera(self,"")
        #tnt_exploded()
        self.animation()
        #self.explode()
        
class Ice_wall(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        super().__init__()
        self.ice = pygame.transform.scale(pygame.image.load('graphics/weapons/ice_wall.png'),(50,50)).convert_alpha()  

        
        self.rect = self.ice.get_rect(center = (x,y))
        self.image = self.ice
        
        self.rect.x=x
        self.rect.y=y
        self.time = 0
        self.direction=direction

    def movement(self):
        if self.direction == "up":
            self.rect.y-=1
           
        if self.direction == "down":
            self.rect.y+=1
        
        if self.direction == "left":
            self.rect.x-=1
            
        if self.direction == "right":
            self.rect.x+=1
            
            
       

    def animation(self):
        self.image = pygame.transform.scale(self.image,(50,50)).convert_alpha()
        self.rect.x+self.time
        self.rect.y+self.time

    def destroy(self):
        self.time+=0.2
        if self.time > 50:
            self.kill()
            
    def update(self):
        camera(self,"")
        #self.movement()
        self.destroy()
        self.animation()
        
class Wood_wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.wood = pygame.image.load('graphics/wall/wood.png')
        
        self.rect = self.wood.get_rect(center = (x,y))
        self.image = self.wood
        
        self.rect.x=x
        self.rect.y=y
        self.flag=""

    def destroy(self):
        wood_wall_bomber()     
        
    

    def update(self):
        
        camera(self,"")
        
        self.destroy()
        
class Stone_wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.stone_wall = pygame.image.load('graphics/wall/Stone_wall.png').convert_alpha()
        self.rect = self.stone_wall.get_rect(center = (x,y))
        self.rect.x=x
        self.rect.y=y

        self.image = self.stone_wall
        
    
    def update(self):
        camera(self,"")
        
class Trees_wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.trees_wall = pygame.image.load('graphics/wall/trees.png').convert_alpha()
        self.rect = self.trees_wall.get_rect(center = (x,y))
        self.rect.x=x
        self.rect.y=y
        self.image = self.trees_wall
        
    
    def update(self):
        camera(self,"")
        
class Shield_stone_wall(pygame.sprite.Sprite):
    
    def __init__(self,pos):
        super().__init__()
        
        self.strong_wall = pygame.image.load('graphics/wall/strong_wall.jpg').convert_alpha()
        self.rect=self.strong_wall.get_rect(center = (pos))
        self.image = self.strong_wall
        self.resistance= 5
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
   
        
    def get_self_resistance(self):
        return self.resistance
        
    def dstroy (self):
        shield_stone_wall_block_balls()
    
       
    def update(self):
        self.dstroy()
        camera(self,"")
            
class Enemy_tank(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        self.enemy_tank = pygame.image.load('graphics/enemy_tank/enemy_tank.png').convert_alpha()
        self.rect = self.enemy_tank.get_rect(center = pos)
        self.image = self.enemy_tank
        self.direction=choice(["up","right","left","down"])
        self.tank_speed=1
        self.smart_move_area = 100
        self.shoot_time=40
        
    def time_to_shoot(self):
        self.shoot_time-=0.5
        if self.shoot_time<0:
            balls.add(Ball(self.rect.center,self.direction,"enemy_ball"))
            self.shoot_time=40
            
     
    def smart_move(self):
        if self.rect.x>tank.sprite.rect.x :
            if self.rect.y>tank.sprite.rect.y:
                self.direction = choice( ["up","left"])
            
            elif self.rect.y<tank.sprite.rect.y:
                self.direction = choice(["down","left"])
                
            else:
                self.direction = "left"
                
        if self.rect.x<tank.sprite.rect.x :
            if self.rect.y>tank.sprite.rect.y:
                self.direction = choice(["up", "right"])
            elif self.rect.y<tank.sprite.rect.y:
                self.direction = choice(["down","right"])
            else:
                self.direction = "right"

    def random_movw(self):
        if enemy_back():
            if self.direction=="down":
                while self.rect.y==self.rect.y-10:
                    self.rect.y -=1
                self.direction="up"
                
            if self.direction=="up":
                while self.rect.y==self.rect.y+10:
                    self.rect.y +=1
                self.direction="down"
                
            if self.direction=="right":
                while self.rect.x==self.rect.x-10:
                    self.rect.x -=1
                self.direction="left"
                
            if self.direction=="left":
                while self.rect.x==self.rect.x+10:
                    self.rect.x +=1
                self.direction="right"
    

        if self.direction=="down":
            self.image = pygame.transform.rotate(self.enemy_tank,0)
            self.rect.y+=self.tank_speed
            if enmey_stonr_block() :
                self.direction=choice(["up","right","left","smart_move","smart_move","smart_move"])
                self.rect.y-=1 
        
            if self.rect.y>=width-110:
                self.rect.y-=1
                self.direction=choice(["right","left","up"])
                

        elif self.direction=="up":
            self.image = pygame.transform.rotate(self.enemy_tank,180)
            self.rect.y-=self.tank_speed
            if enmey_stonr_block() :
                self.direction=choice(["right","left","down","smart_move","smart_move","smart_move"])
                self.rect.y+=1
        
            if self.rect.y<=0:
                self.rect.y+=1
                self.direction=choice(["down","right","left"])
            
                
            
        elif self.direction=="right":
            self.image = pygame.transform.rotate(self.enemy_tank,90)
            self.rect.x+=self.tank_speed
            if enmey_stonr_block() :
                self.direction=choice(["up","left","down","smart_move","smart_move","smart_move"])
                self.rect.x-=1
        
            if self.rect.x>=length-40:
                self.rect.x-=1
                self.direction=choice(["up","left","down"])
            
          
            
        elif self.direction=="left":
            self.image = pygame.transform.rotate(self.enemy_tank,270)
            self.rect.x-=self.tank_speed
            if enmey_stonr_block() :
                self.rect.x+=1
                self.direction=choice(["up","right","down","smart_move","smart_move","smart_move"])
        
            if self.rect.x<=0:
                self.rect.x+=1
                
                self.direction=choice(["up","right","down"])
    
    def dostroy(self):
        bollet_hit_enemy_tank()
            
    def freeze(self):
        NULL
        
         
    
    def update(self):
        
        if self.direction == "freeze":
            self.freeze()
        else:
            self.time_to_shoot()
        if self.direction == "smart_move":
            self.smart_move()
        self.random_movw()
        self.dostroy()
        
        camera(self,"")
        
class Flag(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.flag=pygame.image.load('graphics/flag.png').convert_alpha()
        self.rect= self.flag.get_rect(center = (15,175))
        self.image=self.flag
        
    def dstroy(self):
        NULL
        # if flag_hit_from_ball():
        #     self.kill()
    
            
    def update(self):
        camera(self,"")      

class Star(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        
        star_1 =pygame.image.load("graphics/star/star_1.png").convert_alpha()
        star_2 =pygame.image.load("graphics/star/star_2.png").convert_alpha()
        star_3 =pygame.image.load("graphics/star/star_3.png").convert_alpha()
        star_4 =pygame.image.load("graphics/star/star_4.png").convert_alpha()
        star_5 =pygame.image.load("graphics/star/star_5.png").convert_alpha()
        star_6 =pygame.image.load("graphics/star/star_6.png").convert_alpha()
        star_7 =pygame.image.load("graphics/star/star_7.png").convert_alpha()
        
        # star_1 = pygame.transform.scale(pygame.image.load("graphics/star/star_1.png"),(25,25)).convert_alpha()
        # star_2 = pygame.transform.scale(pygame.image.load("graphics/star/star_1.png"),(35,35)).convert_alpha()
        # star_3 = pygame.transform.scale(pygame.image.load("graphics/star/star_1.png"),(50,50)).convert_alpha()
        self.star_frames=[star_1, star_2 ,star_3 ,star_4 ,star_5, star_6, star_7]
        self.index=0
        self.image= self.star_frames[self.index]
        self.rect = self.image.get_rect(center = pos)
        
        self.pos = pos
        
    def star_animhithn(self):
        self.index+=0.3
        self.image=self.star_frames[int(self.index)]
        
        if self.index>=len(self.star_frames)-1 :
           enemy_tank.add(Enemy_tank(self.pos))
           self.kill()
           
        
    
    def update(self):
        self.star_animhithn()
        camera(self,"")
    
class Ball_animation(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        boom_1 = pygame.image.load('graphics/boom/boom_1.png').convert_alpha()
        boom_2 = pygame.image.load('graphics/boom/boom_2.png').convert_alpha()
        boom_3 = pygame.image.load('graphics/boom/boom_3.png').convert_alpha()
        boom_4 = pygame.image.load('graphics/boom/boom_4.png').convert_alpha()
        boom_5 = pygame.image.load('graphics/boom/boom_5.png').convert_alpha()
        boom_6 = pygame.image.load('graphics/boom/boom_6.png').convert_alpha()
        self.boom_image = [boom_1, boom_2, boom_3, boom_4, boom_5, boom_6]
        self.animation_index = 0
        self.image= self.boom_image[self.animation_index]
        self.rect = self.image.get_rect(center = pos)
        
    def animation(self):
        self.animation_index+=0.2
        self.image= self.boom_image[int(self.animation_index)]
        
        if self.animation_index>=len(self.boom_image)-1:
            self.kill()
            
        
    # def camera(self,""): 
    #     if tank.sprite.activ:
    #         if tank.sprite.direction=="right":
    #             self.rect.x-=1
            
    #         if tank.sprite.direction=="left":
    #             self.rect.x+=1
    def update(self):
        #self.camera()
        camera(self,"")
        self.animation()

class Heart(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos=pos
        self.heart = pygame.image.load('graphics/heart.png').convert_alpha()
        self.rect = self.heart.get_rect(center = pos)
        self.image=self.heart
       
class Bounse(pygame.sprite.Sprite):
    def __init__(self,type,x,y):
        super().__init__()
        self.x=x
        self.y=y
        self.type =type
        self.heart = pygame.transform.scale(pygame.image.load('graphics/heart.png'),(25,25)).convert_alpha()
        if self.type=="heart":
            self.image=self.heart
            self.rect = self.heart.get_rect(center = (self.x,self.y))
        
max_x = length*2-10
min_x = length*-2
print(min_x)
def camera(group,type): 

    
        
    if tank.sprite.activ==True :
            
        if tank.sprite.direction=="right":
            
            if group.rect.x>min_x:
                group.rect.x-=1
                
 
            else:
                tank.sprite.activ=False
                group.rect.x-=1
            
        if tank.sprite.direction=="left" :
            if group.rect.x<max_x:
                group.rect.x+=1        
            else:
                tank.sprite.activ=False
            # if group.rect.x>=max_x:
            #     tank.sprite.activ=False
            #     group.rect.x-=1 
                



def stone_block():
    
    if pygame.sprite.spritecollide(tank.sprite,ice_wall,False):
        if pygame.sprite.spritecollide(tank.sprite,ice_wall,False,pygame.sprite.collide_mask):
            return True
    if pygame.sprite.spritecollide(tank.sprite,tnt,False):
        if pygame.sprite.spritecollide(tank.sprite,tnt,False,pygame.sprite.collide_mask):
            return True
          
    if pygame.sprite.spritecollide(tank.sprite,stone_wall,False):
        return True
    
    if pygame.sprite.spritecollide(tank.sprite,wood_wall,False):
        return True
    
    if pygame.sprite.spritecollide(tank.sprite,enemy_tank,False):
        return True
   
    if pygame.sprite.spritecollide(tank.sprite,shield_ston,False):
        return True

    else:
        return False
                                    
def bollet_hit_player(): 
     
     for ball in balls:
         if ball.type=="enemy_ball":
             if pygame.sprite.spritecollide(ball,tank,False) :
                    ball_animation.add(Ball_animation((ball.rect.x,ball.rect.y)))   
                    ball.kill()
                    
                    for hert in heart:
                        hert.kill()
                        break
                        

                    return True
     else:
         return False

def wood_wall_bomber():
    
    for ball in balls:
        box_collide=pygame.sprite.spritecollide(ball,wood_wall,False)
        
        for wood in box_collide:
            wood.kill()
            ball_animation.add(Ball_animation((ball.rect.x,ball.rect.y)))
            ball.kill()         
    
def shield_stone_wall_block_balls():
    for ball in balls:
        ston_shat =pygame.sprite.spritecollide(ball, shield_ston,False)
  
        for ston in ston_shat:
            ston.resistance-=1
            if ston.get_self_resistance()==0:
                ston.kill()   
            ball.kill()
            ball_animation.add(Ball_animation((ball.rect.x,ball.rect.y)))
            
def enemy_back():
    for enemy in enemy_tank:
        if pygame.sprite.spritecollide(enemy,tank,False):
            
            return True
    else:
        return False
    
def enmey_stonr_block():
    oter_enemy = enemy_tank.copy()
    
    for enemy in enemy_tank:
        
        oter_enemy.remove(enemy)
        
        if pygame.sprite.spritecollide(enemy,wood_wall,False):
            return True
        if pygame.sprite.spritecollide(enemy,stone_wall,False):
            return True
        if pygame.sprite.spritecollide(enemy,ice_wall,False):
            enemy.direction = "freeze"
        
        if pygame.sprite.spritecollide(enemy,tnt,False):
            if pygame.sprite.spritecollide(enemy,tnt,False,pygame.sprite.collide_mask):
                return True
            
        if pygame.sprite.spritecollide(enemy,shield_ston,False):
            return True
        
        if  pygame.sprite.spritecollide(enemy,oter_enemy,False) :
            
            return True
        
def bollet_hit_enemy_tank():
    
    for ball in balls:
        if ball.type=="player_ball":
            enemy_tank_kill= pygame.sprite.spritecollide(ball,enemy_tank,False)
            
            for enemy in enemy_tank_kill:
                enemy.kill()
                ball_animation.add(Ball_animation((ball.rect.x,ball.rect.y)))
                ball.kill()
                return True
    return False       

def stone_wall_block_ball():
    for ball in balls:
        if pygame.sprite.spritecollide(ball,stone_wall,False):
            return True
        if pygame.sprite.spritecollide(ball,ice_wall,False):
            if pygame.sprite.spritecollide(ball,ice_wall,False,pygame.sprite.collide_mask):
                return True
    else:
         return False
    
def tnt_exploded():
    
    for tnt_bom in tnt_explosion:
        
        wood_explos = pygame.sprite.spritecollide(tnt_bom,wood_wall,False)
        
        for explos in wood_explos:
            explos.kill()
            
        enemy_explos = pygame.sprite.spritecollide(tnt_bom,enemy_tank,False)
        
        for enemy in enemy_explos:
            enemy.kill()
            
        return len(enemy_explos)
       
    return 0
        

#groups
background = pygame.sprite.Group()

bounses = pygame.sprite.Group()

heart = pygame.sprite.Group()

tnt = pygame.sprite.Group()
tnt_explosion = pygame.sprite.Group()

ice_wall = pygame.sprite.Group()

wood_wall = pygame.sprite.Group()

stone_wall = pygame.sprite.Group()

trees_wall = pygame.sprite.Group()

shield_ston = pygame.sprite.Group()

star =pygame.sprite.Group()

ball_animation= pygame.sprite.Group()

enemy_tank = pygame.sprite.Group()

my_flag= pygame.sprite.Group()

my_flag.add(Flag())

tank = pygame.sprite.GroupSingle()

tank.add(Tank())

balls =pygame.sprite.Group()

