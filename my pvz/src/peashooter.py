from entity import Entity
from bullet import Bullet

class Peashooter(Entity):
    def __init__(self,top,left):
        super().__init__("Peashooter",13,top,left)
        self.name = "Peashooter"
        self.bullet_delay = 5
        self.need_shoot = True
        self.health = 100

    def shoot(self):
        return Bullet(self.rect.right,self.rect.y+15,5)
    