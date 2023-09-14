import pygame

import game_properties as properties
import movement_engine as engine
from character import Character

class Game():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((properties.SCREEN_WIDTH,properties.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.floor_image = pygame.image.load('stone.png')
        self.floor_image = pygame.transform.scale(self.floor_image, (properties.FLOOR_CUBE_WIDTH, properties.FLOOR_CUBE_HEIGHT))
        self.num_copies = self.screen.get_width() // self.floor_image.get_width() + 1

        # Create character and the initial position in screeen
        self.character = Character((properties.SCREEN_WIDTH - properties.CHARACTER_WIDTH) // 2, 
                                   properties.SCREEN_HEIGHT - properties.CHARACTER_HEIGHT - properties.FLOOR_CUBE_HEIGHT,
                                   properties.CHARACTER_WIDTH, properties.CHARACTER_HEIGHT)  

    def run(self):
        running = True

        while running:

            self.clock.tick(properties.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen with the background color
            self.screen.fill(properties.BLACK)
            
            # Draw the floor
            for i in range(self.num_copies):
                x = i * self.floor_image.get_width()  # Calculate the x position for each copy
                self.screen.blit(self.floor_image, (x, self.screen.get_height() - self.floor_image.get_width()))  # (x, y)


            # Handle key presses
            keys = pygame.key.get_pressed()
            engine.handle_movement(keys, self.character)
            
            
            # Boundary checks to prevent the character from going out of bounds
            self.character.x = max(0, min(self.character.x, properties.SCREEN_WIDTH - properties.CHARACTER_WIDTH))
            self.character.y = max(0, min(self.character.y, properties.SCREEN_HEIGHT - properties.CHARACTER_HEIGHT))

            # Check if the character is standing on the floor
            if self.character.y + properties.CHARACTER_HEIGHT >= properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT:
                self.character.y = properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT

            # Draw the character (a simple square)
            pygame.draw.rect(self.screen, properties.RED, (self.character.x, self.character.y, properties.CHARACTER_WIDTH, properties.CHARACTER_HEIGHT))


            pygame.display.update()

        pygame.quit()