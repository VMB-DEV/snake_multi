from enum import Enum

class Corner(Enum):
    TOP_RIGHT = 1
    TOP_LEFT = 2
    BOT_RIGHT = 3
    BOT_LEFT = 4
    NONE = 5

    def isCorners(self):
        return self != Corner.NONE
