
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from game.casting.cast import Cast
import random

class Rock(Actor):
    def __init__(self):
        '''A hard compact object that is caple of making the player fall on the ground and loose his golds
          The responsibility of the rock is to display itself at random position on the screen
        '''
        super().__init__()
        self.rock= Actor()
        
    
        
    def createRock(self):
        for n in range(constants.DEFAULT_ROCK):
            x = random.randint(0, constants.COLUMNS-1)
            y = random.randint(0, constants.ROWS-1)
            position = Point(x, y)
            position = position.scale(constants.CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            dx = 0#variable for velocity
            dy = 1
            velocity = Point(dx, dy)#setting velocity
            
            
            
            self.rock.set_text("0")
            self.rock.set_font_size(constants.FONT_SIZE)
            self.rock.set_color(color)
            self.rock.set_position(position)
            self.rock.set_velocity(velocity)
            return self.rock