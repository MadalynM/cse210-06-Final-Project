
import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile that is caple of killing the gold minner.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the gold is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._second_segments = []
        self._third_segments = []
        self._fourth_segments = []
        self._prepare_body()
        self._prepare_second_snake_body()
        self._prepare_third_snake_body()
        self._prepare_fourth_snake_body()
        
      


    def get_segments(self):
        return self._segments

    def get_second_snake_segments(self):
        return self._second_segments
    
    def get_third_snake_segments(self):
        return self._third_segments
    def get_fourth_snake_segments(self):
        return self._fourth_segments


    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        for second_segment in self._second_segments:
            second_segment.move()
        for third_segment in self._third_segments:
            third_segment.move_next()
        for fourth_segment in self._fourth_segments:
            fourth_segment.move()

        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

        for i in range(len(self._second_segments) - 1, 0, -1):
            trailing = self._second_segments[i]
            previous = self._second_segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    
    def _prepare_body(self):
        x = int(constants.MAX_X+100)
        y = int(constants.MAX_Y-500 )
        

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.GREEN
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def _prepare_second_snake_body(self):
       x = int(constants.MAX_X+200)
       y = int(constants.MAX_Y - 400)

       for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "0"
            color =  constants.YELLOW
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._second_segments.append(segment)

    def _prepare_third_snake_body(self):
       x = int(constants.MAX_X+300)
       y = int(constants.MAX_Y-300)

       for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "0"
            color =  constants.RED
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._third_segments.append(segment)

    def _prepare_fourth_snake_body(self):
       x = int(constants.MAX_X +350)
       y = int(constants.MAX_Y-200)

       for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "0"
            color =  constants.YELLOW
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._fourth_segments.append(segment)