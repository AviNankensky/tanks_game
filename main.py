from asyncio.windows_events import NULL

import pygame
from sys import exit
from random import choice, randint
from tkinter import *
from class_of_game import *
from Database_connection import *
from Database_connection import Information, conn, data


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

    num_of_heart = data.heart
    pos_of_heart = [(375, width-40), (425, width-40), (475, width-40)]

    for i in range(data.heart):
        heart.add(Heart(pos_of_heart[i]))

    # while num_of_heart > 0:
    #     heart.add(Heart(pos_of_heart[num_of_heart-1]))
    #     num_of_heart -= 1
# else:
    door.add(Door(length*2-40, 300))

    # add....
    pixels()
    button.add(Button(300, 300, 200, 50, (255, 0, 0), "entnr"))
    # enemy in...

    if level_of_game == 1:
        background__ = pygame.transform.scale(pygame.image.load(
            'graphics/background/background_level_1.jpg'), (length, width)).convert_alpha()

    if level_of_game == 2:
        background__ = pygame.transform.scale(pygame.image.load(
            'graphics/background/background_level_2.webp'), (length, width)).convert_alpha()

    else:
        #  level_of_game == 3:
        background__ = pygame.transform.scale(pygame.image.load(
            'graphics/background/background_level_3.webp'), (length, width)).convert_alpha()

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
            elif c == 150 and (r == 150 or r == 1000 or r == 1500):
                star.add(Star((r, c)))
            elif r <= 150 and c <= 300 or r == 750 and c == 0 or c == 150 or (r == 0 and (c == 150 or c == 200 or c == 100) or r == 50 and (c == 100 or c == 150 or c == 200) or r > length*2-300 and c == 300):
                NULL

            else:
                if type_pixel == "bounses":
                    bounses.add(Bounse("heart", r, c))
                    print("test")

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
    score_surf = test_font.render(f'Score: {current_time}', False, (0, 0, 0))
    score_rect = score_surf.get_rect(center=(length-150, width-40))
    screen.blit(score_surf, score_rect)
    return current_time


def display_coin_cont():
    coin_surf = test_font.render(
        f'{data.coins} :', False, (0, 0, 0))  # Coin.cont #data.coins
    coin_rect = coin_surf.get_rect(center=(950, width-40))
    screen.blit(coin_surf, coin_rect)


def whell_of_elemnt_in_teh_game(level):
    current_time = display_score()
    if current_time % 5 == 0:
        if len(enemy_tank) < 2*level:

            for f in star:
                f.tank_out()

    if level == 1:

        if current_time % 20 == 0 and current_time != 0 and len(enemy_boss1) == 0:
            enemy_boss1.add(
                Boss1((randint(150, length-150), randint(150, width-150))))

    if level == 2:

        if current_time % 10 == 0 and current_time != 0 and len(enemy_boss1) == 0:
            enemy_boss1.add(
                Boss1((randint(150, length-150), randint(150, width-150))))


def display_inpo_under_line():
    screen.blit(background_line, (0, width-70))
    screen.blit(coin_img_, (870, width-55))
    display_coin_cont()
    screen.blit(ball_image, ball_rect)
    screen.blit(tnt_image, tnt_rect)
    screen.blit(ice_image, ice_rect)
    heart.draw(screen)


def move_tank_smoothly(tank_sprite, distance):
    if len(betweenStages) == 0:
        betweenStages.add(BetweenStages())
    move_speed = 20  # מהירות התזוזה בכל פריים
    for _ in range(distance // move_speed):
        tank_sprite.activ = True
        tank_sprite.direction = "right"

        # tank_sprite.rect.x -= 1
        # tank_sprite.rect.x += move_speed
        # tank.draw(screen)

        # all_sprites.draw(screen)  # צייר את כל הספרייטים
        # pygame.display.flip()  # עדכן את המסך
        # pygame.time.delay(30)  # השהייה קצרה בין כל תזוזה


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()
pygame.display.set_caption('Tanks')
test_font = pygame.font.Font('font/OpenSans-Regular-webfont.woff', 50)
star_x = 775

imags()


Background_start = pygame.transform.scale(pygame.image.load(
    'graphics/Background_AI.jpeg'), (length, width)).convert_alpha()


Background_end = pygame.transform.scale(pygame.image.load(
    'graphics/background_end.png'), (length, width)).convert_alpha()


background_line = pygame.transform.scale(pygame.image.load(
    'graphics/background_line.jpg'), (length, 70)).convert_alpha()

coin_img_ = pygame.image.load("graphics/coin.png").convert_alpha()


# buttons
ball_image = pygame.transform.scale(pygame.image.load(
    'graphics/weapons/ball_image.jpg'), (40, 40)).convert_alpha()
ball_rect = ball_image.get_rect(center=(75, width-40))

ice_image = pygame.transform.scale(pygame.image.load(
    'graphics/weapons/ice_wall.png'), (40, 40)).convert_alpha()
ice_rect = ice_image.get_rect(center=(175, width-40))

tnt_image = pygame.transform.scale(pygame.image.load(
    'graphics/weapons/tnt.jpg'), (40, 40)).convert_alpha()
tnt_rect = tnt_image.get_rect(center=(275, width-40))


button_type = "play"
play_image = pygame.image.load('graphics/buttons/play_2.png').convert_alpha()
play_rect = play_image.get_rect(center=(length/2, width/2-200))


exit_image = pygame.image.load('graphics/buttons/exit_1.png').convert_alpha()
exit_rect = exit_image.get_rect(center=(length/2, width/2-50))


# timers
betweenLevelsOfGame = 0

enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 3000)

