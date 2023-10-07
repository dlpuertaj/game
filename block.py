import pygame

import game_properties as prop


class Block(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, color): # for now it will be a square
        super().__init__()
        self.x = x_position
        self.y = y_position
        self.size = prop.FLOOR_CUBE_WIDTH
        self.image, self.rect = self.get_block(self.size,color)

    def get_block(self, size, color):
        image = pygame.Sprite()# image.load(image_filename).convert_alpha()
        image = pygame.transform.scale(image, (size, size)) 
        image.fill(color)
        rect = image.get_rect()
        rect.center = (self.x, self.y)
        return image, rect

