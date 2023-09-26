import pygame


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, x_position, y_position, width, height, name=None):
        super().__init__()
        self.shape = pygame.Rect(x_position,y_position,width,height)
        
        # SRCALPHA the pixel format will include a per-pixel alpha
        self.surface = pygame.Surface((width,height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, screen):
        screen.blit(self.surface, (self.shape.x, self.shape.y))