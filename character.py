import game_properties as properties

class Character:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.vertical_velocity = 0
        self.width = width
        self.height = height
        self.jumping = False
        self.jump_speed = 0

    def get_position(self):
        return (self.x,self.y)
    
    def move_left(self):
        self.x -= properties.CHARACTER_SPEED
    
    def move_right(self):
        self.x += properties.CHARACTER_SPEED

    def jump(self):
        self.jumping = True
        self.jump_speed = properties.CHARACTER_JUMP_SPEED

    def linear_jump(self):
        # Jumping (linear jump)
        if self.jumping:
            self.y += self.jump_speed
            self.jump_speed += properties.GRAVITY  # Apply gravity to the jump speed
        # Check if the character has reached the ground
        if self.y >= properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT:
            self.y = properties.SCREEN_HEIGHT - properties.FLOOR_CUBE_HEIGHT - properties.CHARACTER_HEIGHT
            self.jumping = False

            # Apply gravity to the character's vertical position
            self.y += properties.GRAVITY