import pygame

import game_properties as properties

class Game():

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((properties.SCREEN_WIDTH,properties.SCREEN_HEIGHT))
        
        self.clock = pygame.time.Clock()
        
        self.floor_image = pygame.image.load('stone.png')
        
        self.floor_image = pygame.transform.scale(self.floor_image, (properties.FLOOR_CUBE_WIDTH, properties.FLOOR_CUBE_HEIGHT))

        self.num_copies = self.screen.get_width() // self.floor_image.get_width() + 1

        # Define character properties
        self.character_x = (properties.SCREEN_WIDTH - properties.CHARACTER_WIDTH) // 2
        self.character_y = properties.SCREEN_HEIGHT - properties.CHARACTER_HEIGHT - properties.FLOOR_CUBE_HEIGHT  # Position the character on top of the floor


    def run(self):
        running = True

        # Define jump variables
        jumping = False
        jump_start_y = 50
        jump_peak_height = 200 

        while running:

            self.clock.tick(properties.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen with the background color
            self.screen.fill(properties.BLACK)
            # Draw the floor
            # screen.blit(floor_image,(0,500))
            # pygame.draw.rect(screen, BLUE, (0, 550, 800, 50))  # (x, y, width, height)

            for i in range(self.num_copies):
                x = i * self.floor_image.get_width()  # Calculate the x position for each copy
                self.screen.blit(self.floor_image, (x, self.screen.get_height() - self.floor_image.get_width()))  # (x, y)


            # Handle key presses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.character_x -= properties.CHARACTER_SPEED 
            if keys[pygame.K_d]:
                self.character_x += properties.CHARACTER_SPEED 


            # Optional: Add jump mechanics
            # if keys[pygame.K_SPACE] and self.character_y >= properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT:
                # Apply an upward force to simulate jumping
                # self.character_y -= properties.CHARACTER_JUMP_FORCE  # You'll need to define jump_force

            # Handle key presses
            if keys[pygame.K_SPACE] and not jumping:
                jumping = True
                jump_speed = -20  # Adjust this value to control jump speed


            # Jumping (linear jump)
            if jumping:
                self.character_y += jump_speed
                jump_speed += properties.GRAVITY  # Apply gravity to the jump speed

                # Check if the character has reached the ground
                if self.character_y >= properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT:
                    self.character_y = properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT
                    jumping = False

                    # Apply gravity to the character's vertical position
                    self.character_y += properties.GRAVITY

            
            # Boundary checks to prevent the character from going out of bounds
            self.character_x = max(0, min(self.character_x, properties.SCREEN_WIDTH - properties.CHARACTER_WIDTH))
            self.character_y = max(0, min(self.character_y, properties.SCREEN_HEIGHT - properties.CHARACTER_HEIGHT))

            # Check if the character is standing on the floor
            if self.character_y + properties.CHARACTER_HEIGHT >= properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT:
                self.character_y = properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT

            # Draw the character (a simple square)
            pygame.draw.rect(self.screen, properties.RED, (self.character_x, self.character_y, properties.CHARACTER_WIDTH, properties.CHARACTER_HEIGHT))


            pygame.display.update()

        pygame.quit()