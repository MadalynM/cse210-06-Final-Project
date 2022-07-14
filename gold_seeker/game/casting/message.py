import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Message(Actor):
    """
    A message that display when a gold is found

   
    """
    def __init__(self):
        super().__init__()
    
    
    def draw(self):
        x = int(constants.MAX_X/2)
        y = int(constants.MAX_Y/2)
        position = Point(x, y)


        message = Actor()
        message.set_text("You found gold!")
        message.set_font_size(constants.FONT_SIZE+10)
        message.set_color(constants.GREEN)
        message.set_position(position)