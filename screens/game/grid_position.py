from engine import values
import random
import copy
from screens.game.game_objects.direction import Direction


# from grid_position import GridPosition


class GridPosition:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def next_position(self, direction):
        copy = self.copy()
        match direction:
            case Direction.UP:
                if (self._y == 0):
                    copy._y = values.gridSize - 1
                else:
                    copy._y -= 1
                # self.print()
            case Direction.DOWN:
                if (copy._y == values.gridSize - 1):
                    copy._y = 0
                else:
                    copy._y += 1
                # copy.print()
            case Direction.RIGHT:
                if (copy._x == values.gridSize - 1):
                    copy._x = 0
                else:
                    copy._x += 1
                # copy.print()
            case Direction.LEFT:
                if (copy._x == 0):
                    copy._x = values.gridSize - 1
                else:
                    copy._x -= 1
                # self.print()
            case _:
                print(f"direction else : {direction}")
        return copy

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._x == other._x and self._y == other._y
        else:
            return False

    def toString(self):
        return f"g({self._x}, {self._y})"

    def print(self):
        print(self.toString())

    def copy(self):
        return copy.copy(self)

    @staticmethod
    def get_random():
        x = random.randrange(0, values.gridSize, 1) # génère un nombre aléatoire entre 0 et gridSize - 1 inclus, cette ligne est équivalente à random.randint(0, gridSize - 1), elle est plus rapide. elle genere un nombre aléatoire entre 0 et gridSize - 1 inclus
        y = random.randrange(0, values.gridSize, 1)
        return GridPosition(x, y)

    @staticmethod
    def isGridPositionAvailable(gridPosition, gameObjectList):
        available = True
        for gameObject in gameObjectList:
            if gridPosition in gameObject._grid_positions:
                available = False
                break
        return available
    
    # too much loop cycle when snake gets longer
    @staticmethod
    def get_available_random(gameObjectList):
        gridPosition = GridPosition.get_random()
        available = GridPosition.isGridPositionAvailable(gridPosition, gameObjectList)
        while available == False:
            gridPosition = GridPosition.get_random()
            available = GridPosition.isGridPositionAvailable(gridPosition, gameObjectList)
        return gridPosition;

