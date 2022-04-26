from turtle import screensize

import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        '''初始化飞船并初始化其位置'''
        self.screen=screen
        self.ai_settings=ai_settings
         
        #加载飞船图像，获取外接矩形
        self.image=pygame.image.load(r"C:\\Users\\YRUI\\Desktop\\外星人\\开启游戏项目\\ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #将每艘船放在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
        #设置飞船移动的标志
        self.moving_right = False
        self.moving_left=False

        #在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

    def update(self):
        '''更新飞船位置'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+= self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center-= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.center 

    def blitme(self): 
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

 




