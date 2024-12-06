import pygame
import random
import math

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))  # Enemy size
        self.image.fill((255, 0, 0))  # Red color for the enemy
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 2

    def update(self, player, screen_width, screen_height):
        # AI: Chase the player if within range
        player_pos = player.rect.center
        enemy_pos = self.rect.center
        distance = math.hypot(player_pos[0] - enemy_pos[0], player_pos[1] - enemy_pos[1])

        # If player is close enough, chase them
        if distance < 300:
            direction_x = player_pos[0] - enemy_pos[0]
            direction_y = player_pos[1] - enemy_pos[1]
            angle = math.atan2(direction_y, direction_x)
            self.rect.x += int(self.speed * math.cos(angle))
            self.rect.y += int(self.speed * math.sin(angle))

        # Boundaries check
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def attack(self, player):
        # Placeholder attack logic when in range
        if self.rect.colliderect(player.rect):
            print("Enemy attacks the player!")