import pygame
from Database_connection import data


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, name, price):
        super().__init__()
        self.image = pygame.Surface([200, 300], pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)
        self.image_ = pygame.image.load(image_path).convert_alpha()
        self.product_image = pygame.transform.scale(self.image_, (180, 180))
        self.font = pygame.font.Font(None, 24)
        self.name = name
        self.price = price
        self.increase_button = SimpleButton(
            (110, 230), 'buy', self.increase_quantity, self.image, pos)
        self.notEnough = False
        self.draw()

    def draw(self):
        pygame.draw.rect(self.image, (240, 240, 240),
                         pygame.Rect(0, 0, 200, 300), border_radius=15)
        self.image.blit(self.product_image, (10, 10))

        name_text = self.font.render(self.name, True, (0, 0, 0))
        price_text = self.font.render(f"Price: {self.price}$", True, (0, 0, 0))
        erorr_text = self.font.render(f"Not enough: ", True, (255, 0, 0))

        if self.notEnough:
            self.image.blit(erorr_text, (10, 260))

        self.image.blit(name_text, (10, 200))
        self.image.blit(price_text, (10, 240))

        self.increase_button.draw()

    def update(self):
        self.increase_button.update()
        self.draw()

    def increase_quantity(self):
        self.updateTehSErver()

    def updateTehSErver(self):
        if self.name == "heart":
            if data.coins > 29:
                data.heart += 1
                data.coins -= 30
            else:
                self.notEnough = True

        elif self.name == "ice":
            if data.coins > 2:
                data.shopDate.ice += 1
                data.coins -= 3
            else:
                self.notEnough = True

        elif self.name == "TNT":
            if data.coins > 9:
                data.shopDate.tnt += 1
                data.coins -= 10
            else:
                self.notEnough = True

        data.shopDate.push()
        data.push()


class SimpleButton(pygame.sprite.Sprite):
    def __init__(self, pos, text, callback, surface, item_pos):
        super().__init__()
        self.width = 50
        self.height = 50
        self.surface = surface
        self.image = pygame.Surface([self.height, self.width], pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)
        self.text = text
        self.callback = callback
        self.item_pos = item_pos
        self.font = pygame.font.Font(None, 24)
        self.click = False
        self.draw()

    def draw(self):
        pygame.draw.rect(self.image, (0, 51, 102), pygame.Rect(
            0, 0, self.height, self.width), border_radius=10)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(self.height/2, self.width/2))
        self.image.blit(text_surf, text_rect)

        self.hover()
        self.surface.blit(self.image, self.rect)

    def hover(self):
        button_pos = (
            self.rect.x + self.item_pos[0], self.rect.y + self.item_pos[1])
        mous_pos = pygame.mouse.get_pos()
        if pygame.Rect(button_pos, self.rect.size).collidepoint(mous_pos):
            pygame.draw.rect(self.image, (212, 175, 55), pygame.Rect(
                0, 0, self.height, self.width), 5, border_radius=10)


    def onclick(self):
        mous_pos = pygame.mouse.get_pos()
        button_pos = (
            self.rect.x + self.item_pos[0], self.rect.y + self.item_pos[1])
        if pygame.Rect(button_pos, self.rect.size).collidepoint(mous_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.callback()
                self.click = True
                pygame.time.wait(300)

    def update(self):
        self.draw()
        self.onclick()


item = pygame.sprite.Group()
simpleButton = pygame.sprite.Group()
