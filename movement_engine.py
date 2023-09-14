
import pygame
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