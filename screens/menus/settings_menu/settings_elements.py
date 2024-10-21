from enum import Enum

class SettingsElements(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    MAIN_MENU = 4

    @property
    def movements(self):
        return [SettingsElements.UP.value, SettingsElements.DOWN.value, SettingsElements.RIGHT.value, SettingsElements.LEFT.value]