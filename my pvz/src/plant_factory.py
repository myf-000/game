import json
import random

from plant import *
from utils import load_json

class PlantFactory:
    def __init__(self,grid):
        self.data = load_json('data/plant.json')
        # self.last_check_time = 0
        # self.cooldown = 1000
        # self.current_stage = 0
        # self.stage_count = len(self.data['stages'])
        self.grid = grid

    def create_plant(self, money, plant, x, y,create_plant):
        if money < self.data[plant]['price']:
            return None
        
        grid_pos = self.grid.get_grid_pos(x,y)
        if grid_pos is None:
            return None
        
        x,y = grid_pos

        plant_instance = None
        if plant == 'sunflower':
            plant_instance = Xiaobaisunflower(x, y)
        elif plant == 'xiaobai':
            plant_instance =  Xiaobai(x, y)
        elif plant == 'xiaobai_chuipaopao':
            plant_instance = Xiaobaichuipaopao(x, y)
        elif plant == 'xiaobai_car':
            plant_instance = Xiaobaicar(x, y)
        elif plant == 'xiaobai_boxer':
            plant_instance = Xiaobaiboxer(x, y)
        elif plant == 'xiaobai_bomb':
            plant_instance = Xiaobaibomb(x, y,create_plant)
        else:
            plant_instance = None
        
        if plant_instance is None:
            return None
        
        if self.grid.place_plant(plant_instance,x,y):
            return plant_instance
        else:
            return None
        
    def create_death_plant(self,x,y,create_time):
        return Xiaobaideath(x,y,create_time)