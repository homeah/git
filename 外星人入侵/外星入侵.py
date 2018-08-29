import pygame
from setting import Setting
from ship import Ship
from alien import Alien
from pygame.sprite import Group
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard

def run_game():
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    pygame.display.set_caption('外星人入侵')
    ship = Ship(ai_setting,screen)
    #alien = Alien(ai_setting,screen)
    bullets = Group()
    aliens = Group()
    play_button = Button(ai_setting,screen,"Play")
    stats = GameStats(ai_setting)
    gf.create_fleet(ai_setting,screen,aliens,ship)
    sb = ScoreBoard(ai_setting,screen,stats)

    while True:
        gf.check_events(ai_setting,screen,ship,bullets,stats,play_button,aliens,sb)
        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets,aliens,ai_setting,screen,ship,sb,stats)
            gf.update_aliens(aliens,ai_setting,ship,bullets,stats,screen,sb)
        gf.update_screen(ai_setting,screen,ship,bullets,aliens,stats,play_button,sb)
run_game()
            

