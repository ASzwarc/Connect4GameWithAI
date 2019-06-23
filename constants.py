"""
Definiton of constanst for game
"""
# Color definition for game
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
SQUARE_SIZE = 100
MESSAGE_PROMPT_SIZE = 100
# TODO document magic number 5. Why it's 5 and not other number?
RADIUS = int(SQUARE_SIZE / 2 - 5)
# Board parameters
# TODO consider moving it to Board class that will handle board related stuff
ROW_COUNT = 6
COLUMN_COUNT = 7

SCREEN_WIDTH = COLUMN_COUNT * SQUARE_SIZE
SCREEN_HEIGHT = ROW_COUNT * SQUARE_SIZE
