import json
import random

from zombie import *
from utils import load_json

class ZombieFactory:
    def __init__(self):
        self.data = load_json('game.json')
        self.last_check_time = 0
        self.cooldown = 1000
        self.zombie_list = []
        self.current_stage = 0
        self.stage_count = len(self.data['stages'])
        self.prepare_stage_zombie(0)

    def prepare_stage_zombie(self,stage):
        self.zombie_list = []
        for zombie in self.data['stages'][stage]['zombies']:
            self.zombie_list.extend([zombie["name"]]*zombie["count"])

        random.shuffle(self.zombie_list)

    def update(self,current_time):
        check_result = self.check(current_time)
        if check_result:
            if len(self.zombie_list) == 0:
                self.current_stage += 1
                if self.current_stage >= self.stage_count:
                    print("Game Over")
                    return None
                print("Stage %d"%self.current_stage)
                self.prepare_stage_zombie(self.current_stage)
            zombie = self.zombie_list.pop()

            x,y = self.random_position()

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
        x=1100
        y=random.randint(100, 600)
        return x,y


    def check(self,current_time):
        if current_time - self.last_check_time >= self.cooldown:
            self.last_check_time = current_time
            return random.random() < 0.2
        return False