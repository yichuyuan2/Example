import pygame
import sys
from pygame.locals import *

pygame.init()
size = width, height = 600, 400  #初始化Pygame
speed = [0, 0]
bg = (255, 255, 255)
screen = pygame.display.set_mode(size) #创建指定大小的窗口
pygame.display.set_caption("初次见面，请大家多多关照！") #设置窗口标题
king = pygame.image.load("images/king.png")
position = king.get_rect() #获得图像的位置矩形
l_head = king #头朝左
r_head = pygame.transform.flip(king, True, False) #头朝右

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1, 0]
                king = l_head
            if event.key == K_RIGHT:
                speed = [1, 0]
                king == r_head
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
    position = position.move(speed) #移动图像
    if position.left < 0 or position.right > width:
        king = pygame.transform.flip(king, True, False) #翻转图像
        speed[0] = -speed[0] #反方向移动
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    screen.fill(bg) #填充背景
    screen.blit(king, position) #更新图像
    pygame.display.flip() #更新界面
    pygame.time.delay(30) #延迟30毫秒
    
