import pygame

import game_properties as prop
import movement_engine as engine
import graphics_engine as graphics

from background import Background
from character import Character
from block import Block

class Game():

    def __init__(self):
        pygame.init()

        # screen_info = pygame.display.Info()

        self.screen = pygame.display.set_mode((prop.SCREEN_WIDTH, prop.SCREEN_HEIGHT)) # This is also a surface
                                              # (screen_info.current_w,screen_info.current_h))

        self.background = Background()

        self.clock = pygame.time.Clock()

        self.scroll_offset_x = 0

        self.floor_cubes = pygame.sprite.Group(graphics.get_floor_objects())
        
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
            self.character.move()
            
            # Create the floor rectangles anf groups for collision
            # floor_group = pygame.sprite.Group(self.floor_cubes)

            # spritecollide for collision using groups
            collisions = pygame.sprite.spritecollide(self.character, self.floor_cubes, False)
            
            if self.character.velocity.y > 0:
                if len(collisions) > 0:
                    self.character.velocity.y = 0
                    self.character.position.y = collisions[0].rect.top + 1                

            self.character.velocity.y += prop.GRAVITY

            # ---- Fill the screen ----

            # Clear the screen with the background color
            self.screen.fill(prop.WHITE)
                      
            # self.background.update()
            # self.background.render(self.screen)
            # Draw the character (a simple square)
            self.screen.blit(self.character.surface, (self.character.rect.x - self.scroll_offset_x, self.character.rect.y))

            # Draw floor
            for floor_cube in self.floor_cubes:
                self.screen.blit(floor_cube.image, (floor_cube.rect.x - self.scroll_offset_x, floor_cube.rect.y))
            # all_objects_group.draw(self.screen)
            
           
            if( (self.character.rect.right - self.scroll_offset_x >= prop.SCREEN_WIDTH - prop.SCROLL_AREA_WIDTH) and self.character.velocity.x > 0
                or (self.character.rect.left - self.scroll_offset_x <= prop.SCROLL_AREA_WIDTH) and self.character.velocity.x < 0):
                self.scr
                oll_offset_x += self.character.velocity.x

                x = self.floor_cubes[len(self.floor_cubes) - 1].rect.x + prop.FLOOR_CUBE_WIDTH *2 # Calculate the x position for each copy
                
                tail_block = self.floor_cubes.pop(0) # get the block from index 0
                tail_block.rect.x = x # update x position 
                self.floor_cubes.append(tail_block) # add block to the top of the list
                
            pygame.display.update()
            self.clock.tick(prop.FPS)

        pygame.quit()