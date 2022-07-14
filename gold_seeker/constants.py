from game.shared.color import Color
import os


COLUMNS = 40
ROWS = 40
CELL_SIZE = 15
MAX_X = 900
MAX_Y = 600
FRAME_RATE = 20
FONT_SIZE = 15
CAPTION = "Gold Seeker"
SNAKE_LENGTH = 10
WHITE = Color(255, 255, 255)
RED = Color(255, 0, 0)
YELLOW = Color(255, 255, 0)
GREEN = Color(0, 255, 0)
BLACK = Color(0, 300, 90)
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/message.txt"