
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast

class Player(Actor):
    def __init__(self):
        "Constructs a new player."
        """The responsibility of the player is to display itself at a given position
        and move pass objects to find gold
        """
        super().__init__()
        self.player = Actor()
        #self._createPlayer()
        
    def createPlayer(self):
         
         cast = Cast()
         x = int(constants.MAX_X / 2)
         y = int(constants.MAX_Y /3)
         position = Point(x, y)
         self.player.set_text("#")
         self.player.set_font_size(constants.FONT_SIZE)
         self.player.set_color(constants.WHITE)
         self.player.set_position(position)
         return self.player