
import pygame
import game_properties as prop
from character import Character


def handle_movement(keys, character: Character):
    if keys[pygame.K_a]:
        character.move_left() 
    if keys[pygame.K_d]:
        character.move_right()

    # Jump
    if keys[pygame.K_SPACE] and not character.jumping: 
        character.jump()

    # Jumping (linear jump)
    character.linear_jump()

    # Crouch

    # Slide

# Function to check for collision
def is_colliding(rect1, rect2):
    return rect1.colliderect(rect2)

def simulate_gravity(character:Character):
    character.vertical_velocity += prop.GRAVITY
    character.y += character.vertical_velocity

def detect_fixed_floor_colision(character: Character):
    if character.y + prop.CHARACTER_HEIGHT >= prop.SCREEN_HEIGHT - prop.FLOOR_CUBE_HEIGHT:
        character.y = prop.SCREEN_HEIGHT - prop.FLOOR_CUBE_HEIGHT - prop.CHARACTER_HEIGHT
