from asyncio.windows_events import NULL

import pygame
from sys import exit
from random import choice, randint
from tkinter import *
from class_of_game import *
from Database_connection import *
from Database_connection import Information, conn, data
from BetweenStages import *
from store import item , Item ,simpleButton
from menu import screen_main , button 
win = Tk()
win.geometry("650x250")
width = win.winfo_screenheight()
length = win.winfo_screenwidth()
outcome_of_enemy_tanks = 0
start_time = 0
score = 0
weapon_type = 'ball'
weapon_list = ["ball", "ice", "tnt"]
weapon_index = 0

game_active = False

screen_2 = False


def star_block():
    for enemy in enemy_tank:
        if enemy.rect.x > 650 and enemy.rect.x < 950 and enemy.rect.y < 150:

            return False
    else:
        return True


def ice_wall_bomber():
    for enemy in enemy_tank:
        if pygame.sprite.spritecollide(enemy, ice_wall, False):
            enemy.kill()


def flag_hit_from_ball():
    for ball in balls:
        if pygame.sprite.spritecollide(ball, door, False):

            return False
    else:
        return True


def reset_game(level_of_game):
    mysteriousBox.empty()
    heart.empty()
    background.empty()
    ice_wall.empty()
    trees_wall.empty()
    wood_wall.empty()
    stone_wall.empty()
    shield_ston.empty()
    enemy_tank.empty()
    balls.empty()
    fire.empty()
    star.empty()
    enemy_boss1.empty()
    key.empty()
    door.empty()
    # Tank.pos_rest_flag = True
    Tank.flag = True

    Tank.cont_movment = 0

    # hart

    # if level_of_game==1:
    if len(tank) == 0:
        tank.add(Tank())
    tank.sprite.rect.x = 60
    tank.sprite.rect.y = 150
    tank.sprite.key = False

    # Coin.cont=0
    display_inpo_under_line()
  
    door.add(Door(length*2-40, 300))

    # add....
    pixels()
  

    background__ = pygame.image.load('graphics/background/backgroun_d_level_1.jpg').convert_alpha()
    if level_of_game == 1:
        background__ = pygame.image.load('graphics/background/backgroun_d_level_1.jpg').convert_alpha()
            

    if level_of_game == 2:
        background__ = pygame.image.load(
            'graphics/background/background_level_2.webp').convert_alpha()

    
    if level_of_game == 3:
        background__ = pygame.image.load(
            'graphics/background/background_level_3.webp').convert_alpha()
    # background
    background.add(Background((0, 0), background__))
    background.add(Background((length, 0), background__))

    # heart


def pixels():
    for r in range(0, length*2, 50):   # 800
        for c in range(0, width-50, 50):  # 400
            type_pixel = choice(['stone', 'shield_stone', 'wood',
                                "empty", 'trees', 'wood', 'wood', "empty", "", "", ""])

            if c == 0 or c > width-125 or r == 0 and c != 150 or r == 50 and c != 150 or r == 100 and c != 150 or r > length*2-150 and c != 300:
                stone_wall.add(Stone_wall(r, c))
            elif c == 250 and (r == 250 or r == 1000 or r == 1500 or r == 2000):
                star.add(Star((r, c)))
            elif r <= 150 and c <= 300 or r == 750 and c == 0 or c == 150 or (r == 0 and (c == 150 or c == 200 or c == 100) or r == 50 and (c == 100 or c == 150 or c == 200) or r > length*2-300 and c == 300):
                NULL

            else:
                if type_pixel == "bounses":
                    bounses.add(Bounse("heart", r, c))


                if type_pixel == "empty":
                    NULL

                if type_pixel == 'stone':
                    stone_wall.add(Stone_wall(r, c))

                if type_pixel == 'trees':
                    trees_wall.add(Trees_wall(r, c))

                if type_pixel == 'wood':
                    wood_wall.add(Wood_wall(r, c))
                if type_pixel == 'shield_stone':
                    shield_ston.add(Shield_stone_wall((r, c)))


