from entity import Entity

class Sun(Entity):
    def __init__(self, create_time, top, left):
        super().__init__("sun",17,top,left)
        self.create_time = create_time
        self.alive_time = 8000
        self.money = 25

    def update(self, index,current_time):
        super().update(index)
        if current_time - self.create_time > self.alive_time:
            self.kill()
        