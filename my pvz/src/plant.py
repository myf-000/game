from entity import Entity

class Plant(Entity):
    def __init__(self,image_name,image_count,center_x,center_y,speed=0,direction="right"):
        super().__init__(image_name,image_count,center_x,center_y,speed,direction)
        self.health = 0
        self.damage = 0
        self.cooldown = 0
        self.last_produced_time = 0
        self.can_produce = True
        self.production_type = None
        self.production_count = 0
        self.production = None
        self.price = 0

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