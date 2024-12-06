# import pygame


# class Map:
#     def __init__(screen, map_data):
#         f = open('map.txt', 'r')
#         map_data = f.readlines()
#         f.close()
#         for y, row in enumerate(map_data):
#             for x, tile in enumerate(row):
#                     tile_size = 32
#                     wall_image = pygame.image.load('assets/wall.png')
#                     floor_image = pygame.image.load('assets/floor.png')
#             if tile == 'x':
#                     screen.blit(wall_image, (x * tile_size, y * tile_size))
#             elif tile == '.':
#                     screen.blit(floor_image, (x * tile_size, y * tile_size))