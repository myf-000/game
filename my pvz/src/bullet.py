from entity import Entity

class Bullet(Entity):
    def __init__(self,top,left,speed):
        super().__init__("Bullet_1",1,top,left,speed)
        self.damage = 20

    def update(self,index):
        super().update(index)

        if (self.rect.top < 0 or self.rect.top > 720) or (self.rect.left < 0 or self.rect.left > 1200):
            self.kill()

