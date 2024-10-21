from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def canChangeTo(self, direction):
        if not isinstance(direction, Direction):
            raise ValueError(f"Direction.canChangeTo : ERROR direction missType")
        match self:
            case Direction.UP:
                return direction != Direction.DOWN
            case Direction.DOWN:
                return direction != Direction.UP
            case Direction.LEFT:
                return direction != Direction.RIGHT
            case Direction.RIGHT:
                return direction != Direction.LEFT
