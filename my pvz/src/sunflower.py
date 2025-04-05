from entity import Entity

class Sunflower(Entity):
    def __init__(self,top,left):
        super().__init__("Sunflower",13,top,left)
        self.name = "Sunflower"