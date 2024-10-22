import string

import pygame

from engine.color import Color


class MenuElement:
    _font_path = "fonts/BigBlueTermPlusNerdFont-Regular.ttf"
    _text_color = Color.grey()

    def __init__(self, display: pygame.display, text: string, x_y_ratio: (float, float), windows_size: (int, int), selected: bool = False):
        self._display = display
        self._text = text
        self._selected = selected
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
        # self._update_text_img()
        self._update_text_img()
        self._display.blit(self._text_img, self._text_top_left)
        self._text_color = Color.white() if self._selected else Color.grey()

    def _update_text_img(self):
        self._text_img = self._font.render(self._text, True, self._text_color.rgb)
