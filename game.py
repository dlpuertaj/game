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

        # self.background = Background() no background for now

        self.clock = pygame.time.Clock()

        self.camera_offset_x = 0
        self.camera_reference_x = prop.CHARACTER_WIDTH

        self.floor_blocks = pygame.sprite.Group(graphics.get_floor_objects())
        
        # Create character and the initial position in the screeen
        self.character = Character(0,0, prop.CHARACTER_WIDTH, prop.CHARACTER_HEIGHT)

        # Create ghost for camera scrolling
        self.ghost = Character(0,prop.CHARACTER_WIDTH,prop.CHARACTER_WIDTH, prop.CHARACTER_HEIGHT)
        self.ghost.velocity.y = 0

        self.color_index = 0

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

            # spritecollide for collision using groups
            collisions = pygame.sprite.spritecollide(self.character, self.floor_blocks, False)
            
            if collisions:
                self.character.velocity.y = 0
                self.character.position.y = collisions[0].rect.top + 1 

            # ---- Logical Updates ----

            # Handle key presses
            self.character.move()
            self.ghost.move()
            self.camera_offset_x = self.ghost.rect.centerx - self.ghost.rect.width // 2

            
            print("Blocks: " + str(len(self.floor_blocks)))
            for block in self.floor_blocks:
                if block.rect.right < self.camera_offset_x:
                    block.kill()         

                    self.color_index = 1 - self.color_index  # Alternate between 0 (black) and 1 (gray)
                    color = (0, 0, 0) if self.color_index == 0 else (128, 128, 128)      
            
                    # generate new floor blocks
                    last_block = self.floor_blocks.sprites()[len(self.floor_blocks) - 1].rect
                    
                    new_block_x = last_block.centerx + (prop.CHARACTER_WIDTH * 2)
                    new_block = Block(new_block_x , prop.FLOOR_CUBE_Y_POSITION,color) # Bug
                    self.floor_blocks.add(new_block)

            self.character.velocity.y += prop.GRAVITY

            # ---- Fill the screen ----

            # Clear the screen with the background color
            self.screen.fill(prop.WHITE)
                      
            # Draw the character (a simple square)
            self.screen.blit(self.character.surface, (self.character.rect.x - self.camera_offset_x, self.character.rect.y))

            # Draw floor
            for floor_cube in self.floor_blocks:
                self.screen.blit(floor_cube.image, (floor_cube.rect.x - self.camera_offset_x, floor_cube.rect.y))
                
            
            pygame.draw.rect(self.screen, (255,0,0), (self.ghost.rect.x - self.camera_offset_x, self.ghost.rect.y, 
                                                     self.ghost.rect.width, self.ghost.rect.height), 1, border_radius=1)


            pygame.display.update()
            self.clock.tick(prop.FPS)

        pygame.quit()