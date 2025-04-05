import pygame  #引入第三方游戏库
import sys     #引入系统库
import os      #引入操作系统库

from peashooter import Peashooter       #代入自己写的peashooter中的Peashooter类
from sunflower import Sunflower         #代入自己写的sunflower中的Sunflower类
from shovel import Shovel
from zombie import Zombie
from bullet import Bullet
from xiaobai import Xiaobai
from card import SunflowerCard, PeaShooterCard, ShovelCard,XiaobaiCard



pygame.init() 
screen = pygame.display.set_mode((1250,720))                           #设置屏幕大小

# 定义植物
plant_sprites = pygame.sprite.Group()
# xiaobai = Xiaobai(400,350)
# plant_sprites.add(xiaobai)

image_path = os.path.join(os.getcwd(), "..", "resource","images")      #获取图片路径
background_path = os.path.join(image_path,"background1.jpg")           #拼接背景图片完整路径
bg_image = pygame.image.load(background_path)                             #加载背景图片

seed_path = os.path.join(image_path,"SeedBank.png")
seed_image = pygame.image.load(seed_path)

# 定义植物卡片
card_sprites = pygame.sprite.Group()
sunflower_card = SunflowerCard(100,40)
pea_card = PeaShooterCard(160,40)
xiaobai_card = XiaobaiCard(220,40)
#shovel_card = ShovelCard(100,300)

card_sprites.add(sunflower_card)
card_sprites.add(pea_card)
card_sprites.add(xiaobai_card)
#card_sprites.add(shovel_card)

# 定义子弹
bullet_sprites = pygame.sprite.Group()



index = 0                                                              #初始化index

clock = pygame.time.Clock()                                            #设置游戏时钟

# 定义僵尸
zombie_sprites = pygame.sprite.Group()


zombie1 = Zombie(1000,100)
zombie2 = Zombie(1000,200)
zombie3 = Zombie(1000,300)

zombie_sprites.add(zombie1)
zombie_sprites.add(zombie2)
zombie_sprites.add(zombie3)


choose = None
dragging = False                                                       #是否处于拖动图片的状态
while True:                                                            #游戏主循环
    if index > 100:                                                    #当index大于100时
        index = 0                                                      #重置index

    dt = clock.tick(15) / 1000.0                                      #设置游戏帧率                                                    #设置游戏帧率
    for event in pygame.event.get():                                  #处理事件（鼠标点击、键盘按键等）
        if event.type == pygame.QUIT:                                 #如果事件类型为退出
            pygame.quit()                                             #退出游戏
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos

                for card in card_sprites:
                    if card.rect.collidepoint(x,y):
                        dragging = True
                        if card.name == "Sunflower":
                            dragging = True
                            choose = Sunflower(x,y)
                        elif card.name == "Peashooter":
                            dragging = True
                            choose = Peashooter(x,y)
                        elif card.name == "Xiaobai":
                            dragging = True
                            choose = Xiaobai(x,y)
                        elif card.name == "Shovel":
                            dragging = True
                            choose = Shovel(x,y)    
                        else:
                            dragging = False
                            choose = None
                        print("choose",choose)
                        print("dragging",dragging)
                    else:
                        choose = None
        
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if dragging and choose:
                    x,y = event.pos
                    print("1",choose)
                    plant_sprites.add(choose)

                    print("2",choose)
                    if choose.name == "Peashooter":
                        print(choose)
                    if choose.name == "Sunflower":
                        print(choose)
                        # bullet = Bullet(x,y)
                        # bullet_sprites.add(bullet)
                    dragging = False


        if event.type == pygame.MOUSEMOTION:
            if dragging and choose:
                print("3",choose)
                choose.rect.center = event.pos

    zombie_sprites.update(index)
    plant_sprites.update(index)
    bullet_sprites.update(index)
    card_sprites.update(index)

    for plant in plant_sprites:
        if index % 13 == 0:
            bullet = plant.shoot()
            if bullet:
                bullet_sprites.add(bullet)
    # 碰撞检测
    bullet_collisions = pygame.sprite.groupcollide(zombie_sprites, bullet_sprites, False, True)
    for zombie, bullets in bullet_collisions.items():
        for bullet in bullets:
            zombie.health -= bullet.damage
            if zombie.health <= 0:
                zombie.kill()

    plant_collisions = pygame.sprite.groupcollide(zombie_sprites, plant_sprites, True, True)

# 绘制游戏内容
    screen.fill((0,0,0))                                              #清空屏幕，填充颜色
    screen.blit(bg_image,(0,0))    
    screen.blit(seed_image,(0,0))                                       #绘制种子图片

    plant_sprites.draw(screen)
    zombie_sprites.draw(screen)
    bullet_sprites.draw(screen)
    card_sprites.draw(screen)

   
    if choose:                                        
        screen.blit(choose.images[index % choose.image_count],choose.rect)                      #绘制peashooter图片

    pygame.display.flip()                                           #更新屏幕

    index += 1                                                        #更新index
