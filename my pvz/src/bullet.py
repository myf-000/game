from entity import Entity

class Bullet(Entity):
    def __init__(self,top,left,speed):
        super().__init__("Bullet_1",1,top,left,speed)
        self.damage = 20

