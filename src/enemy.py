import pygame
import random

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(400, 300, 50, 50)
        self.color = (255, 0, 0)
        self.speed = 3
        self.health = 50 

    def update(self):
        # Random movement for the enemy
        direction = random.choice(["left", "right", "up", "down"])
        if direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed
        elif direction == "up":
            self.rect.y -= self.speed
        elif direction == "down":
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)  # Draw the red box for the enemy

    def take_damage(self):
        # Reduce health when hit
        self.health -= 10
        if self.health <= 0:
            print("Enemy defeated!")
            self.rect.x = -100
            self.rect.y = -100

