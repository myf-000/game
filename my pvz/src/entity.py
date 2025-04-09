import pygame
import os

class Entity(pygame.sprite.Sprite):
    def __init__(self,image_name,image_count,center_x,center_y,speed=0,direction="right"):
        super().__init__()
        self.image_path = os.path.join(os.getcwd(), "..", "resource","images")
        self.images = []
        self.image_count = image_count
        Entity_SIZE = (100,100)
        if image_count == 1:
            img = pygame.image.load(os.path.join(self.image_path, "{}.png".format(image_name))).convert_alpha()
            # img  = pygame.transform.scale(img , Entity_SIZE)
            #img = pygame.transform.smoothscale(img, Entity_SIZE)

            self.images.append(img)
        else:
            for i in range(0, image_count):
                img = pygame.image.load(os.path.join(self.image_path, "{}_{:02d}.png".format(image_name,i))).convert_alpha()
                #img  = pygame.transform.scale(img , Entity_SIZE)
                #img = pygame.transform.smoothscale(img, Entity_SIZE)
                self.images.append(img)

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)
        self.speed = speed
        self.direction = direction
        self.need_shoot = False


    def update(self,index):
        self.image = self.images[index % self.image_count]
        if self.speed <= 0:
            return

        if self.rect.left > 0:
            if self.direction == "right":
                self.rect.right += self.speed
            elif self.direction == "left":
                self.rect.left -= self.speed
            else:
                pass

    def shoot(self):
        return False
