import pygame

# 定义颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
class Grid:
    def __init__(self, x, y, width, height, cell_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = [[None for _ in range(height)] for _ in range(width)]


    def get_cell_center(self, grid_x, grid_y):
        return (self.x + grid_x * self.cell_size + self.cell_size // 2,
                self.y + grid_y * self.cell_size + self.cell_size // 2)


    def get_grid_pos(self, mouse_x, mouse_y):
        if self.x <= mouse_x < self.x + self.width * self.cell_size and \
           self.y <= mouse_y < self.y + self.height * self.cell_size:
            return ((mouse_x - self.x) // self.cell_size,
                    (mouse_y - self.y) // self.cell_size)
        return None


    def place_plant(self, plant, grid_x, grid_y):
        if 0 <= grid_x < self.width and 0 <= grid_y < self.height:
            if self.grid[grid_x][grid_y] is None:
                center_x, center_y = self.get_cell_center(grid_x, grid_y)
                plant.rect.center = (center_x, center_y)
                self.grid[grid_x][grid_y] = plant
                return True
        return False


    def draw(self, screen):
        # 绘制网格背景
        # pygame.draw.rect(screen, LIGHT_GRAY, 
        #                  (self.x, self.y, 
        #                   self.width * self.cell_size, 
        #                   self.height * self.cell_size))
        
        # 绘制网格线
        for x in range(self.width + 1):
            pygame.draw.line(screen, BLACK, 
                             (self.x + x * self.cell_size, self.y),
                             (self.x + x * self.cell_size, self.y + self.height * self.cell_size))
        for y in range(self.height + 1):
            pygame.draw.line(screen, BLACK, 
                             (self.x, self.y + y * self.cell_size),
                             (self.x + self.width * self.cell_size, self.y + y * self.cell_size))