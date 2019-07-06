"""
Definiton of constanst for game
"""
# Color definition for game
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
CIRCLE_DIAMETER = 100
MESSAGE_PROMPT_SIZE = 100
# TODO document magic number 5. Why it's 5 and not other number?
RADIUS = int(CIRCLE_DIAMETER / 2 - 5)
# Board parameters
# TODO consider moving it to Board class that will handle board related stuff
ROW_COUNT = 6
COLUMN_COUNT = 7
FONT_SIZE = 65
FONT_TYPE = "monospace"
MS_BEFORE_EXIT = 3000

HUMAN = 1
AI = 2

MINIMAX_DEPTH = 4
WINDOW_LENGTH = 4

SCREEN_WIDTH = COLUMN_COUNT * CIRCLE_DIAMETER
SCREEN_HEIGHT = ROW_COUNT * CIRCLE_DIAMETER + MESSAGE_PROMPT_SIZE
