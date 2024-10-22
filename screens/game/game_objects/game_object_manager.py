from typing import List

from screens.game.game_objects.direction import Direction
from engine.color import Color
from screens.game.game_objects.donut import Donut
from screens.game.game_objects.game_object import GameObject
from screens.game.game_objects.snake import Snake
from screens.game.matrix import Matrix
from screens.states.state_manager import StateManager


class GameObjectManager:
    def __init__(self, state_manager: StateManager, matrix: Matrix, multi: bool = False):
        self._state_manager = state_manager
        self._current_score1 = 1
        self._current_score2 = 1
        self._donut = None
        self._lst: List[GameObject] = []
        self._snake1 = None
        self._snake2 = None
        self._snakes_directions = None
        self._wall = None
        self._multi = multi
        self._matrix = matrix
        self.init_snakes()
        self.init_donut()
        self._winner = 0

    def init_snakes(self):
        self._snakes_directions = [Direction.UP, Direction.UP]
        self._snake1 = Snake.create_snake_one(grid_unit_size=self._matrix.unit_size, color=Color.red())
        self._lst.append(self._snake1)
        self._snake2 = None
        if self._multi:
            self._snake2 = Snake.create_snake_two(grid_unit_size=self._matrix.unit_size, color=Color.blue())
            self._lst.append(self._snake2)

    def init_donut(self):
        self._donut = Donut.create_random_position(lst=self._lst, size=self._matrix.unit_size)
        self._lst.append(self._donut)

    def update_first_snake_direction_to(self, direction: Direction):
        self._snakes_directions[0] = direction

    def update_second_snake_direction_to(self, direction: Direction):
        self._snakes_directions[1] = direction

    def update_snakes(self):
        self._snake1.update_direction(self._snakes_directions[0])
        self._snake1.update_position()
        self._current_score1 = self._snake1.score
        if self._multi:
            self._snake2.update_direction(self._snakes_directions[1])
            self._snake2.update_position()
            self._current_score2 = self._snake2.score
            self._are_snakes_each_other()
        self._are_snakes_eating_them_self()
        self._are_snakes_eating()

    def _are_snakes_eating(self):
        if self._snake1.is_eating_donut(self._donut):
            self._snake1.grow()
            self._donut.new_position(lst=self._lst)
        if self._multi:
            if self._snake2.is_eating_donut(self._donut):
                self._snake2.grow()
                self._donut.new_position(lst=self._lst)

    def _are_snakes_eating_them_self(self):
        if self._snake1.is_eating_him_self():
            if self._multi:
               self._winner = 2
            self._state_manager.go_to_game_over()
        if self._multi:
            if self._snake2.is_eating_him_self():
                self._winner = 1
                self._state_manager.go_to_game_over()

    def _are_snakes_each_other(self):
        if self._snake1.is_eating_other_snake(self._snake2):
            self._winner = 2
            self._state_manager.go_to_game_over()
        elif self._snake2.is_eating_other_snake(self._snake1):
            self._winner = 1
            self._state_manager.go_to_game_over()

    def update_donut(self):
        self._donut.update_donut()

    @property
    def list(self):
        return self._lst
    @property
    def score1(self):
        return self._current_score1
    @property
    def score2(self):
        return self._current_score2
    @property
    def highest_score(self):
        return self.score1 if self.score1 > self.score2 else self.score2
    @property
    def winner(self):
        return self._winner
