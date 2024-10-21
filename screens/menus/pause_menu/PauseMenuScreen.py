import pygame
from screens.Screen import Screen
from screens.menus.menu_elements.button import Button
from screens.menus.menu_elements.indication import Indication
from screens.menus.pause_menu.PauseMenuElement import PauseMenuElement
from screens.states.state_manager import StateManager


class PauseMenuScreen(Screen):
    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager):
        super().__init__(display, window_width, window_height, state_manager)
        self._init_indication()
        self._init_buttons()
        self._selected = PauseMenuElement.RESUME.value

    def _init_indication(self):
        self._top_indication = Indication(self._display, "game on pause", (0.5, 0.07), (self._window_width, self._window_height), False)

    def _init_buttons(self):
        self._resume_button = Button(self._display, " resume ", (0.5, 0.4), (self._window_width, self._window_height), False)
        self._main_menu_button = Button(self._display, " main menu ", (0.5, 0.7), (self._window_width, self._window_height), False)
        self._buttons_lst = [self._main_menu_button, self._resume_button]

    def draw(self):
        self._draw_indications()
        self._draw_buttons()
    def update(self):
        self._update_indications()
        self._update_buttons()

    def _draw_buttons(self):
        for button in self._buttons_lst:
            button.draw()

    def _draw_indications(self):
        self._top_indication.draw()

    def _update_buttons(self):
        for n, button in enumerate(self._buttons_lst):
            if n == self._selected:
                button.select()
            else:
                button.deselect()
            button.update()

    def _update_indications(self):
        self._top_indication.draw()

    def listen_to_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if self._selected == PauseMenuElement.MAIN_MENU.value:
                        self._state_manager.go_to_main()
                    elif self._selected == PauseMenuElement.RESUME.value:
                        self._state_manager.resume_button_selected()
                elif event.key == pygame.K_DOWN:
                    match self._selected:
                        case PauseMenuElement.MAIN_MENU.value:
                            self._selected = 0 if self._selected == 1 else 1
                        case PauseMenuElement.RESUME.value:
                            self._selected = 0 if self._selected == 1 else 1
                elif event.key == pygame.K_UP:
                    match self._selected:
                        case PauseMenuElement.MAIN_MENU.value:
                            self._selected = 0 if self._selected == 1 else 1
                        case PauseMenuElement.RESUME.value:
                            self._selected = 0 if self._selected == 1 else 1