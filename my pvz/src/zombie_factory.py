import json
import random

from zombie import *
from utils import load_json

class ZombieFactory:
    def __init__(self,grid,mode):
        self.data = load_json('game.json')
        self.last_check_time = 0
        self.cooldown = 1000
        self.zombie_list = []
        self.current_stage = 0
        self.stage_count = len(self.data['stages'])
        self.grid = grid
        self.prepare_stage_zombie(0)
        self.mode = mode

    def prepare_stage_zombie(self,stage):
        self.zombie_list = []
        for zombie in self.data['stages'][stage]['zombies']:
            self.zombie_list.extend([zombie["name"]]*zombie["count"])

        random.shuffle(self.zombie_list)

    def update(self,current_time):
        check_result = self.check(current_time)
        if check_result:
            if self.mode == "normal":
                if len(self.zombie_list) == 0:
                    self.current_stage += 1
                    if self.current_stage >= self.stage_count:
                        print("Game Over")
                        return None
                    print("Stage %d"%self.current_stage)
                    self.prepare_stage_zombie(self.current_stage)
                zombie = self.zombie_list.pop()
            elif self.mode == "forever":
                zombie = self.random_create_zombie()

            x,y = self.random_position()
            grid_x,grid_y = self.grid.get_center_pos(x,y)

            if zombie == "xiaojimao":
                return Xiaojimao(x,y)
            elif zombie == "xiaojimao_jump":
                return Xiaojimaojump(x,y)
            elif zombie == "xiaojimao_bag":
                return Xiaojimaobag(x,y)
            elif zombie == "xiaojimao_music":
                return Xiaojimaomusic(x,y)
            elif zombie == "xiaojimao_strong":
                return Xiaojimaostrong(x,y)
            else:
                return None
        else:
            return None

    def random_position(self):
        x=random.randint(1000, 1100)
        y=random.randint(100, 600)
        grid_x,grid_y = self.grid.get_center_pos(x,y)
        return grid_x,grid_y


    def check(self,current_time):
        if current_time - self.last_check_time >= self.cooldown:
            self.last_check_time = current_time
            return random.random() < 0.15
        return False
    
    def random_create_zombie(self):
        zombie_type = [ "xiaojimao","xiaojimao_jump","xiaojimao_bag","xiaojimao_music","xiaojimao_strong"]

        return random.choice(zombie_type)