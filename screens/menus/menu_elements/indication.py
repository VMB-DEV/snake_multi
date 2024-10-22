import string
import pygame

from engine.color import Color
from screens.menus.menu_elements.menu_element import MenuElement


class Indication(MenuElement):
    counter_max = 230
    counter_min = 127

    def __init__(self, display: pygame.display, text: string, x_y_ratio: (float, float), window_size: (int, int), shiny: bool, text_color = Color.grey()):
        super().__init__(display, text, x_y_ratio, window_size, text_color)
        self._counter = self.counter_min
        self._add_counter = 1
        self._shiny = shiny

    def draw(self):
        if self._shiny:
            self._update_text_img()
            self._text_img.set_alpha(self._counter)
        self._display.blit(self._text_img, self._text_top_left)

    def _update_text_img(self):
        self._text_img = self._font.render(self._text, True, self._text_color.rgb)

    def update(self):
        if self._shiny:
            if self._counter >= self.counter_max:
                self._add_counter = -1
            elif self._counter <= self.counter_min:
                self._add_counter = 1
            self._counter += self._add_counter
        self._update_text_img()

    def shiny(self):
        self._shiny = True
    def unshiny(self):
        self._shiny = False