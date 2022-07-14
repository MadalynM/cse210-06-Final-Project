import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Gold(Actor):
    """
    A Mineral that can make miner's rich.
    
    The responsibility of Gold is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the gold is worth.
    """
    def __init__(self):
        "Constructs a new gold."
        super().__init__()
        self._points = 0
        self.set_text("@")
        
        self.set_color(constants.RED)
        self.reset()
        
    def reset(self):
        """Selects a random position the gold appears and its worth(point)."""
        self._points = random.randint(1, 8)
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)
        self.set_position(position)
        
    def get_points(self):
        """Gets the points the gold is worth.
        
        Returns:
            points (int): The points the gold is worth.
        """
        return self._points