from engine import values
from id import Id
from screens.game.game_objects.game_object import GameObject


class Wall(GameObject):
    def __init__(self, gridPosition):
        super().__init__(gridPosition, Id.WALL, values.grey)

    def is_collision(self, snake):
        return snake.head_grid_position() in self._grid_positions

    @staticmethod
    def create_random_position(gameObjectList):
        from screens.game.grid_position import GridPosition
        randomGridPosition = GridPosition.get_available_random(gameObjectList)
        return Wall(randomGridPosition)
