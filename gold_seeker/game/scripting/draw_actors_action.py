from unittest.mock import DEFAULT
from game.scripting.action import Action
import constants


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("scores")
        gold = cast.get_first_actor("gold")
        snake = cast.get_first_actor("snakes")
        second_snake = cast.get_first_actor("second snake")
        third_snake = cast.get_first_actor("third snake")
        fourth_snake =cast.get_first_actor("fourth snake")
        found_gold_message =cast.get_first_actor("message")
        segments = snake.get_segments()
        second_segments = second_snake.get_second_snake_segments()
        third_segments = third_snake.get_third_snake_segments()
        fourth_segments = fourth_snake.get_fourth_snake_segments()
        segments = snake.get_segments()
        messages = cast.get_actors("messages")
        rocks = cast.get_first_actor("rocks")
        rock_two = cast.get_first_actor("second rock")
        rock_three = cast.get_first_actor("third rock")
        rock_four = cast.get_first_actor("fourth rock")
        rock_five = cast.get_first_actor("fifth rock")
        rock_six = cast.get_first_actor("sixth rock")
        rock_seven = cast.get_first_actor("seventh rock")
        rock_eight = cast.get_first_actor("eighth rock")
        rock_nine = cast.get_first_actor("ninth rock")
        rock_ten = cast.get_first_actor("tenth rock")
        player = cast.get_actors("player")
        

        self._video_service.clear_buffer()
        self._video_service.draw_actor(gold)
        self._video_service.draw_actor(found_gold_message)
        self._video_service.draw_actors(segments)
        self._video_service.draw_actors(second_segments)
        self._video_service.draw_actors(third_segments)
        self._video_service.draw_actors(fourth_segments)
        self._video_service.draw_actor(score)
        self._video_service.draw_actor(rocks)
        self._video_service.draw_actor(rock_two)
        self._video_service.draw_actor(rock_three)
        self._video_service.draw_actor(rock_four)
        self._video_service.draw_actor(rock_five)
        self._video_service.draw_actor(rock_six)
        self._video_service.draw_actor(rock_seven)
        self._video_service.draw_actor(rock_eight)
        self._video_service.draw_actor(rock_nine)
        self._video_service.draw_actor(rock_ten)
        self._video_service.draw_actors(player)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()