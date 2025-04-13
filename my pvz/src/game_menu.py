import os
import pygame
import pygame_gui
from typing import Callable

class GameMenu:
    def __init__(self, manager: pygame_gui.UIManager, screen_size: tuple):
        self.manager = manager
        self.screen_size = screen_size
        self.menu_window = None
        image_path = os.path.join(os.getcwd(), "..", "resource","images")
        background = os.path.join(image_path,"Surface.png")           #拼接背景图片完整路径
        self.background = pygame.image.load(background).convert()
        self.background = pygame.transform.scale(self.background, screen_size)
        

    def show(self):
        """显示菜单窗口"""
        
        # 创建半透明覆盖层
        overlay = pygame.Surface(self.screen_size, pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))  # 半透明黑色
        
        # 创建菜单窗口
        self.menu_window = pygame_gui.elements.UIWindow(
            rect=pygame.Rect(
                (self.screen_size[0]//2 - 150, self.screen_size[1]//2 - 200),
                (300, 400)
            ),
            manager=self.manager,
            window_display_title="游戏菜单",
            object_id="#game_menu",
            visible=1
        )
        self.menu_window.set_blocking(True)  # 模态窗口
        
        # 添加菜单按钮
        button_height = 45
        padding = 15
        options = [
            ("回到游戏", "#resume_button"),
            ("重新开始", "#restart_button"),
            ("图鉴收集", "#gallery_button"), 
            ("返回主界面", "#return_button")
        ]
        
        for i, (text, obj_id) in enumerate(options):
            pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(
                    (50, 80 + i*(button_height + padding)),
                    (200, button_height)
                ),
                text=text,
                manager=self.manager,
                container=self.menu_window,
                object_id=obj_id
            )

    def handle_events(self, event):
        """处理菜单事件"""
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if not self.menu_window:
                return
                
            # 通过object_id判断哪个按钮被点击
            if hasattr(event.ui_element, "object_ids"):
                if "#resume_button" in event.ui_element.object_ids:
                    self.close()
                    self.resume_game()
                elif "#restart_button" in event.ui_element.object_ids:
                    self.restart_game()
                elif "#gallery_button" in event.ui_element.object_ids:
                    self.show_gallery()
                elif "#return_button" in event.ui_element.object_ids:
                    self.close()
                    self.return_to_menu()

    def close(self):
        """关闭菜单"""
        if self.menu_window:
            self.menu_window.kill()
            self.menu_window = None

    def draw_background(self, surface):
        """绘制带背景的菜单"""
        surface.blit(self.background, (0, 0))
        if self.menu_window:
            # 添加背景模糊效果
            blur = pygame.Surface(self.screen_size, pygame.SRCALPHA)
            blur.fill((0, 0, 0, 128))
            surface.blit(blur, (0, 0), special_flags=pygame.BLEND_MULT)

    def resume_game(self):
        print("1")

    def restart_game(self):
        print("2")

    def show_gallery(self):
        print("3")

    def return_to_menu(self):
        print("4")