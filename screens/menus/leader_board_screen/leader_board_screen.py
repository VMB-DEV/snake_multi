from typing import List

import pygame

from engine.color import Color
from screens.Screen import Screen
from screens.menus.leader_board_screen.leader_board import LeaderBoard
from screens.menus.menu_elements.indication import Indication
from screens.states.state_manager import StateManager


class LeaderBoardScreen(Screen):
    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager):
        super().__init__(display, window_width, window_height, state_manager)
        self._current_player_name = ""
        self._current_player_score = 0
        self._indication_lst : List[Indication] = [
            self._create_indication(text="", x_y_ratios=(0.35, 0.2), shiny=False, color=Color.white()),
            self._create_indication(text="", x_y_ratios=(0.35, 0.28), shiny=False, color=Color.white()),
            self._create_indication(text="", x_y_ratios=(0.35, 0.36), shiny=False, color=Color.white()),
            self._create_indication(text="", x_y_ratios=(0.35, 0.44), shiny=False, color=Color.white()),
            self._create_indication(text="", x_y_ratios=(0.35, 0.52), shiny=False, color=Color.white()),
            self._create_indication(text="", x_y_ratios=(0.35, 0.60), shiny=False, color=Color.white()),
            self._create_indication(text="", x_y_ratios=(0.35, 0.68), shiny=False, color=Color.white()),
        ]
        self._top_indication = self._create_indication(text="Leaderboard", x_y_ratios=(0.5, 0.1), shiny=False, color=Color.white())
        self._main_menu_button = self._create_button(text=" main menu ", x_y_ratios=(0.5, 0.85), selected=True)

    def draw(self):
        self._top_indication.draw()
        for indication in self._indication_lst:
            indication.draw()
        self._main_menu_button.draw()

    def update(self):
        for indication in self._indication_lst:
            indication.update()
        self._main_menu_button.update()

    def listen_to_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self._state_manager.go_to_main()



    def set_name_score(self, name_score: (int, str)):
        self._current_player_name = name_score[0]
        self._current_player_score = name_score[1]
        LeaderBoard.save_score_and_name(name=name_score[0], score=name_score[1])
        self._update_leader_board()

    def _update_leader_board(self):
        scores: int = LeaderBoard.get_scores()
        i = 0
        y = 0.5
        delta = 0.1
        match = -1
        for point in scores.keys():
            self._indication_lst[i].set_text(f"{i + 1}. {point} : {scores[point]}")
            y += delta
            i += 1
            if i >= len(self._indication_lst):
                break
        if match != -1:
            self._indication_lst[match].shiny()