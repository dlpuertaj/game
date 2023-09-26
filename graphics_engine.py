import pygame
from block import Block

import game_properties as prop

def load_floor_image(image_file_name):
    loaded_image = pygame.image.load(image_file_name).convert_alpha()
    return pygame.transform.scale(loaded_image, (prop.FLOOR_CUBE_WIDTH, prop.FLOOR_CUBE_HEIGHT)) 

def get_floor(screen, floor_image):
    num_copies = 2 # screen.get_width() // floor_image.get_width() + 1
    list = []
    for i in range(num_copies):
        x = i * floor_image.get_width()  # Calculate the x position for each copy
        y = screen.get_height() - floor_image.get_width()
        rect = floor_image.get_rect()
        rect.center = (x,y) # Position of the rectangle
        list.append(rect)
    
    return list

def get_floor_objects(screen):
    num_copies = 1 # screen.get_width() // floor_image.get_width() + 1
    list = []
    for i in range(1,num_copies + 1):
        x = i * (prop.FLOOR_CUBE_WIDTH // 2)  # Calculate the x position for each copy
        y = screen.get_height() - (prop.FLOOR_CUBE_WIDTH // 2)
        block = Block(x, y, prop.FLOOR_CUBE_WIDTH)
        list.append(block)
    
    return list
