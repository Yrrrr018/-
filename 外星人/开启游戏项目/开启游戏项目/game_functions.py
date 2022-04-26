from re import T
import sys
import pygame
from bullet import Bullet 

def check_event(ship,ai_settings,screen,bullets):
    '''监视键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_event(ship,event,ai_settings,screen,bullets)      
        elif event.type==pygame.KEYUP:
            check_keyup_event(ship,event)
                

def check_keydown_event(ship,event,ai_settings,screen,bullets):
    #检测按键event
    if event.key==pygame.K_RIGHT:
        ship.moving_right = True 
    if event.key==pygame.K_LEFT:
        ship.moving_left=True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, ship,screen,bullets)
    
def fire_bullet (ai_settings, ship,screen,bullets):
    #创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed: 
        new_bullet = Bullet(ai_settings, ship,screen) 
        bullets.add(new_bullet)

def check_keyup_event(ship,event):
    #检测松键event
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False



def update_screen(ai_settings, screen, ship,bullets):
    #每次循环时重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme() 
    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites(): 
        bullet.drawme() 
    
    #让最近绘制的屏幕可见
    pygame.display.flip()