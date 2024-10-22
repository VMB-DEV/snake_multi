from screens.states.state import State

class StateManager:
    def __init__(self, state=State.MENU_MAIN):  # Valeur par défaut: State.MENU_MAIN
        self._l_state = [state]
        self._current_state = state  # Initialisation avec l'état passé ou MENU_MAIN par défaut

    def switch_state(self, new_state):
        self._l_state[0] = new_state
        self._current_state = new_state

    def go_to_leader_board(self):
        if self.state == State.SET_LEADER_BOARD:
            self.switch_state(new_state=State.LEADER_BOARD)
        else:
            print(f"StateManage current state {self.state}\nCan not go to leader board")

    def set_leader_board(self):
        if self.state == State.GAME_OVER:
            self.switch_state(new_state=State.SET_LEADER_BOARD)
        else:
            print(f"StateManage current state {self.state}\nCan not set_leader_board")

    def go_to_game_over(self):
        if self.state.is_in_game:
            self.switch_state(new_state=State.GAME_OVER)
        else:
            print(f"StateManage current state {self.state}\nCan not end_of_game")

    def go_to_pause(self):
        if self.is_in_game():
            self.switch_state(new_state=State.PAUSE)
        else:
            print(f"StateManage current state {self.state}\nCan not pause")

    def go_to_main(self):
        if self.is_settings or self.is_paused:
            self.switch_state(new_state=State.MENU_MAIN)
        else:
            print(f"StateManage current state {self.state}\nCan not go_to_main")

    def go_to_settings(self):
        if self.is_main_menu():
            self.switch_state(new_state=State.MENU_SETTINGS)
        else:
            print(f"StateManage current state {self.state}\nCan not go to settings")

    def launch_game(self):
        if self.is_game_set:
            self.switch_state(State.GAME)
        else:
            print(f"StateManage current state {self.state}\nCan not launch_game")

    def resume_button_selected(self):
        self.switch_state(new_state=State.RESUME)

    # def resume_game(self, multi: bool):
    def resume_game(self):
        # self.switch_state(new_state=State.DUO_GAME if multi else State.SOLO_GAME)
        self.switch_state(State.GAME)

    @property
    def is_game_set(self):
        return self._current_state == State.SET_SOLO_GAME or self._current_state == State.SET_DUO_GAME
    @property
    def is_paused(self):
        return self._current_state == State.PAUSE
    @property
    def is_settings(self):
        return self._current_state == State.MENU_SETTINGS
    def is_main_menu(self):
        return self._current_state == State.MENU_MAIN

    def get_state(self):
        return self._current_state

    def is_in_game(self):
        return self._current_state == State.GAME
        # return self._current_state == State.SOLO_GAME or self._current_state == State.DUO_GAME

    def is_it_option_menu(self):
        return self._current_state == State.MENU_OPTION

    def is_it_exit(self):
        return self._current_state == State.EXIT

    def is_it_pause(self):
        return self._current_state == State.PAUSE

    @property
    def state(self):
        return self._current_state

