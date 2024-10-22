import asyncio
import pygame

from screens.menus.game_over_menu.game_over_menu_screen import GameOverMenuScreen
from screens.menus.leader_board_screen.leader_board_screen import LeaderBoardScreen
from screens.menus.main_menu.main_menu_screen import MainMenuScreen
from screens.game.game_screen import GameScreen
from screens.menus.pause_menu.PauseMenuScreen import PauseMenuScreen
from screens.menus.settings_menu.key_set import KeySet
from screens.states.state import State
from screens.states.state_manager import StateManager
from screens.menus.settings_menu.settings_menu_screen import SettingsMenuScreen


class Engine:
    def __init__(self, window_width: int = 800, window_height: int = 800):
        self._window_height = window_height
        self._window_width = window_width
        self._state_manager = StateManager(State.MENU_MAIN)
        # self._state_manager = StateManager(State.GAME_OVER)
        self._display = pygame.display.set_mode((self._window_width, self._window_height))
        self._key_set_p1 = KeySet(pygame.K_i, pygame.K_k, pygame.K_j, pygame.K_l)
        self._key_set_p2 = KeySet(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
        self._game_screen = GameScreen(display=self._display, state_manager=self._state_manager, window_width= window_width, window_height= window_height, key_sets=(self._key_set_p1, self._key_set_p2), multi=False)
        self._settings_menu = SettingsMenuScreen(display=self._display, state_manager=self._state_manager, window_width= window_width, window_height= window_height, key_sets=(self._key_set_p1, self._key_set_p2))
        self._main_menu_screen = MainMenuScreen(display=self._display, state_manager=self._state_manager, window_width= window_width, window_height= window_height)
        self._pause_menu_screen = PauseMenuScreen(display=self._display, state_manager=self._state_manager, window_width= window_width, window_height= window_height)
        self._game_over_screen = GameOverMenuScreen(display=self._display, state_manager=self._state_manager, window_width= window_width, window_height= window_height, snake_1_win=False)
        self._leader_board_screen = LeaderBoardScreen(display=self._display, state_manager=self._state_manager, window_width= window_width, window_height= window_height)

    async def start(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            self._display.fill((52, 78, 91))
            match self._state_manager.state:
                case State.MENU_SETTINGS:
                    self._settings_menu.run()
                case State.MENU_MAIN:
                    self._main_menu_screen.run()
                case State.GAME:
                    self._game_screen.run()
                case State.GAME_OVER:
                    winner = self._game_screen.winner
                    self._game_over_screen.set_winner(winner)
                    score = self._game_screen.highest_score
                    self._game_over_screen.set_score(score)
                    self._game_over_screen.run()
                case State.SET_LEADER_BOARD:
                    name_score: (str, int) = self._game_over_screen.name_score
                    self._leader_board_screen.set_name_score(name_score)
                    self._state_manager.go_to_leader_board()
                case State.LEADER_BOARD:
                    self._leader_board_screen.run()
                case State.PAUSE:
                    self._pause_menu_screen.run()
                case State.SET_SOLO_GAME:
                    self._game_screen.set_solo_game()
                    self._state_manager.launch_game()
                case State.SET_DUO_GAME:
                    self._game_screen.set_duo_game()
                    self._state_manager.launch_game()
                case State.RESUME:
                    self._game_screen.resume()
                    self._state_manager.resume_game()
                case _ :
                    print(f"unknown state {self._state_manager.get_state()}")
            pygame.display.flip()
            clock.tick(60)
            await asyncio.sleep(0)

    @property
    def _game_is_multi(self):
        return self._game_screen.multi

    def __del__(self):
        pygame.quit()