
from tkinter import *
from asyncio.windows_events import NULL
from random import choice 
import pygame




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
        self.end=""
        
        self.image=self.background
        self.rect=self.image.get_rect(topleft = (self.pos))
        

         
        
    def update(self):
        
        camera(self)
tank_image = pygame.image.load('graphics/tank/tank.png').convert_alpha()  
class Tank(pygame.sprite.Sprite):
    
    def __init__( self): 
        super().__init__()
        
        self.key=True
        self.tank_image=tank_image
        self.image = self.tank_image
        self.rect = self.image.get_rect(center = (150,150))
        self.direction="up"
        self.activ=False
        self.type_=""
        self.rest_pos=False
        
        self.tank_speed = 1
        
    def input(self):
        
        self.keys = pygame.key.get_pressed()
        if stone_block(self) : 
            self.activ=False
            if self.direction=="left":
                self.rect.x+=1
                self.type_="player_blocked"
                
            if self.direction=="right":
                self.rect.x-=1
                self.type_="player_blocked"
                
            if self.direction=="up":
                self.rect.y+=1
                self.type_="player_blocked"
                
            if self.direction=="down":
                self.rect.y-=1
                self.type_="player_blocked"
        # else:
        #     self.activ=True
                
        else:  
            self.type_=" "
            if  self.keys[pygame.K_LEFT]:
                self.direction="left"
                self.activ=True
                self.image = pygame.transform.rotate(self.tank_image,90)
                self.rect.x -= self.tank_speed
                if self.rect.x< 0:
                    
                    self.rect.x = 0
                    self.activ=False
                    
            
                
            elif self.keys[pygame.K_RIGHT] :
                self.direction="right"
                self.activ=True
                self.image = pygame.transform.rotate(self.tank_image,270)
                self.rect.x += self.tank_speed
                if self.rect.x >length-45:
                    
                    self.rect.x=length-45
                    #self.activ=False
            
            elif self.keys[pygame.K_UP]:
                self.direction="up"
                self.activ=True
                self.image = pygame.transform.rotate(self.tank_image,0)
                self.rect.y -= self.tank_speed
                if self.rect.y <0:
                    #self.activ=False
                    self.rect.y = 0
            
            elif self.keys[pygame.K_DOWN]:
                self.direction="down"
                self.activ=True
                self.image = pygame.transform.rotate(self.tank_image,180)
                self.rect.y += self.tank_speed
                if self.rect.y>width-110:
                    #self.activ=False
                    self.rect.y = width-110
            else:
                self.activ=False
                
            if  self.rect.x>length-45:
                self.rect.x-=1 
            if  self.rect.x<50:
                self.rect.x+=1 
            
                
                
    
    def reset_game(self):
        if bollet_hit_player():
            self.rest_pos=True
            self.rect.x=150
            self.rect.y=150
            
        else:
            self.rest_pos=False
            
    # def screen_border(self):
    #     if self.rect.x > length*3 or self.rect.x<0:
    #         self.activ=False
    #     else:
    #         self.activ=True
            
            
            
    def update(self):
        
        #self.screen_border()
        self.reset_game()
        self.input()     
        
class Fire(pygame.sprite.Sprite):
    def __init__(self, pos ,direction):
        super().__init__() 
        self.direction=direction
        if self.direction=="up":
            self.imag_list=[fire_img1_up, fire_img2_up, fire_img3_up, fire_img4_up, fire_img5_up]
            
        if self.direction=="down":
            self.imag_list=[fire_img1_down, fire_img2_down, fire_img3_down, fire_img4_down, fire_img5_down]
            
        if self.direction=="left":
            self.imag_list=[fire_img1_left, fire_img2_left, fire_img3_left, fire_img4_left, fire_img5_left]
            
        if self.direction=="right":
            self.imag_list=[fire_img1_right, fire_img2_right, fire_img3_right, fire_img4_right, fire_img5_right]
            
        self.image=self.imag_list[0]
        
        self.rect = self.image.get_rect(center = pos)
        self.index=0
        
    def animation(self):
        self.index +=0.5
        self.image=self.imag_list[int(self.index)]
        if self.index>len(self.imag_list)-1:
            self.kill()
    def update(self):
        self.animation()
        camera(self)

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos ,direction,self_type):
        super().__init__()  
        
        
        self.type=self_type
        self.image= ball
        self.rect = self.image.get_rect(center = pos)
        
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
   
    
        
    def destroy(self):
        if stone_wall_block_ball(self):
            ball_animation.add(Ball_animation((self.rect.x,self.rect.y)))
            self.kill()
        if self.rect.x > length+50 or self.rect.x < -50 or self.rect.y > width-50 or self.rect.y < 0:
            self.kill()
        
            
    def update(self):
        self.destroy()
        self.ball_movement()
 
