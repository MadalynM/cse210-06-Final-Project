
import constants


from game.casting.cast import Cast
from game.casting.gold import Gold
from game.casting.rock import Rock
from game.casting.score import Score
from game.casting.player import Player
from game.casting.message import Message
from game.casting.snake import Snake
from game.casting.actor import Actor
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
import random


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("gold", Gold())
    cast.add_actor("player", Player().createPlayer())
    cast.add_actor("message", Message())
    cast.add_actor("snakes", Snake())
    cast.add_actor("second snake", Snake())
    cast.add_actor("third snake", Snake())
    cast.add_actor("fourth snake", Snake())
    cast.add_actor("scores", Score())
    cast.add_actor("rocks", Rock().createRock())
    cast.add_actor("second rock", Rock().createRock())
    cast.add_actor("third rock", Rock().createRock())
    cast.add_actor("fourth rock", Rock().createRock())
    cast.add_actor("fifth rock", Rock().createRock())
    cast.add_actor("sixth rock", Rock().createRock())
    cast.add_actor("seventh rock", Rock().createRock())
    cast.add_actor("eighth rock", Rock().createRock())
    cast.add_actor("ninth rock", Rock().createRock())
    cast.add_actor("tenth rock", Rock().createRock())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()