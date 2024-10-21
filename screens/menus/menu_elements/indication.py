import string
import pygame

from engine.color import Color
from screens.menus.menu_elements.menu_element import MenuElement


class Indication(MenuElement):
    counter_max = 230
    counter_min = 127

    def __init__(self, display: pygame.display, text: string, x_y_ratio: (float, float), windows_size: (int, int), shiny: bool, text_color = Color.grey()):
        super().__init__(display, text, x_y_ratio, windows_size)
        self._counter = self.counter_min
        self._add_counter = 1
        self._shiny = bool

    def draw(self):
        if self._shiny:
            self._update_text_img()
            # self._update_text_img(Color)
        self._text_img.set_alpha(self._counter)
        self._display.blit(self._text_img, self._text_top_left)

    def update(self):
        if self._shiny:
            if self._counter >= self.counter_max:
                self._add_counter = -1
            elif self._counter <= self.counter_min:
                self._add_counter = 1
            self._counter += self._add_counter
    def shiny(self):
        self._shiny = True
    def unshiny(self):
        self._shiny = False
