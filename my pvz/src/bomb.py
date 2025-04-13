from entity import Entity

class Bomb(Entity):
    def __init__(self, create_time, top, left):
        super().__init__("bomb",16,top,left,0,"right",True,size=(180,180))
        self.create_time = create_time
        self.alive_time = 800

    def update(self, index,current_time):
        super().update(index)
        if current_time - self.create_time > self.alive_time:
            self.kill()
        