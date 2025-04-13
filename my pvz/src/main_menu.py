import pygame
import pygame_gui
import sys
import os

from main_game import main_game
# 初始化pygame
pygame.init()
pygame.font.init()
#custom_font = pygame.font.Font("C:\\Windows\\Fonts\\msyh.ttc", 24)
# 设置窗口
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("游戏主界面")

# 加载背景图片（替换为你的图片路径）
image_path = os.path.join(os.getcwd(), "..", "resource","images")
background = os.path.join(image_path,"start_menu.png")           #拼接背景图片完整路径
background = pygame.image.load(background).convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

#default_font = pygame.font.SysFont("Microsoft YaHei", 20)
# 初始化pygame_gui
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), starting_language='zh')

# 创建开始游戏按钮
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2), (200, 50)),
    text="开始游戏",
    manager=manager
)

# 游戏状态
GAME_STATE_MAIN_MENU = 0
GAME_STATE_PLAYING = 1
current_game_state = GAME_STATE_MAIN_MENU

# 游戏主循环
clock = pygame.time.Clock()
running = True

while running:
    time_delta = clock.tick(60) / 1000.0  # 控制帧率

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 处理UI事件
        if current_game_state == GAME_STATE_MAIN_MENU:
            manager.process_events(event)

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    print("进入游戏！")
                    current_game_state = GAME_STATE_PLAYING  # 切换游戏状态

        # 游戏中的事件处理（示例）
        elif current_game_state == GAME_STATE_PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    current_game_state = GAME_STATE_MAIN_MENU  # 返回主菜单

    # 渲染逻辑
    screen.fill((0, 0, 0))  # 清屏

    if current_game_state == GAME_STATE_MAIN_MENU:
        screen.blit(background, (0, 0))  # 绘制背景
        manager.update(time_delta)
        manager.draw_ui(screen)

    elif current_game_state == GAME_STATE_PLAYING:
        # # 这里是游戏主逻辑（示例：显示一个绿色方块）
        # screen.fill((0, 100, 0))
        # font = pygame.font.Font(None, 36)
        # text = font.render("游戏进行中...按ESC返回主菜单", True, (255, 255, 255))
        # screen.blit(text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2))
        ret = main_game()
        if ret:
            current_game_state = GAME_STATE_MAIN_MENU

    pygame.display.flip()  # 更新屏幕

pygame.quit()
sys.exit()