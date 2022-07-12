import sys
import pygame
from bullet import Bullet
from settings import Settings
from ship import Ship


class AlienInvasion:
    '''管理游戏资源和行为'''

    def __init__(self) -> None:
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        pygame.display.set_caption("AlienInvasion")
        self.icon = pygame.image.load('images/图标.png')
        pygame.display.set_icon(self.icon)
    def _check_events(self):
        '''检测鼠标键盘的事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False
    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
    def _update_screen(self):
        self.screen.fill(color=self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    def run_game(self):
        '''游戏主循环'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
