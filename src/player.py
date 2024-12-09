import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 50, 50)
        self.color = (0, 128, 255)
        self.speed = 5
        self.attack_range = pygame.Rect(self.rect.x - 10, self.rect.y - 10, self.rect.width + 20, self.rect.height + 20)
        self.is_attacking = False

    def update(self):
        keys = pygame.key.get_pressed()

        # Arrow key movement
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Attack with space
        if keys[pygame.K_SPACE]:
            self.attack()

    def attack(self):
        self.is_attacking = True
        self.attack_range.x = self.rect.x - 10
        self.attack_range.y = self.rect.y - 10

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # Draws the blue player box on screen

        if self.is_attacking:
            pygame.draw.rect(screen, (255, 255, 0), self.attack_range, 2)  # Show attack range as a yellow outline
            self.is_attacking = False

    def check_attack_collision(self, enemy):
        # Checks if enemy is in attack range
        if self.attack_range.colliderect(enemy.rect):
            enemy.take_damage()

