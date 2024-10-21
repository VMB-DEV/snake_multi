class Color:
    def __init__(self, red: int, green: int, blue: int):
        self._red = 0 if red < 0 else 255 if red > 255 else red
        self._green = 0 if green < 0 else 255 if green > 255 else green
        self._blue = 0 if blue < 0 else 255 if blue > 255 else blue

    # def rgb(self) -> (int, int, int):
    #     return self._red, self._green, self._blue

    def update_red(self, value):
        self._red = 0 if value < 0 else 255 if value > 255 else value

    def update_green(self, value):
        self._green = 0 if value < 0 else 255 if value > 255 else value

    def update_blue(self, value):
        self._blue = 0 if value < 0 else 255 if value > 255 else value

    @classmethod
    def red(cls):
        return Color(red = 255, green = 0, blue = 0)

    @classmethod
    def blue(cls):
        return Color(red = 0, green = 0, blue = 255)

    @classmethod
    def green(cls):
        return Color(red = 0, green = 255, blue = 0)

    @classmethod
    def grey(cls):
        return Color(red = 150, green = 150, blue = 150)

    @classmethod
    def black(cls):
        return Color(red = 0, green = 0, blue = 0)

    @classmethod
    def white(cls):
        return Color(red = 255, green = 255, blue = 255)

    @property
    def rgb(self):
        return self._red, self._green, self._blue
