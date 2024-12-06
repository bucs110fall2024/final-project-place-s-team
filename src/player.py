# import pygame

# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((50, 50))  # Player size
#         self.image.fill((0, 128, 255))  # Blue color
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.health = 100
#         self.attack_damage = 10
#         self.heal_amount = 20
#         self.speed = 5

#     def move(self, keys):
#         if keys[pygame.K_LEFT]:
#             self.rect.x -= self.speed
#         if keys[pygame.K_RIGHT]:
#             self.rect.x += self.speed
#         if keys[pygame.K_UP]:
#             self.rect.y -= self.speed
#         if keys[pygame.K_DOWN]:
#             self.rect.y += self.speed

#     def attack(self, enemies):
#         for enemy in enemies:
#             if self.rect.colliderect(enemy.rect):
#                 enemy.take_damage(self.attack_damage)

#     def heal(self):
#         self.health += self.heal_amount
#         if self.health > 100:
#             self.health = 100

#     def take_damage(self, amount):
#         self.health -= amount
#         if self.health <= 0:
#             self.health = 0

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))  # Player size
        self.image.fill((0, 255, 0))  # Green color for the player
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self, keys, screen_width, screen_height):
        # Movement with arrow keys
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.y += self.speed

    def attack(self):
        # Placeholder attack logic
        print("Player attacks!")