# background
name_text = ""
# level=1
# sutfes_level= pygame.Surface((width,length),pygame.SRCALPHA)
# pygame.draw.rect(sutfes_level,(128,128,128,180),(100,100,300,300))
screen_main("start")

while True:
    # print(game_active)

    whell_of_elemnt_in_teh_game(data.level)
    if bollet_hit_enemy_tank():
        outcome_of_enemy_tanks += 1

    op = tnt_exploded()
    if op > 0:
        outcome_of_enemy_tanks += op

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # # data.push()
            screen_2 = False
            if event.type == pygame.KEYDOWN:
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

                    if weapon_type == 'ice':

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

                    if event.type == pygame.KEYDOWN:
                        if i.text == i.type_:
                            i.text = " "
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

            # if button_type=="screen 2":
            #     button_type="play"
            # start_time = int(pygame.time.get_ticks() / 1000)
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_DOWN:
            #         #rect = pygame.draw.rect(screen,'black',exit_rect,40)
            #         button_type="exit"
            #         exit_image=pygame.image.load('graphics/buttons/exit_2.png').convert_alpha()
            #         play_image=pygame.image.load('graphics/buttons/play_1.png').convert_alpha()

            #     if event.key == pygame.K_UP:
            #         button_type="play"

            #         exit_image=pygame.image.load('graphics/buttons/exit_1.png').convert_alpha()
            #         play_image=pygame.image.load('graphics/buttons/play_2.png').convert_alpha()

            #     if score > 0  and screen_2== False:
            #         button_type ="screen 2"

            #     if  event.key == pygame.K_SPACE  :

            #         if button_type =="screen 2":
            #             screen_2 = True

            #         if button_type=="play":

            #             game_active=True

            #             outcome_of_enemy_tanks=0
            #             #num_enemy_tank=5
            #             reset_game(1)

            #         if button_type=="exit":
            #             pygame.quit()
            #             exit()

    if game_active:

        if door_is_open() or betweenLevelsOfGame != 0:
            betweenLevelsOfGame += 1
            if betweenLevelsOfGame == length:
                betweenLevelsOfGame = 0

            tank_sprite = tank.sprite
            move_tank_smoothly(tank_sprite, length)

        # if door_is_open() :

        #     data.level += 1
        #     data.push()
        #     print(data.level, "00000000000000000000000000000000000000000000000000000")
        #     reset_game(data.level)
        betweenStages.draw(screen)
        betweenStages.update()

        bounses.draw(screen)

        background.draw(screen)
        background.update()

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
        x = tank.sprite.rect.x
        # if door_is_open()==False:
        #     tank.sprite.activ = False
        #     while(tank.sprite.rect.x>x-50):

        #         tank.sprite.rect.x-=0.5
        #     game_active=door_is_open()
        # else:
        #     tank.sprite.activ = True
        # game_active=door_is_open() #flag_hit_from_ball()

        screen.blit(background_line, (0, width-70))
        screen.blit(coin_img_, (870, width-55))
        tank.draw(screen)
        tank.update()

        coin.draw(screen)
        coin.update()

        key.draw(screen)
        key.update()

        screen.blit(ball_image, ball_rect)
        screen.blit(tnt_image, tnt_rect)
        screen.blit(ice_image, ice_rect)
        heart.draw(screen)
        score = display_score()
        display_coin_cont()
        if weapon_type == 'ball':
            pygame.draw.rect(screen, (0, 0, 0), ball_rect, 4)
        if weapon_type == 'ice':
            pygame.draw.rect(screen, (0, 0, 0), ice_rect, 4)
        if weapon_type == 'tnt':
            pygame.draw.rect(screen, (0, 0, 0), tnt_rect, 4)
        # screen.blit(Rect)

        if not heart:
            game_active = False

        # screen.blit(sutfes_level,(0,0))
        # game_active=door_is_open()

    else:
        level = 1
        # background.empty()
        # door.empty()
        # key.empty()
        # enemy_boss1.empty()

        if score == 0 or screen_2:
            # print(data.data_connect,"uuuuuuuuuuuuuuuuuuuuuuuu")
            screen.blit(Background_start, (0, 0))
            button.draw(screen)
            button.update()
            # if :
            #     game_active = True
            # screen.blit(play_image,play_rect)

            # screen.blit(exit_image,exit_rect)
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
