import pygame


class Ship:
    '''管理飞船'''
    def __init__(self,ai_game) -> None:
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.rect.width = 55 
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
        if self.moving_down:
            self.y += self.settings.scrap_speed
        if self.moving_up:
            self.y -= self.settings.scrap_speed
        self.rect.y = self.y
    def blitme(self):
        '''绘制飞船'''
        self.screen.blit(self.image,self.rect)