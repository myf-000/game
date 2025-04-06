from entity import Entity
from utils import load_json

class Zombie(Entity):
    def __init__(self,zombie_name,top,left):
        self.name = zombie_name
        date = load_json("zombie.json")
        immage_name = date[zombie_name]["image_name"]
        immage_count = date[zombie_name]["image_count"]
        self.speed = date[zombie_name]["speed"]
        self.direction = date[zombie_name]["direction"]
        super().__init__(immage_name,immage_count,top,left,self.speed,self.direction)
        self.health = date[zombie_name]["health"]
        self.damage = date[zombie_name]["damage"]
        self.attack_cooldown = date[zombie_name]["cooldown"]
        self.last_attack_time = 0
        self.level = 1
        self.win = False

    def update(self,index):
        super().update(index)

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
        data = load_json("zombie.json")
        self.speed = data[self.name]["speed"]

    def stop(self):
        self.speed = 0

class Xiaojimao(Zombie):
    def __init__(self,top,left):
        super().__init__("xiaojimao",top,left)

class Xiaojimaojump(Zombie):
    def __init__(self,top,left):
        super().__init__("xiaojimao_jump",top,left)