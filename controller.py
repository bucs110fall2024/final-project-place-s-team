import pygame
import sys
import random
from src.player import Player
from src.enemy import Enemy

class Controller:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Dungeon Quest")
        self.clock = pygame.time.Clock()
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        # Create player instance
        self.player = Player(self.screen_width // 2, self.screen_height // 2)
        self.all_sprites.add(self.player)

    def start_menu(self):
        font = pygame.font.SysFont('Arial', 36)
        start_text = font.render("Press ENTER to Start", True, (255, 255, 255))
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.game_loop()

            self.screen.fill((0, 0, 0))
            self.screen.blit(start_text, (self.screen_width // 2 - start_text.get_width() // 2, self.screen_height // 2))
            pygame.display.flip()
            self.clock.tick(60)

    def game_loop(self):
        self.running = True
        score = 0
        font = pygame.font.SysFont('Arial', 24)

        while self.running:
            keys = pygame.key.get_pressed()
            self.player.update(keys, self.screen_width, self.screen_height)

            # Spawn enemies randomly
            if random.random() < 0.02:  # Spawn chance per frame
                enemy = Enemy(random.randint(0, self.screen_width), random.randint(0, self.screen_height))
                self.enemies.add(enemy)
                self.all_sprites.add(enemy)

            # Update all sprites
            self.all_sprites.update(self.player, self.screen_width, self.screen_height)

            # Check for collision (player vs enemies)
            for enemy in self.enemies:
                if enemy.rect.colliderect(self.player.rect):
                    enemy.attack(self.player)
                    score -= 1  # Decrease score when attacked by enemy

            # Render the game
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)

            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))

            pygame.display.flip()
            self.clock.tick(60)

            # Handle game over condition
            if score < -10:  # Example game over condition
                self.game_over(score)

    def game_over(self, score):
        font = pygame.font.SysFont('Arial', 36)
        game_over_text = font.render(f"Game Over! Score: {score}", True, (255, 0, 0))
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.start_menu()

            self.screen.fill((0, 0, 0))
            self.screen.blit(game_over_text, (self.screen_width // 2 - game_over_text.get_width() // 2, self.screen_height // 2))
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    controller = Controller()
    controller.start_menu()
    pygame.quit()
    sys.exit()
