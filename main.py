import pygame
from sys import exit
from random import choice
from Player_Enemies import Player,  Enemy


def display_score():
    current_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surface = test_font.render(f'Score: {current_time}', False, 'black')
    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time


def collision():
    if pygame.sprite.spritecollide(player.sprite, enemies, False):
        enemies.empty()
        return False
    else:
        return True


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

music = pygame.mixer.Sound('audio/music.wav')
music.play(loops=-1)

# Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

enemies = pygame.sprite.Group()

# Intro screen
player_front = pygame.transform.scale2x(pygame.image.load('graphics/Player/player_stand.png').convert_alpha())
player_front_rect = player_front.get_rect(center=(400, 200))

intro_logo = test_font.render('Pixel Runner', False, 'lightblue')
logo_rect = intro_logo.get_rect(center=(400, 70))

intro_text = test_font.render('Press space to run', False, 'lightblue')
text_rect = intro_text.get_rect(center=(400, 330))

# Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                enemies.add(Enemy(choice(['fly', 'snail', 'snail'])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        player.draw(screen)
        player.update()

        enemies.draw(screen)
        enemies.update()

        # Collision
        game_active = collision()

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_front, player_front_rect)
        screen.blit(intro_logo, logo_rect)

        player_gravity = 0

        if score == 0:
            screen.blit(intro_text, text_rect)
        else:
            score_message = test_font.render(f'Your score: {score}', False, 'lightblue')
            score_rect = score_message.get_rect(center=(400, 330))
            screen.blit(score_message, score_rect)

    pygame.display.update()
    clock.tick(60)
