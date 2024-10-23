import pygame
from screens.game.game_objects.direction import Direction
from engine.color import Color
from screens.game.game_objects.game_object_manager import GameObjectManager
from screens.game.matrix import Matrix
from screens.Screen import Screen
from screens.menus.settings_menu.key_set import KeySet
from screens.states.state_manager import StateManager


class GameScreen(Screen):
    start_max_counter = 3.0
    start_add_counter = 0.3

    def __init__(self, display: pygame.display, window_width: int, window_height: int, state_manager: StateManager, multi: bool, key_sets: (KeySet, KeySet)):
        super().__init__(display, window_width, window_height, state_manager)
        self._on_pause = False
        self._text_color = Color.white()
        self._key_sets = key_sets
        self._matrix = Matrix(window_width, window_height)
        self._restart(multi)

    def _restart(self, multi: bool):
        self._multi = multi
        self._winner = 0
        self._counter = 0
        self._highest_score = 1
        self._score1 = 1
        self._score2 = 1
        self._add_counter = self.start_add_counter
        self._maxCounter = GameScreen.start_max_counter
        self._game_objects_manager = GameObjectManager(state_manager= self._state_manager, matrix=self._matrix, multi=self._multi)
        self.resume()

    def set_solo_game(self):
        self._restart(False)
    def set_duo_game(self):
        self._restart(True)
    def resume(self):
        self._on_pause = False
    def _pause(self):
        self._on_pause = True

    def listen_to_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self._pause()
                    self._state_manager.go_to_pause()
                elif self._key_sets[0].match_up(event.key):
                    self._game_objects_manager.update_first_snake_direction_to(Direction.UP)
                elif self._key_sets[0].match_right(event.key):
                    self._game_objects_manager.update_first_snake_direction_to(Direction.RIGHT)
                elif self._key_sets[0].match_left(event.key):
                    self._game_objects_manager.update_first_snake_direction_to(Direction.LEFT)
                elif self._key_sets[0].match_down(event.key):
                    self._game_objects_manager.update_first_snake_direction_to(Direction.DOWN)
                if self._multi:
                    if self._key_sets[1].match_up(event.key):
                        self._game_objects_manager.update_second_snake_direction_to(Direction.UP)
                    elif self._key_sets[1].match_right(event.key):
                        self._game_objects_manager.update_second_snake_direction_to(Direction.RIGHT)
                    elif self._key_sets[1].match_left(event.key):
                        self._game_objects_manager.update_second_snake_direction_to(Direction.LEFT)
                    elif self._key_sets[1].match_down(event.key):
                        self._game_objects_manager.update_second_snake_direction_to(Direction.DOWN)

    def draw(self):
        for element in self._game_objects_manager.list:
            element.draw(matrix = self._matrix, display = self._display)
        self.draw_score1()
        if self._multi:
            self.draw_score2()

    def draw_score1(self):
        txt_img = self._font.render(f"score : {self._score1}", True, self._text_color.rgb)
        self._display.blit(txt_img, (5, 5))

    def draw_score2(self):
        txt_img = self._font.render(f"score : {self._score2}", True, self._text_color.rgb)
        self._display.blit(txt_img, (self._window_width - txt_img.get_width() - 5, 5))

    def update(self):
        self._game_objects_manager.update_donut()
        if self._counter >= self._maxCounter:
            self._game_objects_manager.update_snakes()
            if self.highest_score != self._game_objects_manager.highest_score:
                self._highest_score = self._game_objects_manager.highest_score
                self._maxCounter -= self._maxCounter * 0.1
                self._add_counter -= self._add_counter * 0.085
            self._score1 = self._game_objects_manager.score1
            self._score2 = self._game_objects_manager.score2
            self._counter = 0
        self._counter += self._add_counter


    def __del__(self):
        print("GameManager __del__")

    @property
    def highest_score(self) -> int:
        return self._highest_score

    @property
    def score1(self) -> int:
        return self._game_objects_manager.score1

    @property
    def score2(self) -> int:
        return self._game_objects_manager.score2

    @property
    def multi(self):
        return self._multi

    @property
    def winner(self):
        return self._game_objects_manager.winner