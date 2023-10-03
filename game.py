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

        self.floor_cubes = graphics.get_floor_objects(self.screen)
        
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

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and len(collisions) > 0:
                        self.character.jump()

            # ---- Logical Updates ----

            # Handle key presses
            keys = pygame.key.get_pressed()
            self.character.move(keys)
            
            # Create the floor rectangles anf groups for collision
             
            
            floor_group = pygame.sprite.Group(self.floor_cubes)

            # spritecollide for collision using groups
            collisions = pygame.sprite.spritecollide(self.character, floor_group, False)
            
            if self.character.velocity.y > 0:
                if len(collisions) > 0:
                    self.character.velocity.y = 0
                    self.character.position.y = collisions[0].rect.top + 1                

            self.character.velocity.y += prop.GRAVITY

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