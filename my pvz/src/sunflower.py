import random
from plant import Plant
from sun import Sun
        
class Sunflower(Plant):
    def __init__(self,top,left):
        super().__init__("Sunflower",13,top,left)
        self.health = 100
        self.damage = 0
        self.cooldown = 5000
        self.last_produced_time = 0
        self.can_produce = False
        self.production_type = "sun"
        self.production_count = 1
        self.production = None

    def produce(self):
        if self.can_produce:
            x = random.randint(100,800)
            y = random.randint(100,600)
            self.production = Sun(self.last_produced_time,x,y)
            self.can_produce = False
            return (self.production_type,self.production_count,self.production)
        else:
            return False


