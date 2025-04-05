from entity import Entity

class Zombie(Entity):
    def __init__(self,top,left):
        super().__init__("Zombie",21,top,left,1,"left")
        self.health = 100

