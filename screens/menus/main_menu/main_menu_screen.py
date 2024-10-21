import pygame

from screens.game.game_screen import GameScreen
from screens.menus.menu_elements.button import Button
from screens.menus.main_menu.Screen import Screen
from screens.menus.menu_elements.indication import Indication
from screens.menus.settings_menu.key_set import KeySet
from screens.states.state import State
from screens.states.state_manager import StateManager

class MainMenuScreen(Screen):
    counter_max = 210
    counter_min = 127

    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager):
        super().__init__(display, window_width, window_height, state_manager)
        self._button_p1 = Button(self._display, "1 Player", (0.2, 0.3), (window_width, window_height), True)
        self._button_p2 = Button(self._display, "2 Player", (0.8, 0.3), (window_width, window_height), False)
        self._button_settings = Button(self._display, "settings", (0.5, 0.5), (window_width, window_height), False)
        self._instruction = Indication(self._display, "select with arrow keys and return key", (0.5, 0.7), (window_width, window_height), True)
        self._precedent_selection = 1

    def draw(self):
        self._instruction.draw()
        self._button_p1.draw()
        self._button_p2.draw()
        self._button_settings.draw()

    def update(self):
        self._instruction.update()
        self._button_p1.update()
        self._button_p2.update()
        self._button_settings.update()

    def listen_to_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self._button_p1.is_selected:
                        self._state_manager.switch_state(State.SET_SOLO_GAME)
                        # self._state_manager.launch_game(self._button_p2.is_selected)
                    elif self._button_p2.is_selected:
                        self._state_manager.switch_state(State.SET_DUO_GAME)
                        # self._state_manager.launch_game(self._button_p2.is_selected)
                    else:
                        self._state_manager.go_to_settings()
                elif event.key == pygame.K_UP:
                    if self._precedent_selection == 1:
                        self._select_button_1p()
                    else:
                        self._select_button_2p()
                elif event.key == pygame.K_LEFT:
                    self._select_button_1p()
                elif event.key == pygame.K_RIGHT:
                    self._select_button_2p()
                elif event.key == pygame.K_DOWN:
                    self._select_button_setting()

    def _select_button_1p(self):
        self._precedent_selection = 1
        self._button_settings.deselect()
        self._button_p2.deselect()
        self._button_p1.select()

    def _select_button_2p(self):
        self._precedent_selection = 2
        self._button_settings.deselect()
        self._button_p1.deselect()
        self._button_p2.select()

    def _select_button_setting(self):
        self._button_p1.deselect()
        self._button_p2.deselect()
        self._button_settings.select()