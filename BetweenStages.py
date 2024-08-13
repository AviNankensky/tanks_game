import pygame
from class_of_game import camera, length, width, mysteriousBox, balls, coin, Coin, ball_animation, Ball_animation, stone_wall, Stone_wall, key, Background, background
from Database_connection import data


class BetweenStages(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.img = pygame.image.load('graphics/background7.jpg')

        self.img = pygame.transform.scale(self.img, (length, width))

        self.rect = self.img.get_rect(topleft=(length, 0))

        self.image = self.img

    def update(self):
        camera(self)


class MysteriousBox(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.box = mysterious_box_img
        self.image = self.box
        self.rect = self.image.get_rect(center=(x, y))

        self.rect.x = x
        self.rect.y = y

    def destroy(self):
        for ball in balls:
            if ball.type == "player_ball":
                if pygame.sprite.spritecollide(ball, [self], False):

                    ball_animation.add(Ball_animation(
                        (ball.rect.x, ball.rect.y)))
                    coin.add(Coin((self.rect.x, self.rect.y)))
                    ball.kill()
                    self.kill()

    def update(self):
        camera(self)

        self.destroy()


def printNumWhitMysteriousBox(num, x, y):

    for r in range(length, length*2, 50):   # 800
        stone_wall.add(Stone_wall(r, width-100))
        stone_wall.add(Stone_wall(r, 0))

    for c in range(0, width, 50):
        stone_wall.add(Stone_wall(length*2 - 50, c))

    startPointX = x
    startPointY = y
    if num == 1:

        mysteriousBox.add(MysteriousBox(startPointX, startPointY+100))
        mysteriousBox.add(MysteriousBox(startPointX, startPointY+300))
        mysteriousBox.add(MysteriousBox(startPointX+50, startPointY+50))
        mysteriousBox.add(MysteriousBox(startPointX+50, startPointY+300))
        for i in range(0, 350, 50):
            mysteriousBox.add(MysteriousBox(startPointX+100, startPointY+i))
        mysteriousBox.add(MysteriousBox(startPointX+150, startPointY+300))
        mysteriousBox.add(MysteriousBox(startPointX+200, startPointY+300))
        mysteriousBox.add(MysteriousBox(startPointX+100, startPointY+300))
    if num == 2:
        mysteriousBox.add(MysteriousBox(startPointX+50, startPointY+0))
        mysteriousBox.add(MysteriousBox(startPointX+100, startPointY+0))
        mysteriousBox.add(MysteriousBox(startPointX+150, startPointY+0))
        mysteriousBox.add(MysteriousBox(startPointX+0, startPointY+50))
        mysteriousBox.add(MysteriousBox(startPointX+200, startPointY+50))
        mysteriousBox.add(MysteriousBox(startPointX+200, startPointY+100))
        mysteriousBox.add(MysteriousBox(startPointX+100, startPointY+150))
        mysteriousBox.add(MysteriousBox(startPointX+150, startPointY+150))
        mysteriousBox.add(MysteriousBox(startPointX+50, startPointY+200))
        mysteriousBox.add(MysteriousBox(startPointX+0, startPointY+250))
        for i in range(0, 250, 50):
            mysteriousBox.add(MysteriousBox(startPointX+i, startPointY+250))


# global cont
# cont = 0


def changing_screen_smoothly(tank_sprite):
    key.empty()

    # global cont
    # if cont == 0:

    #     cont += 1
    #     background.add(Background((length, 0), background_img))
    #     printNumWhitMysteriousBox(data.level, length+300, 200)

    tank_sprite.activ = True
    tank_sprite.direction = "right"
    tank_sprite.rect.x -= 1


mysterious_box_img = pygame.image.load(
    'graphics/wall/mysterious_box.png').convert_alpha()
background_img = pygame.image.load(
    'graphics/wall/wood.png').convert_alpha()


betweenStages = pygame.sprite.Group()
