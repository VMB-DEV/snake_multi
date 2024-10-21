import pygame

from engine import values
from engine.color import Color
from screens.game.game_objects.corner import Corner
from screens.game.game_objects.direction import Direction
from screens.game.game_objects.game_object_type import GameObjectType
from screens.game.grid_position import GridPosition
from screens.game.matrix import Matrix
from screens.game.game_objects.game_object import GameObject


class Snake(GameObject):
    def __init__(self, direction: Direction, grid_position: GridPosition, grid_unit_size: int,color: Color):
        super().__init__(grid_position = grid_position, t_game_object = GameObjectType.SNAKE, color = color)
        self._direction = direction
        self._grid_unit_size = grid_unit_size
        self._delta = grid_unit_size // 3.8
        self._len = len(self._grid_positions)
        self._growing = False

    def update_position(self):
        next_position = self._grid_positions[0].next_position(self._direction)
        self._grid_positions.insert(0, next_position)
        if self._growing:
            self._growing = False
        else:
            del self._grid_positions[-1]
        self._len = len(self._grid_positions)

    def draw(self, matrix, display):
        for i, bodyPartPosition in enumerate(self._grid_positions):
            rect = matrix.get_Rect_at(bodyPartPosition)
            if i == 0:
                polygon = self.get_head_polygon(rect)
                pygame.draw.polygon(display, self.get_colors(), polygon)
            elif self._len - 1 > i > 0:
                corner = self.get_corner(i)
                polygon = self.get_corner_polygon(corner, rect)
                pygame.draw.polygon(display, self.get_colors(), polygon)
            else :
                polygon = self.get_corner_polygon(Corner.NONE, rect)
                pygame.draw.polygon(display, self.get_colors(), polygon)

    def get_corner(self, i):
        p = self._grid_positions[i - 1]
        m = self._grid_positions[i]
        n = self._grid_positions[i + 1]

        if (m._x > p._x and m._y > n._y) or (m._x > n._x and m._y > p._y):
            return Corner.BOT_RIGHT
        elif (m._x < p._x and m._y > n._y) or (m._x < n._x and m._y > p._y):
            return Corner.BOT_LEFT
        elif (m._x < p._x and m._y < n._y) or (m._x < n._x and m._y < p._y):
            return Corner.TOP_LEFT
        elif (m._x > p._x and m._y < n._y) or (m._x > n._x and m._y < p._y):
            return Corner.TOP_RIGHT
        else:
            return Corner.NONE

    def get_corner_polygon(self, corner, rect):
        delta = self._delta
        top_left = rect.topleft
        top_left_delta_right = (top_left[0] + delta, top_left[1])
        top_left_delta_down = (top_left[0], top_left[1] + delta)
        top_right = rect.topright
        top_right_delta_left = (top_right[0] - delta, top_right[1])
        top_right_delta_down = (top_right[0], top_right[1]+ delta)
        bot_right = rect.bottomright
        bot_right_delta_left = (bot_right[0] - delta, bot_right[1])
        bot_right_delta_up = (bot_right[0], bot_right[1]- delta)
        bot_left = rect.bottomleft
        bot_left_delta_right = (bot_left[0] + delta, bot_left[1])
        bot_left_delta_up = (bot_left[0], bot_left[1] - delta)
        match corner:
            case Corner.TOP_LEFT:
                polygon = (top_left_delta_down, top_left_delta_right, top_right, bot_right, bot_left)
            case Corner.TOP_RIGHT:
                polygon = (top_right_delta_down, top_right_delta_left, top_left, bot_left, bot_right)
            case Corner.BOT_RIGHT:
                polygon = (bot_right_delta_up, bot_right_delta_left, bot_left, top_left, top_right)
            case Corner.BOT_LEFT:
                polygon = (bot_left_delta_up, bot_left_delta_right, bot_right, top_right, top_left)
            case _:
                polygon = (bot_left, bot_right, top_right, top_left)
        return polygon


    def get_head_polygon(self, rect):
        delta = self._delta
        top_left = rect.topleft
        top_left_delta_right = (top_left[0] + delta, top_left[1])
        top_left_delta_down = (top_left[0], top_left[1] + delta)
        top_right = rect.topright
        top_right_delta_left = (top_right[0] - delta, top_right[1])
        top_right_delta_down = (top_right[0], top_right[1]+ delta)
        bot_right = rect.bottomright
        bot_right_delta_left = (bot_right[0] - delta, bot_right[1])
        bot_right_delta_up = (bot_right[0], bot_right[1]- delta)
        bot_left = rect.bottomleft
        bot_left_delta_right = (bot_left[0] + delta, bot_left[1])
        bot_left_delta_up = (bot_left[0], bot_left[1] - delta)
        match self._direction:
            case Direction.UP:
                polygon = (top_left_delta_down, top_left_delta_right, top_right_delta_left, top_right_delta_down, bot_right, bot_left)
            case Direction.DOWN:
                polygon = (bot_left_delta_up, bot_left_delta_right, bot_right_delta_left, bot_right_delta_up, top_right, top_left)
            case Direction.RIGHT:
                polygon = (bot_right_delta_left, bot_right_delta_up, top_right_delta_down, top_right_delta_left, top_left, bot_left)
            case Direction.LEFT:
                polygon = (bot_left_delta_right, bot_left_delta_up, top_left_delta_down, top_left_delta_right, top_right, bot_right)
            case _ :
                polygon = (bot_left, bot_right, top_right, top_left)
        return polygon

    def update_direction(self, direction):
        if not isinstance(direction, Direction):
            raise ValueError(f"Snake.get_head_rect : ERROR direction missType")
        if self._direction.canChangeTo(direction):
            self._direction = direction

    def get_head_rect(self, matrix):
        if not isinstance(matrix, Matrix):
            raise ValueError(f"Snake.update_direction : ERROR matrix missType")
        return self._grid_positions[0].as_Rect(matrix)

    def head_grid_position(self):
        return self._grid_positions[0]

    def is_eating_donut(self, donut):
        result = self.head_grid_position() == donut.get_pos()
        return result
    def grow(self):
        self._growing = True

    def is_eating_him_self(self):
        return self.head_grid_position() in self.body_no_head
    def is_eating_other_snake(self, snake):
        return self.head_grid_position() in snake.body_no_head

    @property
    def body_no_head(self):
        return self._grid_positions[1:]
    @property
    def score(self):
        return len(self._grid_positions)

    @classmethod
    def create_snake_one(cls, grid_unit_size: int, color: Color):
        return Snake(direction = Direction.UP, grid_position = GridPosition(0, 0), grid_unit_size=grid_unit_size, color = color)

    @classmethod
    def create_snake_two(cls, grid_unit_size: int, color: Color):
        return Snake(direction = Direction.UP, grid_position = GridPosition(values.gridSize - 1, 0), grid_unit_size=grid_unit_size, color = color)
