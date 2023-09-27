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
        self.position = pygame.math.Vector2((50, 150))
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.Vector2(0, 0)


    def move(self, keys):
        self.acceleration = pygame.math.Vector2(0,0)

        if keys[pygame.K_LEFT]:
            self.acceleration.x = -prop.ACCELERATION
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = prop.ACCELERATION

        self.acceleration.x += self.velocity.x * prop.FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration

        """
        if self.position.x > screen.WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = screen.WIDTH
        """

        self.rect.midbottom = self.position

    """def update_body_position(self):
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill(prop.BLUE)
        self.rect.center = (self.x, self.y)"""
