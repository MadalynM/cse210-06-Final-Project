import os
import constants
from game.casting.actor import Actor
from game.casting.message import Message
from game.scripting.action import Action
from game.shared.point import Point
class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the gold, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self.message = Message()
    
       
    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_gold_collision(cast)
            self._handle_objects_collision(cast)
            self._handle_game_over(cast)

    def _handle_gold_collision(self, cast):
        """Updates the score nd moves the gold if the snake collides with the gold.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score = cast.get_first_actor("scores")
        gold = cast.get_first_actor("gold")
        player = cast.get_first_actor("player")
    

        if player.get_position().equals(gold.get_position()):
            points = gold.get_points()
            self.message.draw()
            score.add_points(points)
            gold.reset()
    
    def _handle_objects_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake = cast.get_first_actor("snakes")
        second_snake = cast.get_first_actor("second snake")
        third_snake = cast.get_first_actor("third snake")
        fourth_snake = cast.get_first_actor("fourth snake")
        segments = snake.get_segments()
        second_segments = second_snake.get_second_snake_segments()
        third_segments = third_snake.get_third_snake_segments()
        fourth_segments = fourth_snake.get_fourth_snake_segments()
        score = cast.get_first_actor("scores")
        
        player = cast.get_first_actor("player")

        rocks = cast.get_first_actor("rocks")
        
        for segment in segments:
            if player.get_position().equals(segment.get_position()):
                self._is_game_over = True
        for second_segment in second_segments:
            if player.get_position().equals(second_segment.get_position()):
                self._is_game_over = True
        
        for third_segment in third_segments:
            if player.get_position().equals(third_segment.get_position()):
                self._is_game_over = True
        
        for fourth_segment in fourth_segments:
            if player.get_position().equals(fourth_segment.get_position()):
                self._is_game_over = True
        
        
        if player.get_position().equals(rocks.get_position()):
            score.reset_points(0)
        
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and gold white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            gold = cast.get_first_actor("gold")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)
            gold.set_color(constants.WHITE)