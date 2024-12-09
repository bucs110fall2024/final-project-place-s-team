import pygame
from src.player import Player
from src.enemy import Enemy
from src.map import Map

class Controller:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False

    def start_game(self):
        while self.running:
            if self.game_over:
                self.game_over_screen()
            else:
                self.main_game_loop()

    def main_game_loop(self):
        player = Player()
        enemy = Enemy()
        game_map = Map()
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.game_over = True

            self.screen.fill((0, 0, 0))
            game_map.draw(self.screen)
            player.update()
            player.draw(self.screen)
            enemy.update()
            enemy.draw(self.screen)

            # Check for attack collision
            player.check_attack_collision(enemy)

            pygame.display.flip()
            self.clock.tick(60)

    def game_over_screen(self):
        font = pygame.font.SysFont("Arial", 36)
        game_over_text = font.render("Game Over! Press ESC to exit", True, (255, 255, 255))
        self.screen.blit(game_over_text, (200, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    self.game_over = False