def display_score():

    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = pygame.font.Font(None, 60).render(f'Score: {current_time}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(center=(length-120, 25))
    screen.blit(score_surf, score_rect)
    return current_time


def display_coin_cont():
    coin_surf = test_font.render(
        f' {data.coins}', False, (0, 0, 0))  
    coin_rect = coin_surf.get_rect(center=(950, width-50))
    screen.blit(coin_surf, coin_rect)


def whell_of_elemnt_in_teh_game(level):
    current_time = display_score()
    if current_time % 5 == 0:
        if len(enemy_tank) < 2*level:

            for f in star:
                f.tank_out()
    # if not door_is_open():
    if level == 1:

        if current_time % 20 == 0 and current_time != 0 and len(enemy_boss1) == 0:
            enemy_boss1.add(
                Boss1((randint(150, length-150), randint(150, width-150))))

    if level == 2:

        if current_time % 10 == 0 and current_time != 0 and len(enemy_boss1) == 0:
            enemy_boss1.add(
                Boss1((randint(150, length-150), randint(150, width-150))))


def display_inpo_under_line():
    ball_text = test_font.render('-', False, (0, 0, 0))
    tnt_text = test_font.render(f'{data.shopDate.tnt}', False, (0, 0, 0))
    ice_text = test_font.render(f'{data.shopDate.ice}', False, (0, 0, 0))
    harte_text = test_font.render(f'{data.heart}', False, (0, 0, 0))
    coin_num = test_font.render( f' {data.coins}', False, (0, 0, 0)) 
        
    coin_num = test_font.render( f' {data.coins}', False, (0, 0, 0)) 
    
    #display under_line
    screen.blit(background_line, (0, width-70))

    screen.blit(coin_img_, (length-170, width-60))
    screen.blit(coin_num, (length-140,width-75))

    # displayHearts()


    screen.blit(ball_image, ball_rect)
    screen.blit(ball_text, (100, width-75))

    screen.blit(ice_image, ice_rect)
    screen.blit(ice_text, (180, width-75))

    screen.blit(tnt_image, tnt_rect)
    screen.blit(tnt_text, (310, width-75))

    
    screen.blit(harte_image, harte_rect)
    screen.blit(harte_text, (500, width-75))

    # heart.draw(screen)


pygame.init()
# screen = pygame.display.set_mode((length,width))
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()
pygame.display.set_caption('Tanks')
test_font = pygame.font.Font('font/rexlia rg.otf', 50)
star_x = 775

imags()


Background_start = pygame.transform.scale(pygame.image.load(
    'graphics/Background_AI.jpeg'), (length, width)).convert_alpha()


# Background_end = pygame.transform.scale(pygame.image.load(
#     'graphics/background_end.png'), (length, width)).convert_alpha()


background_line = pygame.transform.scale(pygame.image.load(
    'graphics/background_line.jpg'), (length, 70)).convert_alpha()

coin_img_ = pygame.image.load("graphics/coin.png").convert_alpha()


# buttons
ball_image = pygame.transform.scale(pygame.image.load(
    'graphics/weapons/ball_image.jpg'), (40, 40)).convert_alpha()
ball_rect = ball_image.get_rect(center=(75, width-40))

ice_image = pygame.transform.scale(pygame.image.load(
    'graphics/weapons/ice_wall.png'), (40, 40)).convert_alpha()
ice_rect = ice_image.get_rect(center=(150, width-40))

tnt_image = pygame.transform.scale(pygame.image.load(
    'graphics/weapons/tnt.jpg'), (40, 40)).convert_alpha()
tnt_rect = tnt_image.get_rect(center=(285, width-40))

harte_image = pygame.transform.scale(pygame.image.load(
    'graphics/heart.png'), (40, 40)).convert_alpha()
harte_rect = harte_image.get_rect(center=(455, width-40))


# timers
betweenLevelsOfGame = 0
betweenLevels=False
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 3000)

name_text = ""
screen_main("start")

