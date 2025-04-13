import pygame
import os

class Entity(pygame.sprite.Sprite):
    def __init__(self,image_name,image_count,center_x,center_y,speed=0,direction="right",scale=False,size=(95,95)):
        super().__init__()
        self.image_path = os.path.join(os.getcwd(), "..", "resource","images")
        self.images = []
        self.image_count = image_count
        self.images = []
        self.image = None
        self.load_images(image_name,image_count,scale,size)

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
    
    def load_images(self,image_name,image_count,scale,size):
        new_images = []
        if image_count == 1:
            img = pygame.image.load(os.path.join(self.image_path, "{}.png".format(image_name))).convert_alpha()
            if scale:
                img  = pygame.transform.scale(img , size)
                img = pygame.transform.smoothscale(img, size)

            new_images.append(img)
        else:
            for i in range(0, image_count):
                img = pygame.image.load(os.path.join(self.image_path, "{}_{:02d}.png".format(image_name,i))).convert_alpha()
                if scale:
                    img  = pygame.transform.scale(img , size)
                    img = pygame.transform.smoothscale(img, size)
                new_images.append(img)       
                
        self.images[:] = new_images 
        self.image_count = image_count
        self.image = self.images[0]