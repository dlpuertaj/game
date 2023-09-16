import pygame

import game_properties as prop
import movement_engine as engine
import graphics_engine as graphics
from character import Character

class Game():

    def __init__(self):
        pygame.init()

        # screen_info = pygame.display.Info()

        self.screen = pygame.display.set_mode((prop.SCREEN_WIDTH, prop.SCREEN_HEIGHT))
                                              # (screen_info.current_w,screen_info.current_h))

        self.clock = pygame.time.Clock()

        self.floor_image = graphics.load_floor_image('stone.png')
        
        # Create character and the initial position in screeen
        self.character = Character((prop.SCREEN_WIDTH - prop.CHARACTER_WIDTH) // 2, 
                                   prop.SCREEN_HEIGHT - prop.CHARACTER_HEIGHT - prop.FLOOR_CUBE_HEIGHT,
                                   prop.CHARACTER_WIDTH, prop.CHARACTER_HEIGHT)  
        

    def run(self):
        running = True

        while running:

            self.clock.tick(prop.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen with the background color
            self.screen.fill(prop.BLACK)
            
            # Draw the floor rectangle using pygame.draw.rect
            graphics.draw_floor_with_surface(self.screen, self.floor_image)

            # Handle key presses
            keys = pygame.key.get_pressed()
            engine.handle_movement(keys, self.character)
            
            
            # Boundary checks to prevent the character from going out of bounds
            self.character.x = max(0, min(self.character.x, prop.SCREEN_WIDTH - prop.CHARACTER_WIDTH))
            self.character.y = max(0, min(self.character.y, prop.SCREEN_HEIGHT - prop.CHARACTER_HEIGHT))

            # Check if the character is standing on the floor
            engine.detect_fixed_floor_colision(self.character)
            # if self.character.y + properties.CHARACTER_HEIGHT >= properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT:
                # self.character.y = properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT

            # Draw the character (a simple square)
            pygame.draw.rect(self.screen, prop.RED, (self.character.x, self.character.y, prop.CHARACTER_WIDTH, prop.CHARACTER_HEIGHT))

            # engine.simulate_gravity(self.character)

            pygame.display.flip()

        pygame.quit()