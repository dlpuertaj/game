import pygame
import game_properties as prop

class Character(pygame.sprite.Sprite):

    def __init__(self,x, y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.surface = pygame.Surface((width,height))
        self.surface.fill(prop.RED)
        self.rect = self.surface.get_rect()

        # Vectors
        self.position = pygame.math.Vector2((x, y))
        self.velocity = pygame.math.Vector2(prop.CHARACTER_SPEED, prop.GRAVITY)
        self.acceleration = pygame.math.Vector2(0, 0)


    def move(self):
        self.acceleration.x = prop.ACCELERATION
        self.acceleration.x += self.velocity.x * prop.FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        self.rect.midbottom = self.position

    def jump(self):
        self.velocity.y = prop.CHARACTER_JUMP_FORCE

