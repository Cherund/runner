import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(100, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.3)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def player_animation(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        if enemy == 'fly':
            fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
            fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 200
        else:
            snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
            snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.enemy_index = 0
        self.image = self.frames[self.enemy_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def enemy_animation(self):
        self.enemy_index += 0.1
        if self.enemy_index >= len(self.frames):
            self.enemy_index = 0
        self.image = self.frames[int(self.enemy_index)]

    def update(self):
        self.enemy_animation()
        if self.rect.x > -100:
            self.rect.x -= 5
        else:
            self.kill()
