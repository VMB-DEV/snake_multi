import pygame

from engine.color import Color
from screens.Screen import Screen
from screens.menus.menu_elements.indication import Indication
from screens.states.state_manager import StateManager

class GameOverMenuScreen(Screen):
    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager, snake_1_win: bool, score: int = 0):
        super().__init__(display, window_width, window_height, state_manager)
        self._score = score
        self._snake_1_win = snake_1_win
        self._name = ""
        self._current_score_indication = Indication(self._display, f"you just made : {score} points", (0.5, 0.2), (self._window_width, self._window_height), False, Color.white())
        self._name_indication = Indication(self._display, self._name, (0.5, 0.5), (self._window_width, self._window_height), False, Color.white())
        self._bottom_indication = Indication(self._display, "press enter to save your name", (0.5, 0.8), (self._window_width, self._window_height), False, Color.white())

    def draw(self):
        self._name_indication.draw()
        self._bottom_indication.draw()
        self._current_score_indication.draw()

    def listen_to_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self._del_char_name()
                elif event.key == pygame.K_RETURN and len(self._name) > 0 :
                    self._state_manager.set_leader_board()
                elif len(self._name) < 10:
                    input_str = pygame.key.name(event.key)
                    if input_str.isalnum():
                        self.update_name(input_str)

    def update(self):
        self._name_indication = Indication(self._display, self._name, (0.5, 0.5), (self._window_width, self._window_height), False, Color.white())
        self._bottom_indication.update()
        self._current_score_indication.update()

    def update_name(self, char: str):
        self._name = f"{self._name}{char}"

    def _del_char_name(self):
        if len(self._name) > 0:
            self._name = self._name[:-1]

    def set_score(self, score: int):
        self._score = score
        self._current_score_indication = Indication(self._display, f"you just made : {score} points", (0.5, 0.2), (self._window_width, self._window_height), False, Color.white())

    @property
    def name_score(self) -> (str, int):
        return self._name, self._score