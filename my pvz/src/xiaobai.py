from plant import Plant
from bullet import Bullet

    
class Xiaobai(Plant):
    def __init__(self,top,left):
        super().__init__("xiaobai_wandousheshou",13,top,left)
        self.health = 100
        self.damage = 20
        self.cooldown = 1000
        self.last_produced_time = 0
        self.can_produce = True
        self.production_type = "bullet"
        self.production_count = 1
        self.production = None
        self.price = 100

    def produce(self):
        if self.can_produce:
            self.production = Bullet(self.rect.right,self.rect.y+15,5)
            self.can_produce = False
            return (self.production_type,self.production_count,self.production)
        else:
            return False