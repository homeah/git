import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from pygame.locals import *

def check_keydown_events(event,ship,screen,bullets,ai_setting):
    '''响应按键'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets,ai_setting,screen,ship)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

def fire_bullet(bullets,ai_setting,screen,ship):
    if len(bullets) <ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting,screen,ship)
        bullets.add(new_bullet)


def check_keyup_events(event,ship):
    '''响应松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
def check_events(ai_setting,screen,ship,bullets,stats,play_button,aliens,sb):
    '''响应按键和鼠标事件'''
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship,screen,bullets,ai_setting)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,ai_setting,screen,ship,aliens,bullets,sb)

def check_play_button(stats,play_button,mouse_x,mouse_y,ai_setting,screen,ship,aliens,bullets,sb):
    if play_button.rect.collidepoint(mouse_x,mouse_y) and stats.game_active == False:
        stats.reset_stats()
        stats.game_active = True
        sb.prep_score()
        sb.prep_level()
        sb.prep_ships()
        sb.prep_high_score()
        pygame.mouse.set_visible(False) #游戏结束后鼠标不可见
        ai_setting.initialize_setting()

        aliens.empty()
        bullets.empty()

        create_fleet(ai_setting,screen,aliens,ship)
        ship.center_ship()
               

def update_screen(ai_setting,screen,ship,bullets,aliens,stats,play_button,sb):
    '''更新屏幕'''
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    #alien.blitme()
    if not stats.game_active:
        play_button.draw_button()
        
    pygame.display.flip()

def update_bullets(bullets,aliens,ai_setting,screen,ship,sb,stats):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    collisions =pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setting.alien_points*len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
        play_music("sound/explode.wav")  
    if len(aliens) == 0:
        bullets.empty()
        stats.level += 1  #消灭敌人一次后升一级
        play_music("sound/success.wav")
        sleep(4)
        sb.prep_level()
        ai_setting.increase_speed()
        create_fleet(ai_setting,screen,aliens,ship)

def update_aliens(aliens,ai_setting,ship,bullets,stats,screen,sb):
    check_aliens_bottom(ai_setting,stats,screen,ship,aliens,bullets,sb)
    check_fleet_edges(ai_setting,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_setting,stats,screen,ship,aliens,bullets,sb)

def check_fleet_edges(ai_setting,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_setting,aliens)
            break

def change_fleet_direction(ai_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= (-1)
    
def check_aliens_bottom(ai_setting,stats,screen,ship,aliens,bullets,sb):
    #外星人是否到底
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting,stats,screen,ship,aliens,bullets,sb)
            break

def get_number_aliens_x(ai_setting,alien_width):
    available_space_x = ai_setting.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def get_number_rows(ai_setting,ship_height,alien_height):
    #计算容纳多少行外星人
    available_space_y = (ai_setting.screen_height-3*alien_height-2*ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows
    
def creat_alien(ai_setting,screen,aliens,alien_number,row_number):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number+20
    aliens.add(alien)
    

def create_fleet(ai_setting,screen,aliens,ship):
    #创建外星人群，外星人间距为外星人宽度
    alien = Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
    number_rows = get_number_rows(ai_setting,ship.rect.height,alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_setting,screen,aliens,alien_number,row_number)

    
def ship_hit(ai_setting,stats,screen,ship,aliens,bullets,sb):
    if stats.ship_left>0:
        stats.ship_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        play_music("sound/fail.wav")
        sleep(2.3)
        
        create_fleet(ai_setting,screen,aliens,ship)
        ship.center_ship()
 
    else:
        stats.game_active = False
        play_music("sound/total_fail.wav")
        sleep(3.5)
        ai_setting.initialize_setting()
        pygame.mouse.set_visible(True) #游戏结束后鼠标可见

def check_high_score(stats,sb):
    #检查最高得分
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def play_music(music):
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()


        
        
