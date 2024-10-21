import pygame
from engine import values
from screens.game.grid_position import GridPosition


class Matrix:
    len = values.gridSize

    def __init__(self, screen_width, screen_height):
        if screen_width != screen_height:
            raise ValueError(f"Matric.init : ERROR screen W {screen_width} != H {screen_height} ")

        self._displayedItems = []
        self._unitSize = screen_width // self.len

        grid = []
        for rowIndex in range(self.len):
            grid.append([])
            pixelY = self._unitSize * rowIndex
            for colIndex in range(self.len):
                pixelX = self._unitSize * colIndex
                grid[rowIndex].append((pixelX, pixelY))

        self._grid = grid

    def get_Rect_at(self, grid_position: GridPosition):
        return pygame.Rect((self.get_Rect_x(grid_position), self.get_Rect_y(grid_position)), (self._unitSize, self._unitSize))

    def get_Rect_x(self, grid_position: GridPosition):
        return grid_position._x * self._unitSize
    def get_Rect_y(self, grid_position: GridPosition):
        return grid_position._y * self._unitSize

    def get_square_top_left(self, grid_position: GridPosition):
        return self.get_Rect_at(grid_position).topleft

    @property
    def unit_size(self):
        return self._unitSize
