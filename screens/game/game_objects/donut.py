import pygame
from math import cos, sin
from screens.game.game_objects.game_object import GameObject
from screens.game.game_objects.game_object_type import GameObjectType
from screens.game.grid_position import GridPosition


class List:
    pass


class Donut(GameObject):
    def __init__(self, size, grid_position, t_game_object = GameObjectType.DONUT):
        super().__init__(grid_position, t_game_object)
        self.init_donut_resolution(size)
        self.init_donut_animation()

    @classmethod
    def create_random_position(cls, lst, size):
        random_grid_position = GridPosition.get_available_random(lst)
        print(f"Donut.create_random_position {random_grid_position.toString()}")
        return Donut(size, random_grid_position)

    def new_position(self, lst):
        self._grid_positions[0] = GridPosition.get_available_random(gameObjectList=lst)

    def init_donut_animation(self):
        self._A, self._B = 0, 0
        self._thetaSpacing = 7
        self._phiSpacing = 3
        self._R1 = 12
        self._R2 = 20
        self._K2 = 1000
        self._K1 = self._donutResHeight * self._K2 * 3 / (8 * (self._R1 + self._R2))
        self._intensityGrid = [0] * self._donutRes

    def init_donut_resolution(self, size):
        self._intensityMax = 12
        self.init_donut_pixel(size)
        self._donutColor = (255, 255, 0)
        self._S = size
        self._squareResolution = WIDTH, HEIGHT = (size, size)
        self._donutPixelSize = self._pixel_size
        self._donutPixelSize = self._pixel_size
        self._xDonutRes = 0
        self._yDonutRes = 0
        self._donutResWidth = size // self._donutPixelSize
        self._donutResHeight = size // self._donutPixelSize
        self._donutRes = self._donutResWidth * self._donutResHeight

    def init_donut_pixel(self, size):
        if size <= 25:
            self._pixel_size = 1
        elif size <= 50:
            self._pixel_size = 2
        elif size <= 100:
            self._pixel_size = 3
        elif size <= 150:
            self._pixel_size = 4
        else:
            self._pixel_size = 8

    def draw(self, matrix, display):
        k = 0
        for i in range(self._donutResHeight):
            self._yDonutRes += self._donutPixelSize
            for j in range(self._donutResWidth):
                self._xDonutRes += self._donutPixelSize
                if self._intensityGrid[k] != 0:
                    self.draw_ligth(display, matrix, self._intensityGrid[k], self._xDonutRes, self._yDonutRes)
                k += 1
            self._xDonutRes = 0
        self._yDonutRes = 0

    def update_donut(self):
        self.update_output()

    def draw_ligth(self, display, matrix, intensity, x, y):
        light = (intensity) / (self._intensityMax)
        red = self._donutColor[0] * light
        green = self._donutColor[1] * light
        blue = self._donutColor[2] * light
        rectDonutResColor = (red, green, blue)

        rectDonutRes = (matrix.get_Rect_x(self.get_pos()) + self._xDonutRes - self._donutPixelSize,
                        matrix.get_Rect_y(self.get_pos()) + self._yDonutRes - self._donutPixelSize,
                        self._donutPixelSize, self._donutPixelSize)
        pygame.draw.rect(display, rectDonutResColor, rectDonutRes)

    def get_pos(self):
        return self._grid_positions[0]

    def update_output(self):
        zbuffer = [0] * self._donutRes
        self._intensityGrid = [0] * self._donutRes

        hue = 0
        for theta in range(0, 600, self._thetaSpacing):  # theta goes around the cross-sectional circle of a torus, from 0 to 2pi
            for phi in range(0, 600, self._phiSpacing):  # phi goes around the center of revolution of a torus, from 0 to 2pi
                cosA = cos(self._A)
                sinA = sin(self._A)
                cosB = cos(self._B)
                sinB = sin(self._B)
                cosTheta = cos(theta)
                sinTheta = sin(theta)
                cosPhi = cos(phi)
                sinPhi = sin(phi)
                # x, y coordinates before revolving
                circleX = self._R2 + self._R1 * cosTheta
                circleY = self._R1 * sinTheta
                # 3D (x, y, z) coordinates after rotation
                x = circleX * (cosB * cosPhi + sinA * sinB * sinPhi) - circleY * cosA * sinB
                y = circleX * (sinB * cosPhi - sinA * cosB * sinPhi) + circleY * cosA * cosB
                z = self._K2 + cosA * circleX * sinPhi + circleY * sinA
                ooz = 1 / z  # one over z
                # x, y projection
                xp = int(self._donutResWidth / 2 + self._K1 * ooz * x)
                yp = int(self._donutResHeight / 2 - self._K1 * ooz * y)
                position = xp + self._donutResWidth * yp
                # luminance (L ranges from -sqrt(2) to sqrt(2))
                L = cosPhi * cosTheta * sinB - cosA * cosTheta * sinPhi - sinA * sinTheta + cosB * (
                            cosA * sinTheta - cosTheta * sinA * sinPhi)
                if ooz > zbuffer[position]:
                    zbuffer[position] = ooz  # larger ooz means the pixel is closer to the viewer than what's already plotted
                    luminance_index = int(L * 8)  # we multiply by 8 to get luminance_index range 0..11 (8 * sqrt(2) = 11)
                    self._intensityGrid[position] = luminance_index if luminance_index > 0 else 1
        self._A += 0.15
        self._B += 0.07
        hue += 0.002

    def toString(self):
        return(f"D({self._gridPosition._x}, {self._gridPosition._y})")
    def print(self):
        print(self.toString())