class Tnt_explosion(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.explosion_image_list=[explosion_1, explosion_2, explosion_3, explosion_4, explosion_5, explosion_6, explosion_7, explosion_8]
        self.image = self.explosion_image_list[0]
        self.rect = self.image.get_rect(center = (x+20,y))
        self.index=0

    def animation(self):
        self.index +=0.2
        self.image=self.explosion_image_list[int(self.index)]
        if self.index>len(self.explosion_image_list)-0.5:
            self.kill()

    def update(self):
        self.animation()
        camera(self)
        #tnt_exploded()
       
class Tnt(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=tnt_image

      
        self.rect = self.image.get_rect(center = (x,y))
        
        self.rect.x=x
        self.rect.y=y
        
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
        camera(self)
        #tnt_exploded()
        self.animation()
        #self.explode()
        
class Ice_wall(pygame.sprite.Sprite):
    def __init__(self,x,y,direction):
        super().__init__()
        self.image = ice_image
        
        self.rect = self.image.get_rect(center = (x,y))
        
        
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
        camera(self)
        #self.movement()
        self.destroy()
        self.animation()
        
class Wood_wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.wood = wood
        self.image = self.wood
        self.rect = self.image.get_rect(center = (x,y))
        
        
        self.rect.x=x
        self.rect.y=y
        self.flag=""
        #self.visible=False

    def destroy(self):
        wood_wall_bomber()     
        
    

    def update(self):
        camera(self)

        self.destroy()
        
class Stone_wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.image = stone_wall_image
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x=x
        self.rect.y=y

        
        
    
    def update(self):
        camera(self)
        
class Trees_wall(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.image = trees_wall
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x=x
        self.rect.y=y
        
        
    
    def update(self):
        camera(self)
      
class Shield_stone_wall(pygame.sprite.Sprite):
    
    def __init__(self,pos):
        super().__init__()
        
        self.image = strong_wall
        
        self.rect=self.image.get_rect(center = (pos))
        
        self.resistance= 5
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
   
        
    def get_self_resistance(self):
        return self.resistance
        
    def dstroy (self):
        shield_stone_wall_block_balls()
    
       
    def update(self):
        self.dstroy()
        camera(self)
        
class Boss1(pygame.sprite.Sprite):
    def  __init__(self, pos):
        super().__init__()
        
        self.image=boss_img
        self.rect = self.image.get_rect(center = pos)
        self.direction=choice(["up","right","left","down"]) 
        self.move_time=0
        self.tank_speed=1
        self.shoot_time=0
        wall_kill(self)
        
    def dstroy(self):
        collided_balls = pygame.sprite.spritecollide(self, balls, False)
        for ball in collided_balls:
            if ball.type == "player_ball":
                key.add(Key((self.rect.x, self.rect.y), True))
                self.kill()
                break
    
    def time_to_move(self):
        self.move_time-=1
        
            
        if self.move_time<0:
            self.direction=choice(["up","right","down","left","smart_move","smart_move","smart_move","smart_move","smart_move","smart_move"])
            self.move_time=20
        
    
    def random_movw(self):
        
        # if enmey_stonr_block(self):
        #     if self.direction=="down":
        #         while  enmey_stonr_block(self):
        #             self.rect.y -=1
        #         self.direction="up"
                
        #     if self.direction=="up":
        #         while enmey_stonr_block(self):
        #             self.rect.y +=1
        #         self.direction="down"
                
        #     if self.direction=="right":
        #         while enmey_stonr_block(self):
        #             self.rect.x -=1
        #         self.direction="left"
                
        #     if self.direction=="left":
        #         while enmey_stonr_block(self):
        #             self.rect.x +=1
        #         self.direction="right"
    
        
        if self.direction=="down" :
            
            self.image = boss1_down
            self.rect.y+=self.tank_speed
            if enmey_stonr_block(self) :
                self.direction="up"
                
               
                self.rect.y-=1 
        
            # if self.rect.y>=width-110:
            #     self.rect.y-=1
            #     self.direction=choice(["right","left","up"])
                

        elif self.direction=="up" :
            
            self.image = boss1_up
            self.rect.y-=self.tank_speed
            if enmey_stonr_block(self) :
                self.direction="down"
                
               
                self.rect.y+=1
        
            # if self.rect.y<=0:
            #     self.rect.y+=1
            #     self.direction=choice(["down","right","left"])
            
                
            
        elif self.direction=="right":
            
            self.image = boss1_right
            self.rect.x+=self.tank_speed
            if enmey_stonr_block(self) :
                self.direction="left"
                
               
                self.rect.x-=1
        
            # if self.rect.x>=length-40:
            #     self.rect.x-=1
            #     self.direction=choice(["up","left","down"])
            
          
            
        elif self.direction=="left":
            
            self.image = boss1_left
            self.rect.x-=self.tank_speed
            
            if enmey_stonr_block(self) :
                self.direction="right"
                self.rect.x+=1
                
               
        
            # if self.rect.x<=0:
            #     self.rect.x+=1
                
            #     self.direction=choice(["up","right","down"])
            
    def time_to_shoot(self):
        self.shoot_time-=1;
        if self.shoot_time<0:
            
        
            if self.direction=="up":
                fire.add(Fire((self.rect.x+26,self.rect.y-100),self.direction))
            
            
            if self.direction=="down":
                fire.add(Fire((self.rect.x+26,self.rect.y+150),self.direction))
            
            if self.direction=="right":
                fire.add(Fire((self.rect.x+150,self.rect.y+26),self.direction))
            
            if self.direction=="left":
                fire.add(Fire((self.rect.x-100,self.rect.y+26),self.direction))
            self.shoot_time=40

    def update(self):
        camera(self)
        self.dstroy()
        self.time_to_shoot()
        
        self.time_to_move()
        self.random_movw()
        if self.direction == "smart_move":
            self.direction=smart_move(self)
            
class Enemy_tank(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        
        
        
        self.enemy_tank=enemy_image
        self.image = self.enemy_tank
        self.rect = self.image.get_rect(center = pos)
        self.direction=choice(["up"]) #,"right","left","down"
        self.direction_last=""
        self.tank_speed=1
        self.shoot_time=0
        self.move_time=0
        self.type="enemy"
        
    def time_to_shoot(self):
        self.shoot_time-=1
        if self.shoot_time<0:
            balls.add(Ball(self.rect.center,self.direction,"enemy_ball"))
            self.shoot_time=80
            self.direction=choice(["up","right","down","left","smart_move","smart_move","smart_move"])
            
    def time_to_move(self):
        self.move_time-=1
        
            
        if self.move_time<0:
            self.direction=choice(["up","right","down","left","smart_move","smart_move","smart_move"])
            self.move_time=40
            
    # def smart_move(self):
    #     if self.rect.x>tank.sprite.rect.x :
    #         if self.rect.y>tank.sprite.rect.y:
    #             self.direction = choice( ["up","left"])
            
    #         elif self.rect.y<tank.sprite.rect.y:
    #             self.direction = choice(["down","left"])
                
    #         else:
    #             self.direction = "left"
                
    #     if self.rect.x<tank.sprite.rect.x :
    #         if self.rect.y>tank.sprite.rect.y:
    #             self.direction = choice(["up", "right"])
    #         elif self.rect.y<tank.sprite.rect.y:
    #             self.direction = choice(["down","right"])
    #         else:
    #             self.direction = "right"

    def random_movw(self):
        # if enmey_stonr_block(self):
        #     if self.direction=="down":
        #         while  enmey_stonr_block(self):
        #             self.rect.y -=1
        #         self.direction="up"
                
        #     if self.direction=="up":
        #         while enmey_stonr_block(self):
        #             self.rect.y +=1
        #         self.direction="down"
                
        #     if self.direction=="right":
        #         while enmey_stonr_block(self):
        #             self.rect.x -=1
        #         self.direction="left"
                
        #     if self.direction=="left":
        #         while enmey_stonr_block(self):
        #             self.rect.x +=1
        #         self.direction="right"
    

        if self.direction=="down" :
            
            self.image = enemy_down
            self.rect.y+=self.tank_speed
            if enmey_stonr_block(self) :
                self.direction="up"
                
               
                self.rect.y-=1 
        
            # if self.rect.y>=width-110:
            #     self.rect.y-=1
            #     self.direction=choice(["right","left","up"])
                

        elif self.direction=="up" :
            
            self.image = enemy_up
            self.rect.y-=self.tank_speed
            if enmey_stonr_block(self) :
                self.direction="down"
                
               
                self.rect.y+=1
        
            # if self.rect.y<=0:
            #     self.rect.y+=1
            #     self.direction=choice(["down","right","left"])
            
                
            
        elif self.direction=="right":
            
            self.image = enemy_right
            self.rect.x+=self.tank_speed
            if enmey_stonr_block(self) :
                self.direction="left"
                
               
                self.rect.x-=1
        
            # if self.rect.x>=length-40:
            #     self.rect.x-=1
            #     self.direction=choice(["up","left","down"])
            
          
            
        elif self.direction=="left":
            
            self.image = enemy_left
            self.rect.x-=self.tank_speed
            
            if enmey_stonr_block(self) :
                self.direction="right"
                self.rect.x+=1
                
               
        
            # if self.rect.x<=0:
            #     self.rect.x+=1
                
            #     self.direction=choice(["up","right","down"])
    
    def dostroy(self):
        bollet_hit_enemy_tank()
            
    def freeze(self):
        self.enemy_tank=frozen_tank_image

        if self.direction_last =="left":
            self.image = enemy_frozen_left
            
        if self.direction_last =="up":
            self.image = enemy_frozen_up
            
        if self.direction_last =="down":
            self.image = enemy_frozen_down
            
        if self.direction_last =="right":
            self.image = enemy_frozen_right
     
    def update(self):
        
        
        

        camera(self)
        if self.direction == "freeze":
            self.freeze()
        else:
            self.enemy_tank=enemy_image
            self.time_to_shoot()
        if self.direction == "smart_move":
            self.direction=smart_move(self)
            
        self.random_movw()
        self.dostroy()
        self.time_to_move()
        
class Door(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.door=pygame.image.load('graphics/doors/door.jpg').convert_alpha()
        
        self.image =self.door
        self.rect = self.image.get_rect(center = (x,y))
        self.rect.x=x
        self.rect.y=y
        self.type_of_dor=True
        
    def dstroy(self):
        NULL
        # if flag_hit_from_ball():
        #     self.kill()
   
    def update(self):
        camera(self)   

class Key(pygame.sprite.Sprite):
    def __init__(self,pos,key_is_real):
        super().__init__()
        self.key = pygame.image.load('graphics/doors/key.png').convert_alpha()
        self.image=self.key
        self.rect= self.image.get_rect(center =(pos))
        
        self.key_is_real=key_is_real
    def key_is_geting(self):
        if pygame.sprite.spritecollide(self,tank,False):
            tank.sprite.key=False
            key.add(Key((length-300,width-40),False))
            self.kill()
            
    def update(self):
        self.key_is_geting()
        if self.key_is_real:
            camera(self)

class Star(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=star_
        self.rect = self.image.get_rect(center = pos)
        
        self.pos = pos
        wall_kill(self)
    
    def tank_out(self):
        if exit_space_is_empty(self):
            enemy_tank.add(Enemy_tank((self.rect.x+25,self.rect.y+25)))
 

            
    
    def update(self):
       
        camera(self)
    
class Ball_animation(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()

        self.boom_image = [boom_1, boom_2, boom_3, boom_4, boom_5, boom_6 ]
        self.animation_index = 0
        self.image= self.boom_image[self.animation_index]
        self.rect = self.image.get_rect(center = pos)
        
    def animation(self):
        self.animation_index+=0.5
        self.image= self.boom_image[int(self.animation_index)]
        
        if self.animation_index>=len(self.boom_image)-1:
            self.kill()
            
        
   
    def update(self):
        camera(self)
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
            


            
def smart_move(self):
    direction = choice( ["up","left","right","down"])
    if self.rect.x>tank.sprite.rect.x :
        if self.rect.y>tank.sprite.rect.y:
            direction = choice( ["up","left"])
            
        elif self.rect.y<tank.sprite.rect.y:
            direction = choice(["down","left"])
                
        else:
            direction = "left"
                
    if self.rect.x<tank.sprite.rect.x :
        if self.rect.y>tank.sprite.rect.y:
            direction = choice(["up", "right"])
        elif self.rect.y<tank.sprite.rect.y:
            direction = choice(["down","right"])
        else:
            direction = "right"
    return direction

      
def wall_kill(self_):
    
    shield= pygame.sprite.spritecollide(self_,shield_ston,False)
    for h in shield:
        h.kill()

    stone= pygame.sprite.spritecollide(self_,stone_wall,False)
    for s in stone:
        s.kill()

    wall= pygame.sprite.spritecollide(self_,wood_wall,False)
    for w in wall:
        w.kill()
            

max_x = length*2
min_x = length*-1
def camera(group): 
    
    #if tank.sprite.rect.x>300 and tank.sprite.rect.x <length-300:
    if tank.sprite.activ:
        
        #tank.sprite.tank_speed=2
        if tank.sprite.direction=="right":
            

            if group.rect.x>min_x:
                group.rect.x-=1
            else:
                tank.sprite.activ=False
                
            
        if tank.sprite.direction=="left" :
             
            
            if group.rect.x<max_x:
                group.rect.x+=1        
            else:
                tank.sprite.activ=False
    # else:
    #     tank.sprite.tank_speed=1
                
    if tank.sprite.type_=="player_blocked":
        if tank.sprite.direction=="left":
            group.rect.x-=1
            
        if tank.sprite.direction=="right":
            group.rect.x+=1
            
    

    # if tank.sprite.rest_pos:
    #     group.rect.x-=tank.sprite.rect.x
        


def stone_block(tank_self):
    
    if pygame.sprite.spritecollide(tank_self,door,False) and tank_self.key:
        return True
    
    if pygame.sprite.spritecollide(tank_self,ice_wall,False):
        return True
    if pygame.sprite.spritecollide(tank_self,tnt,False):
        return True
          
    if pygame.sprite.spritecollide(tank_self,stone_wall,False):
        return True
    

    if pygame.sprite.spritecollide(tank_self,wood_wall,False):
        return True
    
    if pygame.sprite.spritecollide(tank_self,enemy_tank,False):
        return True
   
    if pygame.sprite.spritecollide(tank_self,shield_ston,False):
        return True

   
    if pygame.sprite.spritecollide(tank_self,enemy_tank,False):
        return True
    
    if pygame.sprite.spritecollide(tank_self,enemy_boss1,False):
        return True
    else:
        return False
                                    
def bollet_hit_player(): 
    
    if pygame.sprite.spritecollide(tank.sprite,fire,False):
        for hert in heart:
            hert.kill()
            fire.empty()
            break
        return True
     
    for ball in balls:
         if ball.type=="enemy_ball":
              if pygame.sprite.spritecollide(ball,tank,False):
                    ball_animation.add(Ball_animation((ball.rect.x,ball.rect.y)))   
                    ball.kill()
                    
                    for hert in heart:
                        hert.kill()
                        break
                      

                    return True
     
    
    return False

def wood_wall_bomber():
    for f in fire:
        wood_boxs = pygame.sprite.spritecollide(f,wood_wall,False)
        for box in wood_boxs:
            box.kill()
        
        wood_boxs = pygame.sprite.spritecollide(f,shield_ston,False)
        for box in wood_boxs:
            box.kill()
            
    
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
            

 
def enmey_stonr_block(enemy_self):
    
   
        
    oter_enemy = enemy_tank.copy()
    
    
        
    oter_enemy.remove(enemy_self)
    if pygame.sprite.spritecollide(enemy_self,door,False):
        return True  
    if pygame.sprite.spritecollide(enemy_self,wood_wall,False):
        return True
    if pygame.sprite.spritecollide(enemy_self,stone_wall,False):
        return True
    if pygame.sprite.spritecollide(enemy_self,ice_wall,False):
        enemy_self.direction_last=enemy_self.direction

        enemy_self.direction = "freeze"
        
    if pygame.sprite.spritecollide(enemy_self,tnt,False):
        return True
            
    if pygame.sprite.spritecollide(enemy_self,shield_ston,False):
        return True
        
    if  pygame.sprite.spritecollide(enemy_self,oter_enemy,False) :    
        return True
    
    if  pygame.sprite.spritecollide(enemy_self,tank,False) :    
        return True
        
    return False
        
def bollet_hit_enemy_tank():
    
        
        
            
    
    for ball in balls:
        if ball.type=="player_ball":
            # if pygame.sprite.spritecollide(ball,enemy_boss1,False):
            #     key.add(Key(enemy_boss1.sprites.rect.x,enemy_boss1.sprites.rect.y,True))
            #     enemy_boss1.empty()
            enemy_tank_kill= pygame.sprite.spritecollide(ball,enemy_tank,False)
            
            for enemy in enemy_tank_kill:
                enemy.kill()
                ball_animation.add(Ball_animation((ball.rect.x,ball.rect.y)))
                ball.kill()
                return True
    return False       

def stone_wall_block_ball(self_ball):
    if pygame.sprite.spritecollide(self_ball,door,False):
        return True
    if pygame.sprite.spritecollide(self_ball,tnt,False):
        return True
    if pygame.sprite.spritecollide(self_ball,stone_wall,False):
        return True
    if pygame.sprite.spritecollide(self_ball,ice_wall,False):
        return True
    else:
         return False
    
def tnt_exploded():
    
    for tnt_bom in tnt_explosion:
        
        ice_explos = pygame.sprite.spritecollide(tnt_bom,ice_wall,False)

        for ice in ice_explos:
            ice.kill()
            
        wood_explos = pygame.sprite.spritecollide(tnt_bom,wood_wall,False)
        
        for explos in wood_explos:
            explos.kill()
            
        enemy_explos = pygame.sprite.spritecollide(tnt_bom,enemy_tank,False)
        
        for enemy in enemy_explos:
            enemy.kill()
            
        return len(enemy_explos)
       
    return 0
  
def imags():
    global explosion_1,explosion_2,explosion_3,explosion_4,explosion_5,explosion_6,explosion_7,explosion_8
    explosion_1 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_1.png'),(200,200)).convert_alpha()
    explosion_2 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_2.png'),(200,200)).convert_alpha()
    explosion_3 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_3.png'),(200,200)).convert_alpha()
    explosion_4 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_4.png'),(200,200)).convert_alpha()
    explosion_5 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_5.png'),(200,200)).convert_alpha()
    explosion_6 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_6.png'),(200,200)).convert_alpha()
    explosion_7 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_7.png'),(200,200)).convert_alpha()
    explosion_8 = pygame.transform.scale(pygame.image.load('graphics/explosion/explosion_8.png'),(200,200)).convert_alpha()

    global boom_1,boom_2,boom_3,boom_4,boom_5,boom_6,ball
    boom_1 = pygame.image.load('graphics/boom/boom_1.png').convert_alpha()
    boom_2 = pygame.image.load('graphics/boom/boom_2.png').convert_alpha()
    boom_3 = pygame.image.load('graphics/boom/boom_3.png').convert_alpha()
    boom_4 = pygame.image.load('graphics/boom/boom_4.png').convert_alpha()
    boom_5 = pygame.image.load('graphics/boom/boom_5.png').convert_alpha()
    boom_6 = pygame.image.load('graphics/boom/boom_6.png').convert_alpha()
    
    ball = pygame.image.load('graphics/weapons/ball.png').convert_alpha() 
    
    #wall
    global wood ,strong_wall ,trees_wall,stone_wall_image
    stone_wall_image = pygame.image.load('graphics/wall/Stone_wall.png').convert_alpha()
    wood = pygame.image.load('graphics/wall/wood.png')
    strong_wall = pygame.image.load('graphics/wall/strong_wall.jpg').convert_alpha()  
    trees_wall = pygame.image.load('graphics/wall/trees.png').convert_alpha()
    
    #weapons
    global fire_img1_left, fire_img2_left, fire_img3_left, fire_img4_left, fire_img5_left \
       , fire_img1_up , fire_img2_up,  fire_img3_up,  fire_img4_up,  fire_img5_up \
       , fire_img1_down , fire_img2_down,  fire_img3_down,  fire_img4_down,  fire_img5_down\
        , fire_img1_right , fire_img2_right,  fire_img3_right,  fire_img4_right,  fire_img5_right
    
    fire_img1_left = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_1.png'),90).convert_alpha()
    fire_img2_left = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_2.png'),90).convert_alpha()
    fire_img3_left = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_3.png'),90).convert_alpha()
    fire_img4_left = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_4.png'),90).convert_alpha()
    fire_img5_left = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_5.png'),90).convert_alpha()
    
    fire_img1_down = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_1.png'),180).convert_alpha()
    fire_img2_down = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_2.png'),180).convert_alpha()
    fire_img3_down = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_3.png'),180).convert_alpha()
    fire_img4_down = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_4.png'),180).convert_alpha()
    fire_img5_down = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_5.png'),180).convert_alpha()
    
    fire_img1_right = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_1.png'),270).convert_alpha()
    fire_img2_right = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_2.png'),270).convert_alpha()
    fire_img3_right = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_3.png'),270).convert_alpha()
    fire_img4_right = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_4.png'),270).convert_alpha()
    fire_img5_right = pygame.transform.rotate(pygame.image.load('graphics/weapons/fire/fire_5.png'),270).convert_alpha()
    

    fire_img1_up = pygame.image.load('graphics/weapons/fire/fire_1.png').convert_alpha()
    fire_img2_up = pygame.image.load('graphics/weapons/fire/fire_2.png').convert_alpha()
    fire_img3_up = pygame.image.load('graphics/weapons/fire/fire_3.png').convert_alpha()
    fire_img4_up = pygame.image.load('graphics/weapons/fire/fire_4.png').convert_alpha()
    fire_img5_up = pygame.image.load('graphics/weapons/fire/fire_5.png').convert_alpha()
    




    global tnt_image,ice_image
    tnt_image = pygame.transform.scale(pygame.image.load('graphics/weapons/tnt.jpg'),(50,50)).convert_alpha()
    ice_image = pygame.transform.scale(pygame.image.load('graphics/weapons/ice_wall.png'),(50,50)).convert_alpha()  


    global star_
    star_ =pygame.image.load("graphics/star/star.jpg").convert_alpha()
        
    #enemy
    global boss_img, boss1_left, boss1_up, boss1_down, boss1_right
    boss_img=pygame.image.load('graphics/enemy_tank/enemy_2_boss1/boss1.png').convert_alpha()
    boss1_left=pygame.transform.rotate(boss_img,90)
    boss1_up=pygame.transform.rotate(boss_img,0)
    boss1_down=pygame.transform.rotate(boss_img,180)
    boss1_right=pygame.transform.rotate(boss_img,270)



    global enemy_image,frozen_tank_image , enemy_up,enemy_right,enemy_down,enemy_left,enemy_frozen_up,enemy_frozen_right,enemy_frozen_down,enemy_frozen_left
    enemy_image = pygame.image.load('graphics/enemy_tank/enemy_tank.png').convert_alpha()
    frozen_tank_image = pygame.image.load('graphics/enemy_tank/frozen_tank.png').convert_alpha()
    
    enemy_left=pygame.transform.rotate(enemy_image,90)
    enemy_up=pygame.transform.rotate(enemy_image,0)
    enemy_down=pygame.transform.rotate(enemy_image,180)
    enemy_right=pygame.transform.rotate(enemy_image,270)
    
    
    enemy_frozen_left=pygame.transform.rotate(frozen_tank_image,90)
    enemy_frozen_up=pygame.transform.rotate(frozen_tank_image,0)
    enemy_frozen_down=pygame.transform.rotate(frozen_tank_image,180)
    enemy_frozen_right=pygame.transform.rotate(frozen_tank_image,270)
    
    
def door_is_open():
    
    if tank.sprite.key==False:
        if pygame.sprite.spritecollide(tank.sprite,door,False):
      
            return False
        return True
    else:
        return True
              
def exit_space_is_empty(self_): 
    if  pygame.sprite.spritecollide(self_,enemy_tank,False):
            
        return False
    return True
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

enemy_boss1 =pygame.sprite.Group()

door = pygame.sprite.Group()

key = pygame.sprite.Group()



tank = pygame.sprite.GroupSingle()

tank.add(Tank())

balls =pygame.sprite.Group()
fire =pygame.sprite.Group()


