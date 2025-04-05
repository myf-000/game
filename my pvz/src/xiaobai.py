from entity import Entity
from bullet import Bullet

class Xiaobai(Entity):
    def __init__(self,top,left):
        super().__init__("xiaobai_wandousheshou",13,top,left)
        self.name = "Xiaobai"


    def shoot(self):
        return Bullet(self.rect.right,self.rect.y+15,5)