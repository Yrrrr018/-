from email.headerregistry import Group
import sys
import pygame
from setting import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from bullet import Bullet

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    #创建飞船
    ship=Ship(ai_settings,screen)
    #创建用来管理子弹的组
    bullets=Group()

    #开启主循环
    while True:
        gf.check_event(ship,ai_settings,screen,bullets)
        ship.update() 
        bullets.update() 

        # 在屏幕更新前删除已消失的子弹
        for bullet in bullets.copy(): 
            if bullet.bullet_rect.bottom <= 0:
                bullets.remove(bullet)  

        gf.update_screen(ai_settings, screen, ship,bullets)  

run_game()






