import pygame

class KeySet:
    def __init__(self, up: int, down: int, left: int, right: int):
        self._up = up
        self._down = down
        self._left = left
        self._right = right

    def update_up(self, key: int):
        self._up = key

    def update_down(self, key: int):
        self._down = key

    def update_left(self, key: int):
        self._left = key

    def update_right(self, key: int):
        self._right = key

    def get_key_name(self, key_constant: int):
        return pygame.key.name(key_constant)

    def match_up(self, key):
        return self._up == key

    def match_down(self, key):
        return self._down == key

    def match_left(self, key):
        return self._left == key

    def match_right(self, key):
        return self._right == key

    @property
    def down(self):
        return self._down

    @property
    def left(self):
        return self._left
    @property
    def right(self):
        return self._right

    @property
    def up_name(self):
        # return pygame.key.name(self._up)
        return self.get_key_name(self._up)

    @property
    def down_name(self):
        return self.get_key_name(self._down)
        # return pygame.key.name(self._down)

    @property
    def left_name(self):
        return self.get_key_name(self._left)
        # return pygame.key.name(self._left)

    @property
    def right_name(self):
        return self.get_key_name(self._right)
        # return pygame.key.name(self._right)
