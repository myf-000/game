from entity import Entity

class Xiaobai(Entity):
    def __init__(self,top,left):
        super().__init__("xiaobai_wandousheshou",13,top,left)
        self.name = "Xiaobai"