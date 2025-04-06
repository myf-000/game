from entity import Entity

class Zombie(Entity):
    def __init__(self,top,left):
        super().__init__("Zombie",21,top,left,1,"left")
        self.health = 100
        self.damage = 10
        self.attack_cooldown = 500
        self.last_attack_time = 0
        self.win = False

    def update(self,index):
        super().update(index)

        if self.rect.left < 100:
            self.win = True

    def attack(self,current_time):
        self.speed = 0
        if self.last_attack_time == 0:
            self.last_attack_time = current_time
            return True
        if current_time - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = current_time
            return True
            
        return False
    
    def move(self):
        self.speed = 1

    def stop(self):
        self.speed = 0

class Xiaojimao(Entity):
    def __init__(self,top,left):
        super().__init__("xiaojimao_jiangshi",13,top,left,1,"left")
        self.health = 300
        self.damage = 10
        self.attack_cooldown = 500
        self.last_attack_time = 0
        self.win = False

    def update(self,index):
        super().update(index)

        if self.rect.left < 100:
            self.win = True

    def attack(self,current_time):
        self.speed = 0
        if self.last_attack_time == 0:
            self.last_attack_time = current_time
            return True
        if current_time - self.last_attack_time > self.attack_cooldown:
            self.last_attack_time = current_time
            return True
            
        return False
    
    def move(self):
        self.speed = 1

    def stop(self):
        self.speed = 0

class GameOver(Entity):
    def __init__(self,top,left):
        super().__init__("GameOver",1,top,left)
