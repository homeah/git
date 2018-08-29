class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (255,255,255)
        self.speed_factor = 1.5

        #子弹设置
       #self.bullet_speed_factor = 1 已放置到initialize_setting里面
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 100

        #外星人设置
        self.initialize_setting()
        
        
        
        self.speedup_scale  = 1.1
        self.drop_speedup_scale  = 1.05
        self.score_scale = 1.5
        self.ship_limit = 3

    def initialize_setting(self):
        self.ship_speed_factor = 1
        self.bullet_speed_factor = 50
        self.alien_speed_factor = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 20
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed *= self.drop_speedup_scale
        self.alien_points = int(self.score_scale*self.alien_points)


        
        
        
        
        
        
