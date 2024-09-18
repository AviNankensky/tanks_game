import pygame
from class_of_game import length, width
from Database_connection import *
from store import item, Item


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, text,  text_color=(0, 0, 0), font_size=24):
        super().__init__()
        self.text_color = text_color
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.game_activ = False
        self.type_ = text
        self.font = pygame.font.Font(None, font_size)
        self.click = False

    def drow(self):
        pygame.draw.rect(self.image, self.color, pygame.Rect(
            0, 0, self.width, self.height), border_radius=20)
        pygame.draw.rect(self.image, (105, 105, 105), pygame.Rect(
            0, 0, self.width, self.height), 4, border_radius=20)

    def text_(self):
        lines = self.text.split('\n')
        y_offset = self.height // 2
        for line in lines:
            text_surface = self.font.render(line, True, self.text_color)
            text_rect = text_surface.get_rect(
                center=(self.width // 2, y_offset))
            self.image.blit(text_surface, text_rect)
            y_offset += self.font.get_height()

    def hover(self):
        mous_pos = pygame.mouse.get_pos()
        if self.click == True:
            pygame.draw.rect(self.image, (20, 20, 184), pygame.Rect(
                0, 0, self.width, self.height), 5, border_radius=20)

        elif self.rect.collidepoint(mous_pos):

            pygame.draw.rect(self.image, (255, 255, 255), pygame.Rect(
                0, 0, self.width, self.height), 5, border_radius=20)

    def onclick(self):

        mous_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mous_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:

                for i in button:
                    if i.type_ != self.type_:
                        i.click = False
                self.click = True

                onclic_of_buttens(self)
                if self.type_ != "password" and self.type_ != "name":
                    self.click=False

    def SetText(self, NewText):
        self.text = NewText
        self.text_color = (0, 0, 0)

    def update(self):
        self.drow()
        self.onclick()
        self.text_()
        self.hover()


def onclic_of_buttens(self_btn):
    name_text = ""
    password_text = ""
    # error_text="Enter a username and password to log in or sing up"
    error_text = ""

    # מושך את הסיסמה והשם משתמש מהכפתורים
    for i in button:
        if i.type_ == "name":
            name_text = i.text
        if i.type_ == "password":
            password_text = i.text

    if self_btn.type_ == "log in":
        error_text += checks_input(name_text, password_text, "log in")
        # if len(error_text)==0:
        if checks_if_user_exists(name_text, password_text) and name_text != "name" and password_text!= "password":
            global data
            data.name = name_text
            data.password = password_text
            data.pull()
            screen_main("log in")
        else:
            error_text += "User not found"

    if self_btn.type_ == "sing up":
        error_text += checks_input(name_text, password_text, "sing up")


        if not chack_PlaerNameExist(name_text):
        # if error_text == "One or more of the details is incorrect ;" or len(error_text) == 0 or error_text == "The user ---- is already exists ;" or error_text == "the password ---- is not exists ;" or error_text == "One or more of the details is incorrect ;" or error_text == "the name ---- is not exists ;":
            error_text = "The user has successfully registered"
            adds_a_user(name_text, password_text)
            pygame.time.delay(1000)
        else:
            print("The user already exists;\n")
            error_text += f"The user '{name_text}' already exists;\n"

    

    # מזריק את הטקסט שגיאה למסך שגיאה
    for i in button:
        if i.type_ == "Enter a username and password to log in or sing up":
            i.text = error_text

    if self_btn.type_ == "shop":
        screen_main("shop")

    if self_btn.type_ == "log out":
        screen_main("start")

    if self_btn.type_ == "back":
        screen_main("log in")


    if self_btn.text == "guest":
        screen_main("guest")

    
    if self_btn.text == "Enter back":
        screen_main("log in")

    if self_btn.text == "enter":
        self_btn.game_activ = True

    if self_btn.text == "X":
        pygame.quit()
        exit()


def screen_main(type_):

    coler = (255, 0, 0)

    button.empty()
    item.empty()
    if type_ == "shop":

        button.add(Button(length-60, 10, 50, 50, (255, 0, 0), "X"))
        button.add(Button(10, 70, 200, 50, (255, 0, 0), "back"))

        item.add(Item((250, 200), "graphics/weapons/beeper.png", "beeper", 10))
        item.add(Item((500, 200), "graphics/heart.png", "heart", 30))
        item.add(Item((750, 200), "graphics/weapons/ice_wall.png", "ice", 3))

    if type_ == "start":
        button.add(Button(length-60, 10, 50, 50, (255, 0, 0), "X"))

        button.add(Button(length/2-150, 100, 400, 50,
                   coler, "name", (211, 211, 211)))

        button.add(Button(length/2-150, 200, 400, 50,
                   coler, "password", (211, 211, 211)))

        button.add(Button(length/2-150, 300, 100, 100, coler, "log in"))

        button.add(Button(length/2, 300, 100, 100, coler, "sing up"))

        if data.data_connect:
            button.add(Button(length/2+150, 300, 100, 100, coler, "Enter back"))
        else:
            button.add(Button(length/2+150, 300, 100, 100, coler, "guest"))

        button.add(Button(length/2-200, 500, 500, 150, (0, 0, 0),
                   "Enter a username and password to log in or sing up", (255, 255, 255)))

    if type_ == "guest":
        # global data
        adds_a_user("guest", "0")
        data.name = "guest"
        data.password = "0"
        data.pull()
        screen_main("log in")
    if type_ == "sing up" or type_ == "log in":
        button.add(Button(length-60, 10, 50, 50, (255, 0, 0), "X"))
        button.add(Button(10, 10, 200, 50, (255, 0, 0), "log out"))

        button.add(Button(length/2-50, 100, 200, 50, (255, 0, 0), "enter"))
        # button.add(Button(length/2-50, 200, 200, 50, (255, 0, 0), "exit"))
        button.add(Button(length/2-50, 300, 200, 50, (255, 0, 0), "shop"))

    if type_ == "guest screen":

        return True
    return False


button = pygame.sprite.Group()
