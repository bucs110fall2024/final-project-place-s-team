import pygame
from controller import Controller

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Set window size
    pygame.display.set_caption("Simple Game")
    
    controller = Controller(screen)
    controller.start_game()

if __name__ == "__main__":
    main()

