from enum import Enum

class State(Enum):
    SET_SOLO_GAME = 1
    SET_DUO_GAME = 2
    GAME = 3
    # SOLO_GAME = 3
    # DUO_GAME = 4
    END_GAME = 4
    MENU_MAIN = 5
    MENU_SETTINGS = 6
    MENU_OPTION = 7
    EXIT = 8
    PAUSE = 9
    RESUME = 10

    @property
    def is_in_game(self) -> bool:
        return self == State.SOLO_GAME or self == State.DUO_GAME
