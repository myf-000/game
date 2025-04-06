import pygame  #引入第三方游戏库
import sys     #引入系统库
import os      #引入操作系统库

from peashooter import Peashooter       #代入自己写的peashooter中的Peashooter类
from sunflower import Sunflower         #代入自己写的sunflower中的Sunflower类
from shovel import Shovel
from zombie import Zombie,Xiaojimao
from bullet import Bullet
from xiaobai import Xiaobai
from card import SunflowerCard, PeaShooterCard, ShovelCard,XiaobaiCard
from sun import Sun
from grid import Grid

money = 50

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1250,720))                           #设置屏幕大小

grid = Grid(320,90,7,5,120)
# 音乐
pygame.mixer.music.load(os.path.join(os.getcwd(), "..", "resource","music","18 - Crazy Dave IN-GAME.mp3"))   #加载背景音乐
pygame.mixer.music.play(-1)                                            #播放背景音乐，-1表示循环播放


# 定义植物
plant_sprites = pygame.sprite.Group()
# xiaobai = Xiaobai(400,350)
# plant_sprites.add(xiaobai)

image_path = os.path.join(os.getcwd(), "..", "resource","images")      #获取图片路径
background_path = os.path.join(image_path,"background1.jpg")           #拼接背景图片完整路径
bg_image = pygame.image.load(background_path)                             #加载背景图片

seed_path = os.path.join(image_path,"SeedBank.png")
seed_image = pygame.image.load(seed_path)

game_over_path = os.path.join(image_path,"GameOver.png")
game_over_image = pygame.image.load(game_over_path)

# 定义植物卡片
card_sprites = pygame.sprite.Group()
sunflower_card = SunflowerCard(100,40)
pea_card = PeaShooterCard(160,40)
xiaobai_card = XiaobaiCard(220,40)
shovel_card = ShovelCard(500,40)

card_sprites.add(sunflower_card)
card_sprites.add(xiaobai_card)
#card_sprites.add(pea_card)
#card_sprites.add(shovel_card)

# 定义子弹
bullet_sprites = pygame.sprite.Group()



index = 0                                                              #初始化index

clock = pygame.time.Clock()                                            #设置游戏时钟

# 定义阳光
sun_sprites = pygame.sprite.Group()

sun = Sun(10,600,600)

sun_sprites.add(sun)

# 定义僵尸
zombie_sprites = pygame.sprite.Group()


zombie1 = Zombie(1000,100)
zombie2 = Zombie(1000,200)
zombie3 = Zombie(1000,300)

xiaojimao1 = Xiaojimao(1000,400)
xiaojimao2 = Xiaojimao(1000,500)

zombie_sprites.add(zombie1)
zombie_sprites.add(zombie2)
zombie_sprites.add(zombie3)

zombie_sprites.add(xiaojimao1)
zombie_sprites.add(xiaojimao2)


choose = None
select_card = None
dragging = False                                                       #是否处于拖动图片的状态
while True:                                                            #游戏主循环
    if index > 100:                                                    #当index大于100时
        index = 0                                                      #重置index

    # 绘制游戏背景
    screen.fill((0,0,0))                                              #清空屏幕，填充颜色
    screen.blit(bg_image,(0,0))    
    screen.blit(seed_image,(0,0))                                       #绘制种子图片
    grid.draw(screen)

    dt = clock.tick(15) / 1000.0                                      #设置游戏帧率                                                    #设置游戏帧率
    for event in pygame.event.get():                                  #处理事件（鼠标点击、键盘按键等）
        if event.type == pygame.QUIT:                                 #如果事件类型为退出
            pygame.quit()                                             #退出游戏

        # 鼠标左键按下
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos

                for card in card_sprites:
                    if card.rect.collidepoint(x,y):
                        if card.name == "Sunflower":
                            if money >= 50:
                                choose = Sunflower(x,y)
                                money -= 50
                            else:
                                print("Not enough money")
                        elif card.name == "Xiaobai":
                            if money >= 100:
                                choose = Xiaobai(x,y)
                                money -= 100
                            else:
                                print("Not enough money")
                        elif card.name == "Shovel":
                            choose = Shovel(x,y)
                        else:
                            choose = None

                        if choose:
                            plant_sprites.add(choose)
                        break
        
        # 鼠标左键松开
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x,y = event.pos
                if choose:
                    grid_pos = grid.get_grid_pos(x,y)
                    if grid_pos:
                        grid_x,grid_y = grid_pos
                        if not grid.place_plant(choose,grid_x,grid_y):
                            money += choose.price
                            choose.kill()
                choose = None

        # 鼠标移动
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            for sun in sun_sprites:
                if sun.rect.collidepoint(x,y):
                    money = money + sun.money
                    sun.kill()

            if choose:
                choose.rect.center = event.pos

    current_time = pygame.time.get_ticks()
    zombie_sprites.update(index)
    plant_sprites.update(index, current_time)
    bullet_sprites.update(index)
    card_sprites.update(index)
    sun_sprites.update(index, current_time)

    for zombie in zombie_sprites:
        if zombie.win == True:
            screen.blit(game_over_image,(200,100))  

    for plant in plant_sprites:
        result = plant.produce()

        print(result)
        if result:
            production_type, production_count, production = result
            if production_type == "bullet":
                bullet_sprites.add(production)
            elif production_type == "sun":
                sun_sprites.add(production)

    # 碰撞检测
    bullet_collisions = pygame.sprite.groupcollide(zombie_sprites, bullet_sprites, False, True)
    for zombie, bullets in bullet_collisions.items():
        for bullet in bullets:
            zombie.health -= bullet.damage
            if zombie.health <= 0:
                zombie.kill()

    plant_collisions = pygame.sprite.groupcollide(plant_sprites,zombie_sprites,False, False)
    for plant,zombies  in plant_collisions.items():
        for zombie in zombies:
            if zombie.attack(current_time)  == True:
                plant.health -= zombie.damage
                if plant.health <= 0:
                    plant.kill()
                    for zombie in zombies:
                        zombie.move()

    plant_sprites.draw(screen)
    zombie_sprites.draw(screen)
    bullet_sprites.draw(screen)
    card_sprites.draw(screen)
    sun_sprites.draw(screen)

    # 绘制文字
    font = pygame.font.Font(None, 25)
    text = font.render(str(money), True, (0,0,0))
    screen.blit(text,(30,65))



   
    # if choose:                                        
    #     screen.blit(choose.images[index % choose.image_count],choose.rect)                      #绘制peashooter图片

    pygame.display.flip()                                           #更新屏幕

    index += 1                                                        #更新index
