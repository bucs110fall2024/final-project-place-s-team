import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Player size
        self.image.fill((0, 128, 255))  # Blue color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.attack_damage = 10
        self.heal_amount = 20
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def attack(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.attack_damage)

    def heal(self):
        self.health += self.heal_amount
        if self.health > 100:
            self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0




# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# PLAYER_SPEED = 5
# HEALTH_MAX = 100
# HEALTH_MIN = 0

# class Player(pygame.sprite.Sprite):
#     def __init__(self, x, y):
#         super().__init__()
#         self.image = pygame.Surface((50, 50))
#         self.image.fill((0, 255, 0))  # Green player square
#         self.rect = self.image.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.health = HEALTH_MAX
#         self.attack_damage = 10

#     def move(self, keys):
#         """Move player."""
#         if keys[pygame.K_LEFT] and self.rect.x > 0:
#             self.rect.x -= PLAYER_SPEED
#         if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
#             self.rect.x += PLAYER_SPEED
#         if keys[pygame.K_UP] and self.rect.y > 0:
#             self.rect.y -= PLAYER_SPEED
#         if keys[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - self.rect.height:
#             self.rect.y += PLAYER_SPEED

#     def attack(self, enemies):
#         """Attack enemies."""
#         for enemy in enemies:
#             if self.rect.colliderect(enemy.rect):
#                 enemy.take_damage(self.attack_damage)

#     def take_damage(self, damage):
#         """Player takes damage."""
#         self.health -= damage
#         if self.health < HEALTH_MIN:
#             self.health = HEALTH_MIN
#         print(f"Player health: {self.health}")

#     def heal(self, amount):
#         """Heal the player."""
#         self.health += amount
#         if self.health > HEALTH_MAX:
#             self.health = HEALTH_MAX
#         print(f"Player health: {self.health}")

#     def update(self, keys, enemies):
#         """Update the player's state (movement and attacks)."""
#         self.move(keys)
#         if keys[pygame.K_SPACE]:  # Attack when space is pressed
#             self.attack(enemies)