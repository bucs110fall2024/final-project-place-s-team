import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Enemy size
        self.image.fill((255, 0, 0))  # Red color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 50
        self.attack_damage = 5
        self.speed = 2

    def chase(self, player):
        if self.rect.x < player.rect.x:
            self.rect.x += self.speed
        elif self.rect.x > player.rect.x:
            self.rect.x -= self.speed
        if self.rect.y < player.rect.y:
            self.rect.y += self.speed
        elif self.rect.y > player.rect.y:
            self.rect.y -= self.speed

    def attack(self, player):
        if self.rect.colliderect(player.rect):
            player.take_damage(self.attack_damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()



