import string

import pygame

from engine.color import Color


class MenuElement:
    _font_path = "fonts/BigBlueTermPlusNerdFont-Regular.ttf"

    def __init__(self, display: pygame.display, text: string, x_y_ratio: (float, float), windows_size: (int, int), text_color: Color):
        self._text_color = text_color
        self._display = display
        self._text = text
        self._x_ratio = x_y_ratio[0]
        self._y_ratio = x_y_ratio[1]
        self._window_width = windows_size[0]
        self._window_height = windows_size[1]
        self._init_text()

    def _init_text(self):
        pygame.font.init()
        self._font = pygame.font.Font(self._font_path, 25)
        self._text_img = self._font.render(self._text, True, self._text_color.rgb)
        self._text_width = self._text_img.get_width()
        self._text_height = self._text_img.get_height()
        x: int = (self._window_width - self._text_width) * self._x_ratio
        y: int = (self._window_height - self._text_height) * self._y_ratio
        self._text_top_left = (x, y)

    def draw(self):
        self._display.blit(self._text_img, self._text_top_left)

    def _update_text_img(self):
        self._text_img = self._font.render(self._text, True, self._text_color.rgb)

    def set_text(self, text: str):
        self._text = text
    def set_text_color(self, color: Color):
        self._text_color = color
