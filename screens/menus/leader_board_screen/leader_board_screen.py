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
            Indication(self._display, "", (0.35, 0.2), (self._window_width, self._window_height), False, Color.white()),
            Indication(self._display, "", (0.35, 0.28), (self._window_width, self._window_height), False, Color.white()),
            Indication(self._display, "", (0.35, 0.36), (self._window_width, self._window_height), False, Color.white()),
            Indication(self._display, "", (0.35, 0.44), (self._window_width, self._window_height), False, Color.white()),
            Indication(self._display, "", (0.35, 0.52), (self._window_width, self._window_height), False, Color.white()),
            Indication(self._display, "", (0.35, 0.60), (self._window_width, self._window_height), False, Color.white()),
            Indication(self._display, "", (0.35, 0.68), (self._window_width, self._window_height), False, Color.white()),
        ]
        self._top_indication = Indication(self._display, "Leaderboard", (0.5, 0.1), (self._window_width, self._window_height), False, Color.white())
        # self._main_menu_button = self._create_button(text=" main menu ", x_y_ratios=(0.5, 5))

    def draw(self):
        self._top_indication.draw()
        for indication in self._indication_lst:
            indication.draw()
    def update(self):
        for indication in self._indication_lst:
            indication.update()
    def listen_to_input(self):
        pass

    def set_name_score(self, name_score: (int, str)):
        self._current_player_name = name_score[0]
        self._current_player_score = name_score[1]
        LeaderBoard.save_score_and_name(name=name_score[0], score=name_score[1])
        self._update_leader_board()

    def _update_leader_board(self):
        scores: int = LeaderBoard.get_scores()
        top_scores = []
        i = 0
        y = 0.5
        delta = 0.1
        match = -1
        for point in scores.keys():
            # if point == f"{self._current_player_score}" and scores[point] == self._current_player_name:
            #     match = i
            self._indication_lst[i].set_text(f"{i + 1}. {point} : {scores[point]}")
            y += delta
            i += 1
            if i >= len(self._indication_lst):
                break
        if match != -1:
            self._indication_lst[match].shiny()
        # self.draw()
        # else:
            # self._indication_lst.append(Indication(self._display, "you are not yet in the top players", (0.5, 0.9), (self._window_width, self._window_height), True, Color.grey()), )

        # if (f"{self._current_player_score}", self._current_player_name) in top_scores:
        #     self._indication_lst[self._current_player_score].shiny()
        # else:
        #     self._indication_lst.append( Indication(self._display, "you are not yet in the top players", (0.5, 0.9), (self._window_width, self._window_height), True, Color.grey()), )
            # self._indication_lst.append( Indication(self._display, "...", (0.35, 0.85), (self._window_width, self._window_height), False, Color.grey()), )
            # self._indication_lst.append( Indication(self._display, "", (0.35, 0.9), (self._window_width, self._window_height), false, Color.white()), )
            # Indication(self._display, f"{i + 1}. {self._current_player_score} : {self._current_player_name}", (0.35, 0.2), (self._window_width, self._window_height), false, Color.white()),