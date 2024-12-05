import pygame
from src.player import Player
from src.enemy import Enemy
from src.map import Map

class Controller:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('RPG Game')
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_over = False
        self.player = Player(100, 100)
        self.enemies = pygame.sprite.Group(Enemy(200, 200), Enemy(300, 300))
        self.all_sprites = pygame.sprite.Group(self.player, *self.enemies)
        self.map = Map('map.txt')
        self.font = pygame.font.SysFont(None, 36)

    def start_menu(self):
        while not self.game_over:
            self.screen.fill((0, 0, 0))
            title = self.font.render('Start Game', True, (255, 255, 255))
            self.screen.blit(title, (300, 250))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.run_game()

    def run_game(self):
        while self.running:
            self.screen.fill((0, 0, 0))
            self.map.draw(self.screen)
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            self.player.attack(self.enemies)
            self.enemies.update()
            for enemy in self.enemies:
                enemy.chase(self.player)
                enemy.attack(self.player)
            self.all_sprites.draw(self.screen)

            if self.player.health <= 0:
                self.game_over_menu()

            pygame.display.flip()
            self.clock.tick(60)

    def game_over_menu(self):
        self.screen.fill((0, 0, 0))
        game_over_text = self.font.render('Game Over', True, (255, 0, 0))
        self.screen.blit(game_over_text, (300, 250))
        pygame.display.flip()
        pygame.time.delay(2000)
        self.running = False

    def start(self):
        self.start_menu()

if __name__ == '__main__':
    controller = Controller()
    controller.start()