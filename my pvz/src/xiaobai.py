from plant import Plant
from bullet import Bullet

    
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