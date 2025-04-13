import pygame
from entity import Entity
from utils import load_json

class Zombie(Entity):
    def __init__(self,zombie_name,top,left):
        self.name = zombie_name
        date = load_json("data/zombie.json")
        immage_name = date[zombie_name]["image_name"]
        immage_count = date[zombie_name]["image_count"]
        self.speed = date[zombie_name]["speed"]
        self.direction = date[zombie_name]["direction"]
        super().__init__(immage_name,immage_count,top,left,self.speed,self.direction)
        self.health = date[zombie_name]["health"]
        self.damage = date[zombie_name]["damage"]
        self.attack_cooldown = date[zombie_name]["cooldown"]
        self.last_attack_time = 0
        self.level = date[zombie_name]["level"]
        self.win = False
        self.attack_range = pygame.Rect(0, 0, 30, 80)
        self.state = "moving"

    def update(self,index,current_time):
        super().update(index)

        self.attack_range.midright = self.rect.midleft if self.direction == "left" else self.rect.midright
        if self.rect.left < 100:
            self.win = True

    def attack(self,current_time):
        self.speed = 0
        if self.last_attack_time == 0:
            self.last_attack_time = current_time
            return True
        if current_time - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = current_time
            return True
            
        return False

    def move(self):
        data = load_json("data/zombie.json")
        self.speed = data[self.name]["speed"]

    def stop(self):
        self.speed = 0

class Xiaojimao(Zombie):
    def __init__(self,top,left):
        super().__init__("xiaojimao",top,left)

class Xiaojimaojump(Zombie):
    def __init__(self,top,left):
        super().__init__("xiaojimao_jump",top,left)

class Xiaojimaobag(Zombie):
    def __init__(self,top,left):
        super().__init__("xiaojimao_bag",top,left)

class Xiaojimaomusic(Zombie):
    def __init__(self,top,left):
        super().__init__("xiaojimao_music",top,left)

class Xiaojimaostrong(Zombie):
    def __init__(self,top,left):
        super().__init__("xiaojimao_strong",top,left)

class Xiaojimaodeath(Zombie):
    def __init__(self,top,left,create_time):
        super().__init__("xiaojimao_death",top,left)
        self.create_time = create_time
        self.alive_time = 450


    def update(self,index,current_time):
        super().update(index,current_time)

        if current_time - self.create_time > self.alive_time:
            self.kill()
