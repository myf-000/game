import random
from bullet import Bullet
from sun import Sun
from bomb import Bomb
from entity import Entity
from utils import load_json

class Plant(Entity):
    def __init__(self,plant_name,center_x,center_y):
        data = load_json("data/plant.json")
        image_name = data[plant_name]["image_name"]
        image_count = data[plant_name]["image_count"]
        speed = data[plant_name]["speed"]
        direction = data[plant_name]["direction"]
        super().__init__(image_name,image_count,center_x,center_y,speed,direction)
        self.health = data[plant_name]["health"]
        self.damage = data[plant_name]["damage"]
        self.cooldown = data[plant_name]["cooldown"]
        self.last_produced_time = 0
        self.can_produce = True
        self.production_type = data[plant_name]["production_type"]
        self.production_count = data[plant_name]["production_count"]
        self.production = None
        self.price = data[plant_name]["price"]
        self.name = data[plant_name]["name"]
        self.dead = False

    def update(self,index,current_time):
        super().update(index)
        if current_time - self.last_produced_time > self.cooldown:
            self.last_produced_time = current_time
            self.can_produce = True
        else:
            pass
            #self.can_produce = False

    def produce(self):
        return False
    
    def handle_collision(self):
        pass
    
class Xiaobai(Plant):
    def __init__(self,top,left):
        super().__init__("xiaobai",top,left)
        self.last_produced_time = 0
        self.can_produce = True
        self.production = None

    def produce(self):
        if self.can_produce:
            self.production = Bullet(self.rect.right,self.rect.y+15,5)
            self.can_produce = False
            return (self.production_type,self.production_count,self.production)
        else:
            return False
        
class Xiaobaichuipaopao(Plant):
    def __init__(self,top,left):
        super().__init__("xiaobai_chuipaopao",top,left)
        self.last_produced_time = 0
        self.can_produce = True
        self.production = None

    def produce(self):
        if self.can_produce:
            self.production = Bullet(self.rect.right,self.rect.y+15,5)
            self.can_produce = False
            return (self.production_type,self.production_count,self.production)
        else:
            return False

class Xiaobaisunflower(Plant):
    def __init__(self,top,left):
        super().__init__("sunflower",top,left)
        self.last_produced_time = 0
        self.can_produce = True
        self.production = None
        self.top = top
        self.left = left

    def produce(self):
        if self.can_produce:
            x = random.randint(100,800)
            y = random.randint(100,600)
            self.production = Sun(self.last_produced_time,x,y)
            self.can_produce = False
            return (self.production_type,self.production_count,self.production)
        else:
            return False
                
class Xiaobaicar(Plant):
    def __init__(self,top,left):
        super().__init__("xiaobai_car",top,left)
        self.last_produced_time = 0
        self.can_produce = False
        self.production = None
        
    def handle_collision(self):
        self.speed = 10

class Xiaobaiboxer(Plant):
    def __init__(self,top,left):
        super().__init__("xiaobai_boxer",top,left)
        self.last_produced_time = 0
        self.can_produce = False
        self.production = None

    def produce(self):
        if self.can_produce:
            self.production = Bullet(self.rect.right,self.rect.y+15,5)
            self.can_produce = False
            return (self.production_type,self.production_count,self.production)
        else:
            return False
        
class Xiaobaideath(Plant):
    def __init__(self,top,left,create_time):
        super().__init__("xiaobai_death",top,left)
        self.last_produced_time = 0
        self.can_produce = False
        self.production = None
        self.create_time = create_time
        self.alive_time = 800
        
    def update(self,index,current_time):
        super().update(index,current_time)

        if current_time - self.create_time > self.alive_time:
            self.kill()

class Xiaobaibomb(Plant):
    def __init__(self,top,left,create_time):
        super().__init__("xiaobai_bomb",top,left)
        self.last_produced_time = 0
        self.can_produce = True
        self.production = None
        self.alive_time = 800
        self.create_time = create_time
        self.dead = False
        
    def update(self,index,current_time):
        super().update(index,current_time)

        if current_time - self.create_time > self.alive_time:
            self.dead = True

    def produce(self):
        if self.can_produce:
            x,y = self.rect.center
            self.production = Bomb(self.last_produced_time,x,y)
            self.can_produce = False
            return (self.production_type,self.production_count,self.production)
        else:
            return False