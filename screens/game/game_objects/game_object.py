import pygame

from engine import values
from engine.color import Color
from screens.game.game_objects.game_object_type import GameObjectType
from screens.game.grid_position import GridPosition


class GameObject:
    def __init__(self, grid_position, t_game_object: GameObjectType, color: Color = Color.black()):
        self._t_game_object = t_game_object
        self._grid_positions = [grid_position]
        self._color = color
        print(f"GameObject {t_game_object}")

    def draw(self, matrix, display):
        for part_position in self._grid_positions:
            rect = matrix.get_Rect_at(part_position)
            pygame.draw.rect(display, self.get_colors(), rect)

    def get_colors(self) -> (int, int, int):
        return self._color.rgb

    @classmethod
    def create_random_position(cls, l_game_object: list, t_game_object: GameObjectType):
        random_grid_position = GridPosition.get_available_random(l_game_object)
        return GameObject(random_grid_position, t_game_object)