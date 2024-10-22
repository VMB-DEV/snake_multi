from enum import Enum

class State(Enum):
    SET_SOLO_GAME = 1
    SET_DUO_GAME = 2
    GAME = 3
    GAME_OVER = 4
    MENU_MAIN = 5
    MENU_SETTINGS = 6
    MENU_OPTION = 7
    EXIT = 8
    PAUSE = 9
    RESUME = 10
    SET_LEADER_BOARD = 11
    LEADER_BOARD = 12

    @property
    def is_in_game(self) -> bool:
        return self == self.GAME
