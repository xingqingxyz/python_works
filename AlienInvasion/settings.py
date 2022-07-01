class Settings:
    '''存储AlienInvasion的所有设置类'''
    def __init__(self) -> None:
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 230,230,230
        self.ship_speed = 1.5
        self.scrap_speed = 1
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        
