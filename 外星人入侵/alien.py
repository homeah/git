import pygame
from pygame.sprite import Sprite
import random as r
class Alien(Sprite):
    def __init__(self,ai_setting,screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #每个外星人开始出现在左上角
        self.rect.x = 0
        self.rect.y = 0

        self.x = float(self.rect.x)

    def update(self):
        #向右移动外星人
        self.x += (self.ai_setting.alien_speed_factor*self.ai_setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def blitme(self):
        self.screen.blit(self.image,self.rect)
