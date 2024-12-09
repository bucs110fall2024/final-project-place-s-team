import pygame

class Map:
    def __init__(self):
        self.background_color = (50, 50, 50)

    def draw(self, screen):
        screen.fill(self.background_color)

