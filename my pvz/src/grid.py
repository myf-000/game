import pygame

# 定义颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (200, 200, 200)
class Grid:
    def __init__(self, x, y, width, height, cell_width,cell_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.grid = [[None for _ in range(height)] for _ in range(width)]


    def get_cell_center(self, grid_x, grid_y):
        return (self.x + grid_x * self.cell_width + self.cell_width // 2,
                self.y + grid_y * self.cell_height + self.cell_height // 2)


    def get_grid_pos(self, mouse_x, mouse_y):
        if self.x <= mouse_x < self.x + self.width * self.cell_width and \
           self.y <= mouse_y < self.y + self.height * self.cell_height:
            return ((mouse_x - self.x) // self.cell_width,
                    (mouse_y - self.y) // self.cell_height)
        return None


    def place_plant(self, plant, grid_x, grid_y):
        if plant.name != "xiaobai_car" and grid_x == 0:
            print("4")
            return False
        if 0 <= grid_x < self.width and 0 <= grid_y < self.height:
            if self.grid[grid_x][grid_y] is None:
                center_x, center_y = self.get_cell_center(grid_x, grid_y)
                plant.rect.center = (center_x, center_y)
                self.grid[grid_x][grid_y] = plant
                return True
        return False

    def remove_plant(self, plant):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x][y] == plant:
                    self.grid[x][y] = None
                    return True
        return False

    def get_center_pos(self, mouse_x, mouse_y):
        grid_x,grid_y = self.get_grid_pos(mouse_x, mouse_y)

        return self.get_cell_center(grid_x,grid_y)
    
    def draw(self, screen):
        # 绘制网格背景
        # pygame.draw.rect(screen, LIGHT_GRAY, 
        #                  (self.x, self.y, 
        #                   self.width * self.cell_size, 
        #                   self.height * self.cell_size))
        
        # 绘制网格线
        for x in range(self.width + 1):
            pygame.draw.line(screen, BLACK, 
                             (self.x + x * self.cell_width, self.y),
                             (self.x + x * self.cell_width, self.y + self.height * self.cell_height))
        for y in range(self.height + 1):
            pygame.draw.line(
                screen, BLACK,
                (self.x, self.y + y * self.cell_height),  # 横线起点（修正：使用 cell_height）
                (self.x + self.width * self.cell_width, self.y + y * self.cell_height)  # 横线终点
            )