while True:


    if bollet_hit_enemy_tank():
        outcome_of_enemy_tanks += 1

    num_of_enemy_has_killed = tnt_exploded()
    if num_of_enemy_has_killed > 0:
        outcome_of_enemy_tanks += num_of_enemy_has_killed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            whell_of_elemnt_in_teh_game(data.level)
            # # data.push()
            screen_2 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    screen_2=True
                    game_active=False
                if event.key == pygame.K_1:
                    weapon_type = weapon_list[0]
                    weapon_index = -1

                if event.key == pygame.K_2:
                    weapon_type = weapon_list[1]
                    weapon_index = -1

                if event.key == pygame.K_3:
                    weapon_type = weapon_list[2]
                    weapon_index = -1

                if event.key == pygame.K_LALT:
                    if weapon_index == len(weapon_list)-1:
                        weapon_index = 0
                        weapon_type = weapon_list[weapon_index]
                    else:
                        weapon_index += 1
                        weapon_type = weapon_list[weapon_index]

                if event.key == pygame.K_SPACE:

                    if weapon_type == "ball":
                        balls.add(Ball(tank.sprite.rect.center,
                                  tank.sprite.direction, "player_ball"))
                        # tank_backpack.play()

                    if weapon_type == 'ice':

                        if data.shopDate.ice != 0:
                            
                            data.shopDate.ice-=1
                            data.shopDate.push()

                            if tank.sprite.direction == "right":
                                ice_wall.add(
                                    Ice_wall(tank.sprite.rect.x+50, tank.sprite.rect.y, "right"))

                            if tank.sprite.direction == "left":
                                ice_wall.add(
                                    Ice_wall(tank.sprite.rect.x-50, tank.sprite.rect.y, "left"))

                            if tank.sprite.direction == "down":
                                ice_wall.add(
                                    Ice_wall(tank.sprite.rect.x, tank.sprite.rect.y+50, "down"))

                            if tank.sprite.direction == "up":
                                ice_wall.add(
                                    Ice_wall(tank.sprite.rect.x, tank.sprite.rect.y-50, "up"))

                    if weapon_type == "tnt":
                        if data.shopDate.tnt != 0:
                            data.shopDate.tnt -=1
                            data.shopDate.push()
                            if tank.sprite.direction == "right":
                                tnt.add(Tnt(tank.sprite.rect.x +
                                        50, tank.sprite.rect.y))

                            if tank.sprite.direction == "left":
                                tnt.add(Tnt(tank.sprite.rect.x -
                                        50, tank.sprite.rect.y))

                            if tank.sprite.direction == "down":
                                tnt.add(Tnt(tank.sprite.rect.x,
                                        tank.sprite.rect.y+50))

                            if tank.sprite.direction == "up":
                                tnt.add(Tnt(tank.sprite.rect.x,
                                        tank.sprite.rect.y-50))

        else:

            for i in button:
                if i.click:
                    if i.type_ == "password" or i.type_ == "name":
                        if event.type == pygame.KEYDOWN:
                            if i.text == i.type_:
                                i.text = ""
                            input_text = i.text
                            if event.key == pygame.K_BACKSPACE and len(input_text) != 0:
                                input_text = input_text[:-1]
                            else:
                                input_text += event.unicode
                            i.SetText(input_text)

                            i.update()
                            break

            for i in button:

                if i.game_activ:
                    reset_game(data.level)
                    game_active = True
                    i.game_activ = False


    if game_active:



        if betweenLevels and betweenLevelsOfGame == 0:

            if len(mysteriousBox)==0:
                betweenLevels=False
                data.level += 1
                data.push()
                reset_game(data.level)

        if door_is_open() and betweenLevelsOfGame==0:
            background.add(Background((length, 0), background_img))
            printFrameWithLevel(length+200, 100, data.level)  # יציג מסגרת עם "LEVEL" ומספר 2 בתוכה, החל מהנקודה (100, 100)
            # printDiamondWithMysteriousBox(length+500, 200)
            # printNumWhitMysteriousBox(data.level, length+200, 200)

        if door_is_open() or betweenLevelsOfGame != 0:
            betweenLevels=True
            betweenLevelsOfGame += 1

            tank_sprite = tank.sprite
            changing_screen_smoothly(tank_sprite)

            if betweenLevelsOfGame == length:
                betweenLevelsOfGame = 0
                tank.sprite.key = False


        background.draw(screen)
        background.update()


        mysteriousBox.draw(screen)
        mysteriousBox.update()

        bounses.draw(screen)


        star.draw(screen)
        star.update()

        enemy_tank.draw(screen)
        enemy_tank.update()

        enemy_boss1.draw(screen)
        enemy_boss1.update()

        trees_wall.draw(screen)
        trees_wall.update()

        balls.draw(screen)
        balls.update()

        ball_animation.draw(screen)
        ball_animation.update()

        fire.draw(screen)
        fire.update()

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
        
        coin.draw(screen)
        coin.update()

        screen.blit(pygame.font.Font(None, 60).render( "Press X to exit", False, (0, 0, 0)), (100,0))

        display_inpo_under_line()
        tank.draw(screen)
        tank.update()


        key.draw(screen)
        key.update()

        screen.blit(ball_image, ball_rect)
        screen.blit(tnt_image, tnt_rect)
        screen.blit(ice_image, ice_rect)
        screen.blit(harte_image,harte_rect)
        heart.draw(screen)

        score = display_score()
        if weapon_type == 'ball':
            pygame.draw.rect(screen, (0, 0, 0), ball_rect, 4)
        if weapon_type == 'ice':
            pygame.draw.rect(screen, (0, 0, 0), ice_rect, 4)
        if weapon_type == 'tnt':
            pygame.draw.rect(screen, (0, 0, 0), tnt_rect, 4)


    else:
        level = 1


        if score == 0 or screen_2:
            screen.blit(Background_start, (0, 0))
            button.draw(screen)
            button.update()
            
            item.draw(screen)
            item.update()
            
        else:
            screen.fill((0, 0, 0))
            screen.blit(Background_end, (50, 20))
            outcome_of_enemy = test_font.render(
                f'Enemy tanks: {outcome_of_enemy_tanks}', False, (255, 255, 255))
            screen.blit(outcome_of_enemy, (length/2-200, width/2-50))

            enemy_tank_image = pygame.transform.scale(pygame.image.load(
                'graphics/enemy_tank/enemy_tank.png'), (80, 80)).convert_alpha()

            screen.blit(enemy_tank_image, (length/2+200, width/2-50))

        if data.data_connect:
            display_inpo_under_line()

    pygame.display.update()
    clock.tick(60)
