import pygame

from engine.color import Color
from screens.states.state_manager import StateManager


class Screen:
    _font_path = "fonts/BigBlueTermPlusNerdFont-Regular.ttf"

    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager):
        self._display = display
        self._window_height = window_height
        self._window_width = window_width
        self._state_manager = state_manager
        self._text_color = Color.white()
        pygame.font.init()
        self._font = pygame.font.Font(None, 20)
        self._font = pygame.font.Font(self._font_path, 20)

    def run(self):
        self.draw()
        self.update()
        self.listen_to_input()
        
    def draw(self):
        print("not implemented")
        
    def update(self):
        print("not implemented")
        
    def listen_to_input(self):
        print("not implemented")
