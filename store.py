import pygame
from Database_connection import data


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, name, price):
        super().__init__()
        # Create a transparent surface with a defined size
        self.image = pygame.Surface([200, 300], pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)

        # Load and scale the product image
        self.product_image = pygame.image.load(image_path).convert_alpha()
        self.product_image = pygame.transform.scale(self.product_image, (180, 180))

        # Font for the text
        self.font = pygame.font.Font(None, 24)

        # Set the name and price
        self.name = name
        self.price = price
        self.quantity = 1 


        # Create buttons
        # self.increase_button = SimpleButton((110, 250), '+', self.increase_quantity, self.image)
        # self.decrease_button = SimpleButton((160, 250), '-', self.decrease_quantity, self.image)
        self.increase_button = SimpleButton((110, 250), '+', self.increase_quantity, self.image, pos)
        self.decrease_button = SimpleButton((160, 250), '-', self.decrease_quantity, self.image, pos)
        # ...
        # Draw the initial appearance of the item
        self.draw()

    def draw(self):
        # Draw the background rectangle
        pygame.draw.rect(self.image, (240, 240, 240), pygame.Rect(0, 0, 200, 300), border_radius=15)

        # Draw the product image
        self.image.blit(self.product_image, (10, 10))

        # Render the name and price text
        name_text = self.font.render(self.name, True, (0, 0, 0))
        price_text = self.font.render(f"Price: {self.price}$", True, (0, 0, 0))
        quantity_text = self.font.render(f"Quantity: ", True, (0, 0, 0))
        quantity_num = self.font.render(f"{self.quantity}", True, (0, 0, 0))

        # Position the text below the image
        self.image.blit(name_text, (10, 200))
        self.image.blit(price_text, (10, 240))
        self.image.blit(quantity_text, (10, 260))
        self.image.blit(quantity_num, (143, 260))

        # Draw the buttons
        self.increase_button.draw()
        self.decrease_button.draw()

    def update(self):
        # Update buttons based on events
        self.increase_button.update()
        self.decrease_button.update()
        # self.decrease_button.update(event_list)

        # Redraw the item to update quantity display
        self.draw()

    def increase_quantity(self):
        self.quantity += 1
        self.draw()
        self.updateTehSErver()

    def decrease_quantity(self):
        if self.quantity > 1:
            self.quantity -= 1
            self.draw()
            self.updateTehSErver()

    def updateTehSErver(self):
        if self.name == "heart":
            if data.coins >29 :
                data.heart+=1
                data.coins-=30
        elif self.name == "ice":
            if data.coins > 2:
                data.shopDate.ice+=1
                data.coins-=3
        elif self.name == "tnt":
            if data.coins > 9:
                data.shopDate.tnt+=1
                data.coins-=10

        print(f"data stor name{data.shopDate.playerName}")
        data.shopDate.push()
        data.push()



class SimpleButton(pygame.sprite.Sprite):
    def __init__(self, pos, text, callback ,surface,item_pos):
        super().__init__()
        self.surface = surface
        self.image = pygame.Surface([30, 30], pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)
        self.text = text
        self.callback = callback
        self.item_pos = item_pos
        # Font for the text
        self.font = pygame.font.Font(None, 24)

        # Draw the initial button appearance
        self.draw()

    def draw(self):
        # Draw the button rectangle
        pygame.draw.rect(self.image, (0, 0, 255), pygame.Rect(0, 0, 30, 30), border_radius=10)
        # pygame.draw.rect(self.image, (255, 255, 255), pygame.Rect(0, 0, 30, 30), 5, border_radius=10)
        
        # Render the button text
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=(15, 15))
        self.image.blit(text_surf, text_rect)

        # Optionally draw on an external surface
        
        self.surface.blit(self.image, self.rect)

    def hover(self):
        mous_pos = pygame.mouse.get_pos()
        button_pos = (self.rect.x + self.item_pos[0], self.rect.y + self.item_pos[1])
        if pygame.Rect(button_pos, self.rect.size).collidepoint(mous_pos):
            pygame.draw.rect(self.image, (255, 255, 255), pygame.Rect(0, 0, 30, 30), 5, border_radius=10)
            
            

    def onclick(self):
        mous_pos = pygame.mouse.get_pos()
        button_pos = (self.rect.x + self.item_pos[0], self.rect.y + self.item_pos[1])
        if pygame.Rect(button_pos, self.rect.size).collidepoint(mous_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.callback()
                print("onclic__________________test")
                pygame.time.wait(300)

    def update(self):
        self.draw()
        self.onclick()
        self.hover()
        
        # for event in event_list:
        #     if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #         if self.rect.collidepoint(event.pos):
        #             self.callback()


item = pygame.sprite.Group()
simpleButton = pygame.sprite.Group()