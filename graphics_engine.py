import pygame

import game_properties as prop

def load_floor_image(image_file_name):
    loaded_image = pygame.image.load(image_file_name)
    return pygame.transform.scale(loaded_image, (prop.FLOOR_CUBE_WIDTH, prop.FLOOR_CUBE_HEIGHT)) 


def draw_single_floor_rectangle(x, y, screen, floor_surface, floor_image):
    pygame.draw.rect(screen, (0, 255, 0), (x, y, prop.FLOOR_CUBE_WIDTH, prop.FLOOR_CUBE_HEIGHT))
    
    # Draw the image on top of the rectangle
    screen.blit(floor_surface, (x, y))

def create_single_surface_rectangle(floor_image):
    # Create a Surface object for the rectangle
    floor_surface = pygame.Surface((prop.FLOOR_CUBE_WIDTH, prop.FLOOR_CUBE_HEIGHT))
    floor_surface.set_colorkey((0, 0, 0))  # Make black transparent
    floor_surface.blit(floor_image, (0, 0))  # Draw the image on the Surface
    return floor_surface 

def draw_floor(screen, floor_image):
    num_copies = screen.get_width() // floor_image.get_width() + 1

    for i in range(num_copies):
        x = i * floor_image.get_width()  # Calculate the x position for each copy
        screen.blit(floor_image, (x, screen.get_height() - floor_image.get_width()))  # (x, y)

def draw_floor_with_surface(screen, floor_image):
    num_copies = 2 # screen.get_width() // floor_image.get_width() + 1

    for i in range(num_copies):
        x = i * floor_image.get_width()  # Calculate the x position for each copy
        y = screen.get_height() - floor_image.get_width()
        surface = create_single_surface_rectangle(floor_image)
        draw_single_floor_rectangle(x, y, screen, surface, floor_image)


