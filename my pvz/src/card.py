import pygame
import os

class Card(pygame.sprite.Sprite):
    def __init__(self,image_name,center_x,center_y):
        super().__init__()
        CARD_SIZE = (55, 75)
        self.image_path = os.path.join(os.getcwd(), "..", "resource","images")
 
        image = pygame.image.load(os.path.join(self.image_path, "{}.gif".format(image_name))).convert_alpha()
        self.image  = pygame.transform.scale(image , CARD_SIZE)

        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)

    def start_drag(self):
        self.dragging = True

    def stop_drag(self):    
        self.dragging = False       

    def drag(self, dx, dy):
        if self.dragging:
            self.rect.center(dx, dy)


class SunflowerCard(Card):
    def __init__(self,center_x,center_y):
        super().__init__("Sunflower",center_x,center_y)
        self.name = "sunflower"

class PeaShooterCard(Card):
    def __init__(self,center_x,center_y):
        super().__init__("Peashooter",center_x,center_y)
        self.name = "Peashooter"

class ShovelCard(Card):
    def __init__(self,center_x,center_y):
        super().__init__("Shovel",center_x,center_y)
        self.name = "Shovel"

class XiaobaiCard(Card):
    def __init__(self,center_x,center_y):
        super().__init__("xiaobai_wandousheshou",center_x,center_y)
        self.name = "xiaobai"

class XiaobaichuipaopaoCard(Card):
    def __init__(self,center_x,center_y):
        super().__init__("xiaobai_chuipaopao",center_x,center_y)
        self.name = "xiaobai_chuipaopao"
