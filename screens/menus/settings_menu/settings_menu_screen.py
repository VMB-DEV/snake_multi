import pygame

from engine.color import Color
from screens.Screen import Screen
from screens.menus.menu_elements.button import Button
from screens.menus.menu_elements.indication import Indication
from screens.menus.settings_menu.key_set import KeySet
from screens.menus.settings_menu.settings_elements import SettingsElements
from screens.states.state_manager import StateManager
from typing import List


class SettingsMenuScreen(Screen):
    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager, key_sets: (KeySet, KeySet)):
        super().__init__(display, window_width, window_height, state_manager)
        self._key_sets = key_sets
        self._init_buttons()
        self._init_indications()
        self._selected_x = 0
        self._selected_y = 0
        self._listen_to_new_key = False

    def _init_indications(self):
        self._top_instruction = Indication(self._display, "press return key to select a new key", (0.4, 0.07), (self._window_width, self._window_height), True, Color.grey())
        self._p1_indication = self._create_indication(text="player 1", x_y_ratios=(0.14, 0.2), shiny=False, color=Color.grey())
        self._p2_indication = self._create_indication(text="player 2", x_y_ratios=(0.62, 0.2), shiny=False, color=Color.grey())
        self._init_indication_text()

    def _init_indication_text(self):
        p1_x_ratio = 0.35
        p2_x_ratio = 0.80
        up_y_ratio = 0.3
        down_y_ratio = 0.45
        left_y_ratio = 0.6
        right_y_ratio = 0.75
        self._indications: List[List[Indication]] = [
            [
                self._create_indication(text=f"{self._key_sets[0].up_name}", x_y_ratios=(p1_x_ratio, up_y_ratio), shiny=False, color=Color.grey()),
                self._create_indication(text=f"{self._key_sets[0].down_name}", x_y_ratios=(p1_x_ratio, down_y_ratio), shiny=False, color=Color.grey()),
                self._create_indication(text=f"{self._key_sets[0].left_name}", x_y_ratios=(p1_x_ratio, left_y_ratio), shiny=False, color=Color.grey()),
                self._create_indication(text=f"{self._key_sets[0].right_name}", x_y_ratios=(p1_x_ratio, right_y_ratio), shiny=False, color=Color.grey()),
            ],
            [
                self._create_indication(text=f"{self._key_sets[1].up_name}", x_y_ratios=(p2_x_ratio, up_y_ratio), shiny=False, color=Color.grey()),
                self._create_indication(text=f"{self._key_sets[1].down_name}", x_y_ratios=(p2_x_ratio, down_y_ratio), shiny=False, color=Color.grey()),
                self._create_indication(text=f"{self._key_sets[1].left_name}", x_y_ratios=(p2_x_ratio, left_y_ratio), shiny=False, color=Color.grey()),
                self._create_indication(text=f"{self._key_sets[1].right_name}", x_y_ratios=(p2_x_ratio, right_y_ratio), shiny=False, color=Color.grey()),
            ]
        ]

    def _init_buttons(self):
        p1_x_ratio = 0.15
        p2_x_ratio = 0.60
        up_y_ratio = 0.3
        down_y_ratio = 0.45
        left_y_ratio = 0.6
        right_y_ratio = 0.75
        self._button_main_menu = self._create_button(text="main menu", x_y_ratios=(0.38, 0.9), selected=False)
        self._buttons: List[List[Button]] =  [
            [
                self._create_button(text="  up  ", x_y_ratios=(p1_x_ratio, up_y_ratio), selected=False),
                self._create_button(text=" down ", x_y_ratios=(p1_x_ratio, down_y_ratio), selected=False),
                self._create_button(text=" left ", x_y_ratios=(p1_x_ratio, left_y_ratio), selected=False),
                self._create_button(text="right ", x_y_ratios=(p1_x_ratio, right_y_ratio), selected=False),
            ],
            [
                self._create_button(text="  up  ", x_y_ratios=(p2_x_ratio, up_y_ratio), selected=False),
                self._create_button(text=" down ", x_y_ratios=(p2_x_ratio, down_y_ratio), selected=False),
                self._create_button(text=" left ", x_y_ratios=(p2_x_ratio, left_y_ratio), selected=False),
                self._create_button(text="right ", x_y_ratios=(p2_x_ratio, right_y_ratio), selected=False),
            ]
        ]

    def draw(self):
        self._top_instruction.draw()
        self._p1_indication.draw()
        self._p2_indication.draw()
        for column in self._buttons:
            for button in column:
                button.draw()
        for column in self._indications:
            for indication in column:
                indication.draw()
        self._button_main_menu.draw()

    def update(self):
        self._top_instruction.update()
        self._p1_indication.update()
        self._p2_indication.update()
        for c, column in enumerate(self._indications):
            for r,indication in enumerate(column):
                indication.update()
                if self._selected_x == c and self._selected_y == r:
                    indication.shiny()
        for c, column in enumerate(self._buttons):
            for r, button in enumerate(column):
                if self._selected_x == c and self._selected_y == r:
                    button.select()
                else:
                    button.deselect()
                button.update()
        if self._selected_y == SettingsElements.MAIN_MENU.value:
            self._button_main_menu.select()
            self._button_main_menu.update()
        else:
            self._button_main_menu.deselect()
            self._button_main_menu.update()

    def listen_to_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if self._listen_to_new_key:
                    match self._selected_y:
                        case SettingsElements.UP.value:
                            self._key_sets[self._selected_x].update_up(event.key)
                            self._indications[self._selected_x][self._selected_y].set_text(self._key_sets[0].up_name)
                        case SettingsElements.DOWN.value:
                            self._key_sets[self._selected_x].update_down(event.key)
                            self._indications[self._selected_x][self._selected_y].set_text(self._key_sets[0].down_name)
                        case SettingsElements.LEFT.value:
                            self._key_sets[self._selected_x].update_left(event.key)
                            self._indications[self._selected_x][self._selected_y].set_text(self._key_sets[0].left_name)
                        case SettingsElements.RIGHT.value:
                            self._key_sets[self._selected_x].update_right(event.key)
                            self._indications[self._selected_x][self._selected_y].set_text(self._key_sets[0].right_name)
                        case SettingsElements.MAIN_MENU.value:
                            print("SettingsMenUScreen.listen_to_input ERROR")
                    self._deactivate_key_indication()
                    self._listen_to_new_key = False
                elif event.key == pygame.K_RETURN:
                    if self._selected_y == SettingsElements.MAIN_MENU.value:
                        self._state_manager.go_to_main()
                    else:
                        self._listen_to_new_key = True
                        self._activate_key_indication()
                elif event.key == pygame.K_UP:
                    self._selected_y = self._selected_y - 1 if self._selected_y > SettingsElements.UP.value else SettingsElements.MAIN_MENU.value
                elif event.key == pygame.K_DOWN:
                    self._selected_y = self._selected_y + 1 if self._selected_y < SettingsElements.MAIN_MENU.value else SettingsElements.UP.value
                elif event.key == pygame.K_LEFT:
                    self._selected_x = 0 if self._selected_x == 1 else 1
                elif event.key == pygame.K_RIGHT:
                    self._selected_x = 0 if self._selected_x == 1 else 1

    def _activate_key_indication(self):
        self._indications[self._selected_x][self._selected_y].set_text_color(Color.white())

    def _deactivate_key_indication(self):
        self._indications[self._selected_x][self._selected_y].set_text_color(Color.grey())