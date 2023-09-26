import pygame
import game_properties as properties

class Character(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.vertical_velocity = 0
        self.width = width
        self.height = height
        self.image = pygame.Surface((width,height))
        self.rect = pygame.Rect(x, y, width, height)
        # self.rect.center = self.get_position()

    def get_position(self):
        return (self.x,self.y)
    
    def move_left(self):
        self.x -= properties.CHARACTER_SPEED
    
    def move_right(self):
        self.x += properties.CHARACTER_SPEED

    def update_body_position(self):
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(properties.BLUE)
        self.rect.center = (self.x, self.y)
