import pygame  #引入第三方游戏库
import sys     #引入系统库
import os      #引入操作系统库
import json    #引入json库

from card import *
from sun import Sun
from grid import Grid
from zombie_factory import ZombieFactory
from plant_factory import PlantFactory

money = 200

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1250,720))                           #设置屏幕大小

grid = Grid(215,90,10,5,95,120)
# 音乐
pygame.mixer.music.load(os.path.join(os.getcwd(), "..", "resource","music","18 - Crazy Dave IN-GAME.mp3"))   #加载背景音乐
pygame.mixer.music.play(-1)                                            #播放背景音乐，-1表示循环播放

#加载json数据
plant_data = {}
with open(os.path.join(os.getcwd(), "plant.json"),"r") as f:
    plant_data = json.load(f)

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
xiaobaichuipaopao_card = XiaobaichuipaopaoCard(300,40)
shovel_card = ShovelCard(500,40)

card_sprites.add(sunflower_card)
card_sprites.add(xiaobai_card)
card_sprites.add(xiaobaichuipaopao_card)
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

score = 0
state = None
choose = None
select_card = None
select_x = 0
select_y = 0
select_image = None

zombie_factory = ZombieFactory(grid,"forever")
plant_factory = PlantFactory(grid)

for y in range(200,700,120):
    x = 400
    plant_sprites.add(plant_factory.create_plant(money,"xiaobai_car",x,y))
# plant1 = plant_factory.create_plant(money,"xiaobai_car",400,200)
# plant2 = plant_factory.create_plant(money,"xiaobai_car",400,320)
# plant3 = plant_factory.create_plant(money,"xiaobai_car",400,480)
# # plant4 = plant_factory.create_plant(money,"xiaobai_car",400,200)
# # plant5 = plant_factory.create_plant(money,"xiaobai_car",400,200)
# plant_sprites.add(plant1)
# plant_sprites.add(plant2)
# plant_sprites.add(plant3)
# plant_sprites.add(plant4)
# plant_sprites.add(plant5)

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
                        select_card = card.name
                        image_name = plant_data[card.name]['image_name']
                        first_image = image_name + "_00.png"
                        select_path = os.path.join(image_path,first_image)
                        select_image = pygame.image.load(select_path)
                        break

        
        # 鼠标左键松开
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x,y = event.pos
                if select_image is not None:
                    choose = plant_factory.create_plant(money,select_card,x,y)

                    if choose is not None:
                        money -= plant_data[select_card]['price']
                        plant_sprites.add(choose)
                        choose = None
                    select_image = None
                    select_card = None

        # 鼠标移动
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            if select_image is not None:
                select_x,select_y = x,y
            for sun in sun_sprites:
                if sun.rect.collidepoint(x,y):
                    money = money + sun.money
                    sun.kill()


    #更新精灵组状态
    current_time = pygame.time.get_ticks()
    zombie_sprites.update(index)
    plant_sprites.update(index, current_time)
    bullet_sprites.update(index)
    card_sprites.update(index)
    sun_sprites.update(index, current_time)
    zombie = zombie_factory.update(current_time)

    if zombie is not None:
        zombie_sprites.add(zombie)

    # 判断僵尸是否胜利
    for zombie in zombie_sprites:
        if zombie.win == True:
            screen.blit(game_over_image,(200,100))  

    # 将植物的生产物品添加到相应的精灵组中
    for plant in plant_sprites:
        result = plant.produce()
        if result:
            production_type, production_count, production = result
            if production_type == "bullet":
                bullet_sprites.add(production)
            elif production_type == "sun":
                sun_sprites.add(production)

    # 子弹和僵尸碰撞检测
    bullet_collisions = pygame.sprite.groupcollide(zombie_sprites, bullet_sprites, False, True)
    for zombie, bullets in bullet_collisions.items():
        for bullet in bullets:
            zombie.health -= bullet.damage
            if zombie.health <= 0:
                score += zombie.level
                zombie.kill()

    # 僵尸和植物碰撞检测
    plant_collisions = pygame.sprite.groupcollide(plant_sprites,zombie_sprites,False, False)
    for plant,zombies  in plant_collisions.items():
        plant.handle_collision()
        for zombie in zombies:
            if zombie.attack(current_time)  == True:
                plant.health -= zombie.damage
                zombie.health -= plant.damage
                if zombie.health <= 0:
                    zombie.kill()
                if plant.health <= 0:
                    grid.remove_plant(plant)
                    plant.kill()
                    for zombie in zombies:
                        zombie.move()

    # 绘制精灵组
    plant_sprites.draw(screen)
    zombie_sprites.draw(screen)
    bullet_sprites.draw(screen)
    card_sprites.draw(screen)
    sun_sprites.draw(screen)

    # 绘制文字
    font = pygame.font.Font(None, 25)
    text = font.render(str(money), True, (0,0,0))
    screen.blit(text,(30,65))

    font = pygame.font.Font(None, 25)
    text = font.render(str(score), True, (0,0,0))
    screen.blit(text,(1200,700))
   
    if select_image is not None:                                        
        screen.blit(select_image,(select_x-16,select_y-16))

    pygame.display.flip()                                           #更新屏幕

    index += 1                                                        #更新index
