import string
import pygame
from engine.color import Color
from screens.menus.menu_elements.menu_element import MenuElement


class Button(MenuElement):
    counter_max = 255
    counter_min = 200
    step_plus = 0.7
    step_minus = -1.2

    def __init__(self, display: pygame.display, text: string, x_y_ratio: (float, float), window_size: (int, int), selected: bool):
        super().__init__(display, text, x_y_ratio, window_size, Color.grey())
        self._selected = selected
        self._init_borders()
        self._counter = self.counter_min
        self._add_counter = self.step_plus
        self._border_color = Color.grey()

    def _init_borders(self):
        self._square_dimension = ( self._text_width * 1.3, self._text_height * 2)
        self._square_top_left = (self._text_top_left[0] - self._text_width * 0.15, self._text_top_left[1] - self._text_height * 0.5)
        pygame.draw.rect(self._display, self._text_color.rgb, (self._square_top_left, self._square_dimension), width=5, border_radius=2)

    def draw(self):
        self._display.blit(self._text_img, self._text_top_left)
        self._update_text_img()
        pygame.draw.rect(self._display, self._border_color.rgb, (self._square_top_left, self._square_dimension), width=5, border_radius=2)

    def _update_colors(self):
        self._text_color = Color(self._counter, self._counter, self._counter)
        self._border_color = Color(self._counter, self._counter, self._counter)

    def update(self):
        if self._selected:
            self._counter += self._add_counter
            self._update_colors()
            if self._counter >= self.counter_max:
                self._add_counter = self.step_minus
            elif self._counter <= self.counter_min:
                self._add_counter = self.step_plus
        else:
            self._text_color = Color.grey()
            self._border_color = Color.grey()

    def select(self):
        self._selected = True

    def deselect(self):
        self._selected = False

    @property
    def is_selected(self):
        return self._selected