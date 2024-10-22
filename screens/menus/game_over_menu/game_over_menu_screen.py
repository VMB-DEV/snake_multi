import pygame

from engine.color import Color
from screens.Screen import Screen
from screens.menus.menu_elements.indication import Indication
from screens.states.state_manager import StateManager

class GameOverMenuScreen(Screen):
    not_multi = 0
    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager, snake_1_win: bool):
        super().__init__(display, window_width, window_height, state_manager)
        self._score = 0
        self._winner = 0
        self._snake_1_win = snake_1_win
        self._name = ""
        self._top_text = "red snake " if self._winner == 1 else "blue snake " if self._winner == 2 else "you reached"
        self._current_score_indication = self._create_indication(text=f"{self._top_text} reached : {self._score} points", x_y_ratios=(0.5, 0.2), shiny=False, color=Color.white())
        self._name_indication = self._create_indication(text=self._name, x_y_ratios=(0.5, 0.5), shiny=False, color=Color.white())
        self._bottom_indication = self._create_indication(text="press enter to save your name", x_y_ratios=(0.5, 0.8), shiny=True, color=Color.white())

    def update_top_text(self):
        self._top_text = "red snake win" if self._winner == 1 else "blue snake win" if self._winner == 2 else "you reached"

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
        self._name_indication = self._create_indication(text=self._name, x_y_ratios=(0.5, 0.5), shiny=False, color=Color.white())
        self._bottom_indication.update()
        self._current_score_indication.update()

    def update_name(self, char: str):
        self._name = f"{self._name}{char}"

    def _del_char_name(self):
        if len(self._name) > 0:
            self._name = self._name[:-1]

    def set_winner(self, winner: int):
        self._winner = winner

    def set_score(self, score: int):
        self._score = score
        self.update_top_text()
        self._current_score_indication = self._create_indication(text=f"{self._top_text} : {self._score} points", x_y_ratios=(0.5, 0.2), shiny=False, color=Color.white())

    @property
    def name_score(self) -> (str, int):
        return self._name, self._score