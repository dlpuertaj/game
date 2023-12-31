# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "My Awesome Game"
SCROLL_AREA_WIDTH = 500
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
CHARACTER_WIDTH = 50
CHARACTER_HEIGHT = 50
CHARACTER_JUMP_FORCE = -20

# Define jump variables
CHARACTER_PEAK_HEIGHT = 100  # Adjust this value to control jump height
CHARACTER_JUMP_DURATION = 100

# Floor settings
FLOOR_CUBE_WIDTH = 100
FLOOR_CUBE_HEIGHT = 100
FLOOR_CUBE_Y_POSITION = SCREEN_HEIGHT - FLOOR_CUBE_HEIGHT // 2
FLOOR_CUBE_GENERATE_DISTANCE = FLOOR_CUBE_WIDTH * 2
# Gravity
GRAVITY = 0.8
ACCELERATION = 0.7
FRICTION = -0.12
