import pygame

import game_properties as prop
import movement_engine as engine
import graphics_engine as graphics
from character import Character

class Game():

    def __init__(self):
        pygame.init()

        # screen_info = pygame.display.Info()

        self.screen = pygame.display.set_mode((prop.SCREEN_WIDTH, prop.SCREEN_HEIGHT)) # This is also a surface
                                              # (screen_info.current_w,screen_info.current_h))

        self.clock = pygame.time.Clock()
        
        # Create character and the initial position in screeen
        self.character = Character((prop.CHARACTER_WIDTH // 2),prop.CHARACTER_WIDTH, prop.CHARACTER_WIDTH, prop.CHARACTER_HEIGHT)  
        

    def run(self):
        running = True

        #is_colliding = False 

        while running:
            
            # ---- Check for events ----

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # ---- Logical Updates ----

            # Handle key presses
            keys = pygame.key.get_pressed()
            self.character.move(keys)
            
            # Create the floor rectangles anf groups for collision
            floor_objects = graphics.get_floor_objects(self.screen) 
            
            floor_group = pygame.sprite.Group(floor_objects)

            # spritecollide for collision using groups
            colliding = pygame.sprite.spritecollide(self.character, floor_group, False)
            
            if len(colliding) > 0:
                self.character.position.y = colliding[0].rect.top + 1
                self.character.velocity.y = 0
                self.character.surface.fill(prop.BLUE)
            else:
                self.character.velocity.y = prop.GRAVITY

            
            # Boundary checks to prevent the character from going out of bounds
            # self.character.x = max(0, min(self.character.x, prop.SCREEN_WIDTH - prop.CHARACTER_WIDTH))
            # self.character.y = max(0, min(self.character.y, prop.SCREEN_HEIGHT - prop.CHARACTER_HEIGHT))
            
                                    
            # ---- Fill the screen ----

            # Clear the screen with the background color
            self.screen.fill(prop.WHITE)
                      
            # Draw the character (a simple square)
            #pygame.draw.rect(self.screen, prop.RED, self.character.rect)

            # Draw floor
            floor_group.draw(self.screen)
            # all_objects_group.draw(self.screen)
            
            self.screen.blit(self.character.surface, self.character.rect)
           
            pygame.display.update()
            self.clock.tick(prop.FPS)

        pygame.quit()