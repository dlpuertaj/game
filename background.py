import pygame


class Background():
    
    def __init__(self) -> None:
        self.image = pygame.image.load("background.png")
        self.rect = self.image.get_rect()

        self.y1 = 0
        self.x1 = 0
 
        self.y2 = 0
        self.x2 = self.rect.width
 
        self.moving_speed = 5

    def update(self):
        self.x1 -= self.moving_speed    
        self.x2 -= self.moving_speed

        if self.x1 <= -self.rect.width:
            self.x1 = self.rect.width

        if self.x2 <= -self.rect.width:
            self.x2 = self.rect.width

    def render(self, screen):
      screen.blit(self.image, (self.x1, self.y1))
      screen.blit(self.image, (self.x2, self.y2))
    