import pygame
from pygame.sprite import Sprite 
class Bullet(Sprite):
    #管理子弹的类
    def __init__(self, ai_settings,ship,screen):
        super().__init__()
        self.screen=screen

        #在(0,0)处创建一个矩形子弹，再根据飞船将其放到正确位置
        self.bullet_rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.bullet_color=ai_settings.bullet_color
        self.bullet_speed=ai_settings.bullet_speed_factor
        self.bullet_rect.centerx=ship.rect.centerx
        self.bullet_rect.top=ship.rect.top
        #让子弹的y轴能保存小数
        self.bullet_rect_y=float(self.bullet_rect.y)

    def update(self):
        #更新表示子弹位置的小数值
        self.bullet_rect_y-=self.bullet_speed
        #更新表示子弹的rect的位置
        self.bullet_rect.y=self.bullet_rect_y

    def drawme(self):
        #绘出子弹
        pygame.draw.rect(self.screen,self.bullet_color,self.bullet_rect)



        
