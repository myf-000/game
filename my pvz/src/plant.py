from entity import Entity
from utils import load_json

class Plant(Entity):
    def __init__(self,plant_name,center_x,center_y):
        data = load_json("plant.json")
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