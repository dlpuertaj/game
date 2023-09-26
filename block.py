import pygame


class Block(pygame.sprite.Sprite):
    def __init__(self, x_position, y_position, size): # for now it will be a square
        super().__init__()
        self.x = x_position
        self.y = y_position
        self.size = size
        self.image, self.rect = self.get_block(size,"Stone.png")

    def get_block(self, size, image_filename):
        image = pygame.image.load(image_filename).convert_alpha()
        image = pygame.transform.scale(image, (size, size)) 
        rect = image.get_rect()
        rect.center = (self.x, self.y)
        return image, rect

